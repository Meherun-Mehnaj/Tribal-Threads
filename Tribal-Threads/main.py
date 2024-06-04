from tkinter import *
import tkinter as tk
from tkinter import ttk, font, messagebox
from ttkbootstrap import Style
from PIL import Image, ImageTk
import customtkinter as ctk
import pandas as pd
from mainpagebackup import MainPage
from ADMINpage import Log
from supplierprofile import LogS
from category_page1 import ProductApp
import webbrowser



class SignUpForm:

  def __init__(self, master):
    self.master = master
    self.master.geometry("1280x720")
    self.master.title("Sign Up Page")

    # Load the background image
    self.bg_image = tk.PhotoImage(file=r"signupbg.png")
    self.bg_label = tk.Label(master, image=self.bg_image)
    self.bg_label.place(
        relwidth=1, relheight=1)  # Stretch the image to cover the whole window

    # Ensure widgets are placed on top of the background
    self.bg_label.lower()  # Lower the label to the bottom layer

    # Entry widgets
    self.name_entry = ctk.CTkEntry(master=self.bg_label,
                                   width=280,
                                   height=40,
                                   corner_radius=20,
                                   bg_color="#ceb6af",
                                   placeholder_text="Name",
                                   fg_color="#191C27",
                                   text_color="white",
                                   border_color="grey")
    self.name_entry.place(relx=0.50, rely=0.3, anchor="center")

    self.user_entry = ctk.CTkEntry(
        master=self.bg_label,
        width=280,
        height=40,
        corner_radius=20,
        placeholder_text="Username",
        bg_color="#ceb6af",
        border_color="grey",
        text_color="white",
        fg_color="#191C27",
    )
    self.user_entry.place(relx=0.50, rely=0.39, anchor="center")

    self.email_entry = ctk.CTkEntry(
        master=self.bg_label,
        width=280,
        height=40,
        corner_radius=20,
        placeholder_text="Email",
        text_color="white",
        bg_color="#ceb6af",
        border_color="grey",
        fg_color="#191C27",
    )
    self.email_entry.place(relx=0.50, rely=0.48, anchor="center")

    self.user_pass = ctk.CTkEntry(
        master=self.bg_label,
        width=280,
        height=40,
        corner_radius=20,
        placeholder_text="Password",
        show="*",
        text_color="white",
        bg_color="#cfb69d",
        border_color="grey",
        fg_color="#191C27",
    )
    self.user_pass.place(relx=0.50, rely=0.57, anchor="center")

    # Button widgets
    self.button = ctk.CTkButton(master=self.bg_label,
                                command=self.signUp,
                                width=200,
                                height=40,
                                font=("Arial", 17, "bold"),
                                corner_radius=20,
                                text='Create Account',
                                bg_color="#758330")
    self.button.place(relx=0.50, rely=0.76, anchor="center")

    self.loginbutton = ctk.CTkButton(master=self.bg_label,
                                     command=self.open_login,
                                     font=("Arial", 13, "bold"),
                                     corner_radius=20,
                                     text='Log in',
                                     bg_color="#4f6912",
                                     fg_color="#191C27")
    self.loginbutton.place(relx=0.60, rely=0.88, anchor="center")

    # Dropdown box
    options = ["Customer", "Supplier", "Admin"]  # Example options
    self.user_type = tk.StringVar(master)
    self.default_text = "Select an option"
    self.user_type.set(self.default_text)  # Set the default selected option
    self.user_type = ctk.CTkComboBox(master=self.bg_label,
                                     corner_radius=20,
                                     text_color="#a9a9a9",
                                     values=options,
                                     width=280,
                                     height=40,
                                     fg_color="#191C27",
                                     dropdown_hover_color="grey",
                                     bg_color="#ceb9ab")
    self.user_type.place(relx=0.5, rely=0.66, anchor="center")

  def open_login(self):
    login_window = tk.Toplevel(self.master)
    login_form = LogInForm(login_window)
  def signUp(self):
    try:
      # Load existing user info from CSV
      user_info = pd.read_csv(r"User Info.csv")
    except FileNotFoundError:
      # If CSV file does not exist, create an empty DataFrame
      user_info = pd.DataFrame(
          columns=['user_id', 'username', 'email', 'password', 'user_type'])

    # Get user input data
    user_id = self.user_entry.get()
    username = self.name_entry.get()
    email = self.email_entry.get()
    password = self.user_pass.get()
    user_type = self.user_type.get()

    # Check if email already exists in user_info DataFrame
    if email in user_info["email"].values:
      messagebox.showwarning(
          title='Email Already Taken',
          message='This email is already registered. Please log in.')
      self.name_entry.delete(0, tk.END)
      self.user_entry.delete(0, tk.END)
      self.email_entry.delete(0, tk.END)
      self.user_pass.delete(0, tk.END)
      self.user_type.set(self.default_text)
    else:
      # Create new user data
      new_user_info = pd.DataFrame({
          'user_id': [user_id],
          'username': [username],
          'email': [email],
          'password': [password],
          'user_type': [user_type]
      })
      # Concatenate new data with existing user_info
      user_info = pd.concat([user_info, new_user_info], ignore_index=True)
      # Save the updated DataFrame back to the CSV file
      user_info.to_csv(r"User Info.csv", index=False)
      messagebox.showinfo(title="Registration Successful",
                    message="Account created successfully!")

      # Clear input fields after successful registration
      self.name_entry.delete(0, tk.END)
      self.user_entry.delete(0, tk.END)
      self.email_entry.delete(0, tk.END)
      self.user_pass.delete(0, tk.END)
      self.user_type.set(self.default_text)



class LogInForm(tk.Toplevel):

  def __init__(self, master):
    self.master = master
    self.master.geometry("1280x720")
    self.master.title("Sign Up Page")

    # Load the background image
    self.bg_image = ImageTk.PhotoImage(file="loginbg.png")
    self.bg_label = Label(master, image=self.bg_image)
    self.bg_label.place(relwidth=1, relheight=1)

    # Ensure widgets are placed on top of the background
    self.master.lift(self.bg_label)

    self.button = ctk.CTkButton(master=self.bg_label,
                                command=self.logIn,
                                width=200,
                                height=40,
                                font=("Arial", 18, "bold"),
                                corner_radius=20,
                                text='Log in',
                                bg_color="#141d1a")
    self.button.place(relx=0.50, rely=0.65, anchor="center")

    self.signupbutton = ctk.CTkButton(master=self.bg_label,
                                      command=self.open_signup,
                                      width=7,
                                      font=("Arial", 12, "bold"),
                                      corner_radius=20,
                                      text='Sign Up',
                                      bg_color="#091113")
    self.signupbutton.place(relx=0.58, rely=0.751, anchor="center")

    self.username_entry = ctk.CTkEntry(master=self.bg_label,
                                       border_width=4,
                                       width=280,
                                       height=45,
                                       corner_radius=15,
                                       bg_color="#35392f",
                                       placeholder_text="Username",
                                       fg_color="black",
                                       border_color="white",
                                       text_color="white")
    self.username_entry.place(relx=0.50, rely=0.42, anchor="center")

    self.user_pass = ctk.CTkEntry(master=self.bg_label,
                                  border_width=4,
                                  width=280,
                                  height=45,
                                  corner_radius=15,
                                  placeholder_text="Password",
                                  show="*",
                                  bg_color="#35392f",
                                  border_color="white",
                                  fg_color="black",
                                  text_color="white")
    self.user_pass.place(relx=0.50, rely=0.52, anchor="center")

  def open_signup(self):
    signup_window = tk.Toplevel(self.master)
    signup_form = SignUpForm(signup_window)

  def logIn(self):
    user_info = pd.read_csv("User Info.csv")
    userid = self.username_entry.get()
    password = self.user_pass.get()

    if (userid
        in user_info["user_id"].values) and (password
                                             in user_info["password"].values):
      #messagebox.showinfo(title="Login Successful", message="You have logged in Successfully")

      # app_2_window = Tk()  # Create a new Tkinter window
      # app_2 = MainPage(app_2_window)  # Initialize App_2 in the new window
      # app_2_window.mainloop()

      app_2_window = tk.Toplevel(self.master)
      app = MainPage(app_2_window)
      self.username_entry.delete(0, END)
      self.user_pass.delete(0, END)

    else:
      messagebox.showwarning(title='Log in failed!',
                             message="Invalid username or password")
      self.username_entry.delete(0, END)
      self.user_pass.delete(0, END)





class NavBar(Frame):

  def __init__(self, master):
    super().__init__(master, height=50)
    self.default_font = font.Font(family="Times New Roman", size=25)
    self.set_default_font()
    self.pack_propagate(0)

    self.logo_image = self.resize_image("logo.png", (100, 100))
    self.logo_label = ttk.Label(self, image=self.logo_image)
    self.logo_label.grid(row=0,
                         column=0,
                         padx=(30, 950),
                         pady=(0, 3),
                         sticky="w")

    self.signup_button = ctk.CTkButton(self,
                                       text="Sign Up",
                                       font=("Arial", 16),
                                       bg_color="white",
                                       fg_color="white"
                                       ,text_color="black",
                                       command=self.on_signup_click)
    self.signup_button.place(relx=0.86, rely=0.25)

    self.login_button = ctk.CTkButton(self,
                                      text="Log In",
                                      font=("Arial", 16),
                                      bg_color="white",
                                      fg_color="white",
                                      text_color="black",
                                      command=self.on_login_click)
    self.login_button.place(relx=0.74, rely=0.25)


    #############   -->>  ADMIN AND SHOP STUFF EKHANE TONNY  <<--   ######################

    
    self.shop_button = ctk.CTkButton(self,
                                      text="Your Shop",
                                      font=("Arial", 16),
                                      fg_color="white",text_color="black",
                                      command=self.shop_open)
    self.shop_button.place(relx=0.51, rely=0.25)
    self.Admin_button = ctk.CTkButton(self,
                                      text="Admin",
                                      font=("Arial", 16),
                                      fg_color="white",text_color="black",
                                      command=self.open_admin)
    self.Admin_button.place(relx=0.62, rely=0.25)

  
  def open_admin(self):
    s = tk.Toplevel(self.master)
    ss=Log(s)       
  def shop_open(self):
    a= tk.Toplevel(self.master)
    aa=LogS(a)


  
  def set_default_font(self):
    self.option_add("*font", self.default_font)

  def on_signup_click(self):
    signup_window = tk.Toplevel(self.master)
    signup_form = SignUpForm(signup_window)
    

  def on_login_click(self):
    login_window = tk.Toplevel(self.master)
    login_form = LogInForm(login_window)

  def resize_image(self, path, size):
    image = Image.open(path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)


class HomePage(Frame):

  def __init__(self, master):
    super().__init__(master)
    self.banner_image_label = ttk.Label(self, style="dark.TLabel")
    self.banner_image_label.pack(fill=X, pady=(5, 20))

    self.home_label = ttk.Label(
        self,
        text="Shop by Categories",
        style="dark.TLabel",
    )
    self.home_label.pack(pady=20,anchor="center")

    self.paned_window = ttk.Panedwindow(self, orient=HORIZONTAL)
    self.paned_window.pack(fill=BOTH, expand=True)

    f1 = ttk.Labelframe(self.paned_window, width=1200, height=510)
    self.image1 = self.resize_image("mainbgforcode.png", (1280, 500))
    label1 = ttk.Label(f1, image=self.image1)
    label1.pack(expand=True, fill=BOTH)
    self.paned_window.add(f1)

    self.jewel_button = Button(self,
                               text="TRADITIONAL JEWELRIES",
                               font=("Arial", 10),
                               bg="#ebeced",
                               fg="Black",
                               width=23,
                               height=2,
                               command=self.connect_category1)
    self.jewel_button.place(relx=0.14, rely=0.52)

    self.garments_button = Button(self,
                                  text="TRADITIONAL HAND\nWOVEN GARMENTS",
                                  font=("Arial", 10),
                                  bg="#ebeced",
                                  fg="Black",
                                  width=22,
                                  height=3)
    self.garments_button.place(relx=0.55, rely=0.52)

    self.wood_button = Button(self,
                              text="WOOD WORK ITEMS",
                              font=("Arial", 10),
                              bg="#ebeced",
                              fg="Black",
                            
                              width=22,
                              height=2)
    self.wood_button.place(relx=0.215, rely=0.76)

    self.bamboo_button = Button(self,
                                text="BAMBOO AND CANE\n PRODUCTS",
                                font=("Arial", 10),
                                bg="#ebeced",
                                fg="Black",
                                width=22,
                                height=3)
    self.bamboo_button.place(relx=0.63, rely=0.76)

  def connect_category1(self):
    c = tk.Toplevel(self.master)
    cc = ProductApp(c)

  def resize_image(self, path, size):
    image = Image.open(path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)


class About(Frame):

  def __init__(self, master):
    super().__init__(master)

    self.image=PhotoImage(file="aboutus.png")
    self.label = Label(self, image=self.image)
    self.label.pack()
    

class Articles(Frame):

  def __init__(self, master):
      super().__init__(master)
      label = ttk.Label(self, text="Tribal Community Updates and News", style="primary.TLabel")
      label.pack()

     
      self.text_widget = tk.Text(self, wrap='word', font=('Arial', 12), bg=self.cget("bg"), relief=tk.FLAT)
      self.text_widget.pack(expand=True, fill='both')

      # Insert article text
      article = """\n\n\t\t\tSign Up a Petition against the unfair wages of Tea Farmers in Bangladesh. Click Here to Sign Up.\n\n

    Articles:\n
    1. Northern Tea Farming Shrivelled by Unfair Prices\n
    2. Farmers Suffer Despite Success in Plain Land Tea Cultivation\n
    3. The Tribal Crafts in Bangladesh: Prospects and Predicaments\n"""

      self.text_widget.insert(tk.END, article)

     
      links = {
          "Click Here to Sign Up": "https://www.ipetitions.com/petition/petition-against-unfair-wages-for-tea-farmers-in",
          "Northern Tea Farming Shrivelled by Unfair Prices": "https://www.thedailystar.net/opinion/views/news/northern-tea-farming-shrivelled-unfair-prices-3159706",
          "Farmers Suffer Despite Success in Plain Land Tea Cultivation": "https://www.tbsnews.net/bangladesh/farmers-suffer-despite-success-plain-land-tea-cultivation-524358",
          "The Tribal Crafts in Bangladesh: Prospects and Predicaments": "https://arshadsiddiqui.wordpress.com/2016/11/17/the-tribal-crafts-in-bangladesh-prospects-and-predicaments/"
      }

      
      for link_text, url in links.items():
          start_idx = self.text_widget.search(link_text, "1.0", tk.END)
          end_idx = f"{start_idx}+{len(link_text)}c"
          tag_name = f"link_{link_text}"

          
          self.text_widget.tag_add(tag_name, start_idx, end_idx)
          self.text_widget.tag_config(tag_name, foreground="blue", underline=True)
          self.text_widget.tag_bind(tag_name, "<Button-1>", lambda e, url=url: self.open_link(url))

      


     
      self.text_widget.config(state=tk.DISABLED)

  def open_link(self, url):
      webbrowser.open_new(url)


class App(Frame):

  def __init__(self, master):
    super().__init__(master)
    self.master.title("Tribal Threads")
    self.style = Style(theme="flatly")
    self.nav_bar = NavBar(self)
    self.nav_bar.pack(side="top", fill="x")

    self.canvas = Canvas(self)
    self.scrollbar = ttk.Scrollbar(self,
                                   orient="vertical",
                                   command=self.canvas.yview)
    self.scrollable_frame = Frame(self.canvas)

    self.canvas.configure(yscrollcommand=self.scrollbar.set)

    self.content_area = ttk.Notebook(self.scrollable_frame)
    self.home_page = HomePage(self.content_area)
    self.content_area.add(self.home_page, text="Home", padding=10)

    self.about = About(self.content_area)
    self.content_area.add(self.about, text="About", padding=10)

    self.about = Articles(self.content_area)
    self.content_area.add(self.about, text="Articles", padding=10)

    self.content_area.pack(expand=True, fill="both")

    self.banner_image = self.resize_image("banner.png", (1320, 200))
    self.home_page.banner_image_label.configure(image=self.banner_image)

    self.style.configure("Custom.TLabelframe.Label",
                         font=("Times New Roman", 14))
    for child in self.home_page.winfo_children():
      if isinstance(child, ttk.Panedwindow):
        for labelframe in child.winfo_children():
          labelframe.configure(style="Custom.TLabelframe")

    self.canvas.create_window((0, 0),
                              window=self.scrollable_frame,
                              anchor="nw")
    self.canvas.pack(side="left", fill="both", expand=True)
    self.scrollbar.pack(side="right", fill="y")

    self.scrollable_frame.bind(
        "<Configure>",
        lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

  def resize_image(self, path, size):
    image = Image.open(path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)



if __name__ == "__main__":
  root = Tk()
  app = App(root)
  app.pack(side="top", fill="both", expand=True)
  # root.title("Tribal Threads")
  root.geometry("1280x720")
  app.mainloop()
#
