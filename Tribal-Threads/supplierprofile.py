from tkinter import *
import tkinter as tk
from tkinter import ttk
import pandas as pd
import tkinter.messagebox as tkmb
from tkinter import messagebox

import customtkinter as ctk  

class LogS(tk.Toplevel):
    def __init__(self, master):
        self.master = master
        self.master.geometry("1280x720")
        self.master.title("Sign Up Page")

        
        self.bg_image = PhotoImage(file="loginforsupandad.png")
        self.bg_label = Label(master, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)  

        
        self.master.lift(self.bg_label)

        self.button = ctk.CTkButton(master=self.bg_label,command=self.logIn, width=200,height=40, font=("Arial", 18, "bold"),corner_radius=20,text='Log in',bg_color="#141d1a")
        self.button.place(relx=0.50, rely=0.65, anchor="center")

        self.username_entry = ctk.CTkEntry(master=self.bg_label, border_width=4, width=280, height=45, corner_radius=15, bg_color="#35392f", placeholder_text="Username", fg_color="black", border_color="white",text_color="white")
        self.username_entry.place(relx=0.50, rely=0.42, anchor="center")

        self.user_pass = ctk.CTkEntry(master=self.bg_label, border_width=4, width=280, height=45, corner_radius=15, placeholder_text="Password", show="*", bg_color="#35392f", border_color="white", fg_color="black",text_color="white")
        self.user_pass.place(relx=0.50, rely=0.52, anchor="center")

    def logIn(self):
        
        user_info = pd.DataFrame({
            "user_id": ["shop"],
            "password": ["shop"]
        })

        userid = self.username_entry.get()
        password = self.user_pass.get()

        if (userid in user_info["user_id"].values) and (password in user_info["password"].values):
            # Open the SupplierProfile page on successful login
            self.open_supplier_profile()
        else:
            tkmb.showwarning(title='Log in failed!', message="Invalid username or password")
            self.username_entry.delete(0, END)
            self.user_pass.delete(0, END)

    def open_supplier_profile(self):
        
        self.master.destroy()

       
        SupplierProfile().mainloop()
class Products(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        #Banner
        self.bannerimage = PhotoImage(file="banner1280.png")
        self.banner = Label(self, image=self.bannerimage)
        self.banner.place(relx=0.0, rely=0.10)

      
        
  
        
        self.addproduct = ctk.CTkButton(
            self, text="Add Product", font=("Arial", 18, "bold"), fg_color="black", corner_radius=10,
            command=self.add_product_window
        )
        self.addproduct.place(relx=0.5, rely=0.45, anchor="center")  

        self.image=PhotoImage(file="necksup.png")
        self.image_label=Label(self, image=self.image)
        self.image_label.place(relx=0.05,rely=0.53)

        self.edit_button=ctk.CTkButton(self,text="Edit Product", width=200, font=("Ariel",25,"bold"),fg_color="black")
        self.edit_button.place(relx=0.05,rely=0.8)

    

    

    def add_product_window(self):
        AddProductWindow()

class Orders(Frame):
    def __init__(self, master):
        super().__init__(master)
      
        label = Label(self, text="Orders")
        label.pack(expand=True, fill="x")
        self.display_orders()  # Show list of orders

    def display_orders(self):
       
        orders = [
            {"order_id": 1, "customer_name": "Miti", "product": "Chakma Taditional Bangles", "quantity": 2, "status": "Pending"},
            {"order_id": 2, "customer_name": "Tonny", "product": "Khasi Traditional Necklace", "quantity": 1, "status": "Shipped"},
            {"order_id": 3, "customer_name": "Mehnoor", "product": "Monipuri Saree", "quantity": 3, "status": "Delivered"},
            {"order_id": 4, "customer_name": "Moana", "product": "Khasi Traditional Necklace, Hamster", "quantity": 10, "status": "Pending"},
        ]

        
        tree = ttk.Treeview(self)
        tree["columns"] = ("order_id", "customer_name", "product", "quantity", "status")
        tree.heading("#0", text="", anchor="w")
        tree.column("#0", width=0, stretch=NO)
        tree.heading("order_id", text="Order ID")
        tree.column("order_id", anchor="center", width=100)
        tree.heading("customer_name", text="Customer Name")
        tree.column("customer_name", anchor="center", width=150)
        tree.heading("product", text="Product")
        tree.column("product", anchor="center", width=150)
        tree.heading("quantity", text="Quantity")
        tree.column("quantity", anchor="center", width=100)
        tree.heading("status", text="Status")
        tree.column("status", anchor="center", width=100)

        
        for order in orders:
            tree.insert("", "end", text="", values=(
                order["order_id"],
                order["customer_name"],
                order["product"],
                order["quantity"],
                order["status"]
            ))

        
        tree.pack(expand=True, fill="both")

class Deliveries(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = Label(self, text="Deliveries")
        label.pack(expand=True, fill="x")
        self.selected_delivery_id = None
        self.create_dropdown_menu()
        self.display_deliveries()  

    def create_dropdown_menu(self):
       
        statuses = ["Pending", "Shipped", "Delivered"]

       
        self.selected_status = StringVar(self)
        self.selected_status.set(statuses[0])  

        
        self.status_dropdown = OptionMenu(self, self.selected_status, *statuses)
        self.status_dropdown.pack(side="top", pady=10)

        
        self.change_status_button = Button(self, text="Change Status", command=self.change_status)
        self.change_status_button.pack(side="top", pady=5)

    def change_status(self):
        
        if self.selected_delivery_id:
            new_status = self.selected_status.get()
            print(f"Change status of delivery ID {self.selected_delivery_id} to {new_status}")

           
            for item in self.tree.get_children():
                values = self.tree.item(item, "values")
                if values[0] == self.selected_delivery_id:
                    
                    self.tree.item(item, values=(values[0], values[1], values[2], new_status))
                    break

    def update_selected_delivery(self, event):
        selected_item = event.widget.selection()[0]
        self.selected_delivery_id = event.widget.item(selected_item)["values"][0]

    def display_deliveries(self):
        # Example data (will replace with actual delivery data)
        deliveries = [
            {"delivery_id": 1, "recipient": "Miti", "address": "Kalyanpur-dhaka", "status": "Pending"},
            {"delivery_id": 2, "recipient": "Tonny", "address": "nodda-Ctg", "status": "Shipped"},
            {"delivery_id": 3, "recipient": "Mehnoor", "address": "123-Barishal", "status": "Delivered"},
            {"delivery_id": 4, "recipient": "Moana", "address": "123 Dhaka", "status": "Pending"},
        ]

        
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("delivery_id", "recipient", "address", "status")
        self.tree.heading("#0", text="", anchor="w")
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.heading("delivery_id", text="Delivery ID")
        self.tree.column("delivery_id", anchor="center", width=100)
        self.tree.heading("recipient", text="Recipient")
        self.tree.column("recipient", anchor="center", width=150)
        self.tree.heading("address", text="Address")
        self.tree.column("address", anchor="center", width=300)
        self.tree.heading("status", text="Status")
        self.tree.column("status", anchor="center", width=100)

       
        for delivery in deliveries:
            self.tree.insert("", "end", text="", values=(
                delivery["delivery_id"],
                delivery["recipient"],
                delivery["address"],
                delivery["status"]
            ))

       
        self.tree.bind("<<TreeviewSelect>>", self.update_selected_delivery)

       
        self.tree.pack(expand=True, fill="both")

class SupplierProfile(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("Supplier Profile")

       
        self.content_area = ttk.Notebook(self)
        self.content_area.pack(expand=True, fill="both")  

        
        self.products_page = Products(self.content_area)
        self.content_area.add(self.products_page, text="Products", padding=10)

        
        self.orders_page = Orders(self.content_area)
        self.content_area.add(self.orders_page, text="Orders", padding=10)

        
        self.deliveries_page = Deliveries(self.content_area)
        self.content_area.add(self.deliveries_page, text="Deliveries", padding=10)

        
        self.content_area.bind("<Configure>", self.adjust_content_size)

        
        self.signout = ctk.CTkButton(self, text="Sign Out", font=("Arial", 18, "bold"), fg_color="black", corner_radius=10,command=self.sign_out)
        self.signout.place(relx=0.86, rely=0.03)
      
    def sign_out(self):
      self.destroy()

    def adjust_content_size(self, event):
        
        width = event.width
        height = event.height
        self.content_area.config(width=width, height=height)

class AddProductWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Add Product")
        self.geometry("500x550")

        
        self.name_label = Label(self, text="Product Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = Entry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.price_label = Label(self, text="Price:")
        self.price_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.price_entry = Entry(self)
        self.price_entry.grid(row=1, column=1, padx=10, pady=10)

        self.quantity_label = Label(self, text="Quantity:")
        self.quantity_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.quantity_entry = Entry(self)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=10)

        self.category_label = Label(self, text="Category:")
        self.category_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.category_entry = Entry(self)
        self.category_entry.grid(row=3, column=1, padx=10, pady=10)

        self.description_label = Label(self, text="Description:")
        self.description_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.description_entry = Text(self, height=5, width=30)
        self.description_entry.grid(row=4, column=1, padx=10, pady=10)

        
        self.picture_label = Label(self, text="Product Picture Path:")
        self.picture_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.picture_entry = Entry(self)
        self.picture_entry.grid(row=5, column=1, padx=10, pady=10)

       
        self.save_button = Button(self, text="Upload", command=self.save_product)
        self.save_button.grid(row=6, column=0, columnspan=2, pady=10)

    def save_product(self):
        
        product_name = self.name_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get("1.0", "end-1c")
        picture_path = self.picture_entry.get()

        # save to database
        
        print("Product Name:", product_name)
        print("Price:", price)
        print("Quantity:", quantity)
        print("Category:", category)
        print("Description:", description)
        print("Product Picture Path:", picture_path)

       
        self.destroy()
        
# # Create and run the application
# root=Tk()
# app = LogS(root)
# root.mainloop()
