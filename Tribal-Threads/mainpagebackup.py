import tkinter as tk
from PIL import Image, ImageTk
from ttkbootstrap import Style
import customtkinter as ctk
import webbrowser
# from tkinter import *
from tkinter import ttk, font, messagebox
from ttkbootstrap import Style
import pandas as pd
from ADMINpage import Log
from supplierprofile import LogS
from category_page1 import ProductApp
from cart_updated import EcommerceCart

class NavBar(tk.Frame):
    def __init__(self, master):
        super().__init__(master, height=50)
        self.default_font = font.Font(family="Times New Roman", size=25)
        self.set_default_font()
        self.pack_propagate(0)
        self.master.geometry("1280x720")
        self.logo_image = self.resize_image("logo.png", (100, 100))
        self.logo_label = ttk.Label(self, image=self.logo_image)
        self.logo_label.grid(row=0, column=0, padx=(30, 950), pady=(0, 3), sticky="w")

        # self.signup_button = ctk.CTkButton(self,
        #                                    text="Sign Up",
        #                                    font=("Arial", 16),
        #                                    bg_color="white",
        #                                    fg_color="white",
        #                                    text_color="black",
        #                                    command=self.on_signup_click)
        # self.signup_button.place(relx=0.86, rely=0.25)

        # self.login_button = ctk.CTkButton(self,
        #                                   text="Log In",
        #                                   font=("Arial", 16),
        #                                   bg_color="white",
        #                                   fg_color="white",
        #                                   text_color="black",
        #                                   command=self.on_login_click)
        # self.login_button.place(relx=0.74, rely=0.25)

        self.shop_button = ctk.CTkButton(self,
                                         text="Your Shop",
                                         font=("Arial", 16),
                                         fg_color="white",
                                         text_color="black",
                                         command=self.shop_open)
        self.shop_button.place(relx=0.86, rely=0.25)

        self.admin_button = ctk.CTkButton(self,
                                          text="Admin",
                                          font=("Arial", 16),
                                          fg_color="white",
                                          text_color="black",
                                          command=self.open_admin)
        self.admin_button.place(relx=0.74, rely=0.25)
        
    def open_admin(self):
        s = tk.Toplevel(self.master)
        ss = Log(s)  # Uncomment and modify this line according to your actual Log class

    def shop_open(self):
        a = tk.Toplevel(self.master)
        aa = LogS(a)  # Uncomment and modify this line according to your actual LogS class

    def set_default_font(self):
        self.option_add("*font", self.default_font)

    # def on_signup_click(self):
    #     signup_window = tk.Toplevel(self.master)
    #     signup_form = SignUpForm(signup_window)  # Uncomment and modify this line according to your actual SignUpForm class

    # def on_login_click(self):
    #     login_window = tk.Toplevel(self.master)
    #     login_form = LogInForm(login_window)  # Uncomment and modify this line according to your actual LogInForm class

    def resize_image(self, path, size):
        image = Image.open(path)
        image = image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(image)

    
class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.banner_image_label = ttk.Label(self, style="dark.TLabel")
        self.banner_image_label.pack(fill=tk.X, pady=(5, 20))

        self.home_label = ttk.Label(
            self,
            text="Shop by Categories",
            style="dark.TLabel",
        )
        self.home_label.pack(pady=20, anchor="center")

        self.paned_window = ttk.Panedwindow(self, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)

        f1 = ttk.Labelframe(self.paned_window, width=1200, height=510)
        self.image1 = self.resize_image("mainbgforcode.png", (1280, 500))
        label1 = ttk.Label(f1, image=self.image1)
        label1.pack(expand=True, fill=tk.BOTH)
        self.paned_window.add(f1)

        self.jewel_button = tk.Button(self,
                                      text="TRADITIONAL JEWELRIES",
                                      font=("Arial", 10),
                                      bg="#ebeced",
                                      fg="Black",
                                      width=23,
                                      height=2,
                                      command=self.connect_category1)
        self.jewel_button.place(relx=0.14, rely=0.52)

        self.garments_button = tk.Button(self,
                                         text="TRADITIONAL HAND\nWOVEN GARMENTS",
                                         font=("Arial", 10),
                                         bg="#ebeced",
                                         fg="Black",
                                         width=22,
                                         height=3)
        self.garments_button.place(relx=0.55, rely=0.52)

        self.wood_button = tk.Button(self,
                                     text="WOOD WORK ITEMS",
                                     font=("Arial", 10),
                                     bg="#ebeced",
                                     fg="Black",
                                     width=22,
                                     height=2)
        self.wood_button.place(relx=0.215, rely=0.76)

        self.bamboo_button = tk.Button(self,
                                       text="BAMBOO AND CANE\n PRODUCTS",
                                       font=("Arial", 10),
                                       bg="#ebeced",
                                       fg="Black",
                                       width=22,
                                       height=3)
        self.bamboo_button.place(relx=0.63, rely=0.76)

    def connect_category1(self):
        c = tk.Toplevel(self.master)
        cc = ProductApp(c)  # Uncomment and modify this line according to your actual ProductApp class

    def resize_image(self, path, size):
        image = Image.open(path)
        image = image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(image)


class About(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.image = ImageTk.PhotoImage(file="aboutus.png")
        self.label = tk.Label(self, image=self.image)
        self.label.pack()


class Articles(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = ttk.Label(self, text="Tribal Community Updates and News", style="primary.TLabel")
        label.pack()

        self.text_widget = tk.Text(self, wrap='word', font=('Arial', 12), bg=self.cget("bg"), relief=tk.FLAT)
        self.text_widget.pack(expand=True, fill='both')

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


class MainPage(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Tribal Threads")
        self.style = Style(theme="flatly")
        self.nav_bar = NavBar(self)
        self.nav_bar.pack(side="top", fill="x")
        self.s_out_button = ctk.CTkButton(self,
          text="Sign Out",
          font=("Arial", 16),
          fg_color="white",
          text_color="black",
          command=self.out)
        self.s_out_button.pack(side="top", anchor="ne",padx=40)
        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.content_area = ttk.Notebook(self.scrollable_frame)
        self.home_page = HomePage(self.content_area)
        self.content_area.add(self.home_page, text="Home", padding=10)

        self.about = About(self.content_area)
        self.content_area.add(self.about, text="About", padding=10)

        self.articles = Articles(self.content_area)
        self.content_area.add(self.articles, text="Articles", padding=10)

        self.content_area.pack(expand=True, fill="both")

        self.banner_image = self.resize_image("banner.png", (1320, 200))
        self.home_page.banner_image_label.configure(image=self.banner_image)

        self.style.configure("Custom.TLabelframe.Label", font=("Times New Roman", 14))
        for child in self.home_page.winfo_children():
            if isinstance(child, ttk.Panedwindow):
                for labelframe in child.winfo_children():
                    labelframe.configure(style="Custom.TLabelframe")

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        
    def out(self):
        self.destroy()

    def resize_image(self, path, size):
        image = Image.open(path)
        image = image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(image)


def run_main_app():
    root = tk.Tk()
    app = MainPage(root)
    root.state('normal')  
    root.mainloop()


if __name__ == "__main__":
    run_main_app()
