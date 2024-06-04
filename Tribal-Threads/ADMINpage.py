
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from dashboard_gui import TribalThreadsApp

import customtkinter as ctk  
data=pd.read_csv(r"ProductSales.csv")
class Log(tk.Toplevel):
    def __init__(self, master):
        self.master = master
        self.master.geometry("1280x720")
        self.master.title("Sign Up Page")

        
        self.bg_image = PhotoImage(file="loginforsupandad.png")
        self.bg_label = Label(master, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)  

       
        self.master.lift(self.bg_label)

        self.button = ctk.CTkButton(master=self.bg_label, command=self.logIn, width=200,height=40, font=("Arial", 18, "bold"), corner_radius=20, text='Log in', bg_color="#141d1a")
        self.button.place(relx=0.50, rely=0.65, anchor="center")

        self.username_entry = ctk.CTkEntry(master=self.bg_label, border_width=4, width=280, height=45, corner_radius=15, bg_color="#35392f", placeholder_text="Username", fg_color="black", border_color="white",text_color="white")
        self.username_entry.place(relx=0.50, rely=0.42, anchor="center")

        self.user_pass = ctk.CTkEntry(master=self.bg_label, border_width=4, width=280, height=45, corner_radius=15, placeholder_text="Password", show="*", bg_color="#35392f", border_color="white", fg_color="black",text_color="white")
        self.user_pass.place(relx=0.50, rely=0.52, anchor="center")

    def logIn(self):
      
        user_info = pd.DataFrame({
            "user_id": ["admin"],
            "password": ["admin"]
        })

        userid = self.username_entry.get()
        password = self.user_pass.get()

        if (userid in user_info["user_id"].values) and (password in user_info["password"].values):
            
            self.open_supplier_profile()
        else:
            tkmb.showwarning(title='Log in failed!', message="Invalid username or password")
            self.username_entry.delete(0, END)
            self.user_pass.delete(0, END)

    def open_supplier_profile(self):
       
        self.master.destroy()

        
        AdminProfile().mainloop()

class ScrollableFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.canvas = Canvas(self, borderwidth=0, highlightthickness=0)
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
              
            )
        )

        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        #add a back button
        
       


class Dashboard(ScrollableFrame):
  def __init__(self, master):
      super().__init__(master)

      self.dashbutton=ctk.CTkButton(master=self.scrollable_frame, width=280,height=20, text="Open live Dashboard", font=("Arial", 24, "bold"), corner_radius=20,fg_color="darkblue",text_color="white",command=self.ddd)
      self.dashbutton.pack()
      self.dashboardtem1pic=PhotoImage(file="Dashboard1.png")
      self.dashboardtem1=Label(self.scrollable_frame, image=self.dashboardtem1pic)
      self.dashboardtem1.pack()
      
      # 1) Pie chart showing the highest selling products
      plt.figure(figsize=(12.8, 4))
      plt.pie(data['Sales Quantity'], shadow=True,explode=[0.0,0.0,0.0,0.0,0.2,0.0,0.0,0.0] ,wedgeprops={"edgecolor": "white"} ,colors=["lightblue","pink","#FFFF99","#E6E6FA","#A5D6A7","#98FB98", "#FFDAB9","#FFCCCB"],labels=data['Product Name'], autopct='%1.1f%%', startangle=140)
      plt.title('Highest Selling Products')
      plt.axis('equal')
      plt.savefig('highest_selling_products.png')
      plt.close()


      self.highest_selling_products_img = Image.open('highest_selling_products.png')
      self.highest_selling_products_img = ImageTk.PhotoImage(self.highest_selling_products_img)
      self.highest_selling_products_label = Label(self.scrollable_frame, image=self.highest_selling_products_img)
      self.highest_selling_products_label.pack()








      # 2) Bar chart for highest selling supplier
      plt.figure(figsize=(12.8,4))
      df_supplier = pd.DataFrame(data)
      df_supplier = df_supplier.groupby('Manufacturer')['Sales Quantity'].sum().nlargest(6)
      df_supplier.plot(kind='bar', color='skyblue')
      plt.title('Highest Selling Supplier')
      plt.xlabel('Supplier')
      plt.ylabel('Sales Quantity')
      plt.xticks(rotation=45, ha='right')
      plt.tight_layout()
      plt.savefig('highest_selling_supplier.png')

      plt.close()

      self.highest_selling_supplier_img = Image.open('highest_selling_supplier.png')
      self.highest_selling_supplier_img = ImageTk.PhotoImage(self.highest_selling_supplier_img)
      self.highest_selling_supplier_label = Label(self.scrollable_frame, image=self.highest_selling_supplier_img)
      self.highest_selling_supplier_label.pack()

      # 3) Customer satisfaction chart
      plt.figure(figsize=(6.85, 5))
      plt.bar(data['Product Name'], data['Customer Satisfaction'], color='lightgreen')
      plt.title('Customer Satisfaction')
      plt.xlabel('Product')
      plt.ylabel('Satisfaction (out of 10)')
      plt.xticks(rotation=45, ha='right')
      plt.tight_layout()
      plt.savefig('customer_satisfaction.png')
      plt.close()

      self.customer_satisfaction_img = Image.open('customer_satisfaction.png')
      self.customer_satisfaction_img = ImageTk.PhotoImage(self.customer_satisfaction_img)
      self.customer_satisfaction_label = Label(self.scrollable_frame, image=self.customer_satisfaction_img)
      self.customer_satisfaction_label.pack(side="right")

      # 4) Total customer
      total_customers = 8

      # 5) Sell percentage upgrade rate before vs after chart
      geographical_performance_before = [10, 34, 5, 7, 60, 20, 33, 54]  # Example data
      geographical_performance_after = [70, 75, 80, 65, 85, 75, 70, 75]  # Example data
      products = data['Product Name']

      plt.figure(figsize=(6, 5))
      plt.plot(products, geographical_performance_before, marker='o', label='Before')
      plt.plot(products, geographical_performance_after, marker='o', label='After')
      plt.title('Geographical Performance Before vs After')
      plt.xlabel('Product')
      plt.ylabel('Performance (%)')
      plt.xticks(rotation=45, ha='right')
      plt.legend()
      plt.grid(True)
      plt.tight_layout()
      plt.savefig('geographical_performance.png')
      plt.close()

      self.geographical_performance_img = Image.open('geographical_performance.png')
      self.geographical_performance_img = ImageTk.PhotoImage(self.geographical_performance_img)
      self.geographical_performance_label = Label(self.scrollable_frame, image=self.geographical_performance_img)
      self.geographical_performance_label.pack(side="left")

  def ddd(self):
      a=tk.Toplevel(self.master)
      b=TribalThreadsApp(a)
    
    
      
class AdminProfile(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("1280x1000")
        self.title("Admin Profile")


        self.back=ctk.CTkButton(self,text="Back",fg_color="black",text_color="white",font=("Arial", 16),command=self.back_to_main)
       
        self.back.pack(side="top", anchor="nw")
        self.s_out=ctk.CTkButton(self,text="Sign Out",fg_color="black",text_color="white",font=("Arial", 16),command=self.back_to_main)
        
        self.s_out.pack(side="top", anchor="ne")

        self.banner_frame = Frame(self)
        self.banner_frame.pack(fill="x")  

       
        self.banner_image = PhotoImage(file="banner1280.png")
        self.banner_label = Label(self.banner_frame, image=self.banner_image)
        self.banner_label.pack()

        
        content_area = ttk.Notebook(self)
        content_area.pack(expand=True, fill="both")

        
        dashboard = Dashboard(content_area)
        content_area.add(dashboard, text="Analytics Dashboard", padding=10)


    def back_to_main(self):
            self.destroy()

# Create and run the application
# root = Tk()
# app = Log(root)
# root.mainloop()
