from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import tkinter as tk

class EcommerceCart(tk.Toplevel):
    def __init__(self, master, shopping_cart):
        super().__init__(master)
        self.title("E-commerce Cart")
        self.configure(bg="white")

        self.geometry("1280x720")
        self.shopping_cart = shopping_cart
        #make bg white

        self.create_widgets()

    def create_widgets(self):
        self.cart_frame = ctk.CTkFrame(self,height=500,width=500,fg_color="lightblue")
        self.cart_frame.pack(fill=Y,padx=80,pady=30,side="right")

        back_button = ctk.CTkButton(self, text="Back to Home",fg_color="black",text_color="white",font=("Arial", 16), command=self.go_to_home)
        back_button.pack(padx=70, pady=30, anchor="nw")

        self.update_cart()

        checkout_button = ctk.CTkButton(self,text="Checkout",fg_color="black",text_color="white", command=self.checkout)
        checkout_button.place(relx=0.728,rely=0.89)

        self.label_bill=ctk.CTkLabel(self,text="Billing Information",font=("Arial",27,"bold"),fg_color="white",text_color="black")
        self.label_bill.place(relx=0.15,rely=0.2)
        self.fname=ctk.CTkEntry(self,placeholder_text="First Name",width=180,fg_color="white",text_color="black")  
        self.fname.place(relx=0.12,rely=0.3)  
        self.lname=ctk.CTkEntry(self,placeholder_text="Last Name",width=180,fg_color="white",text_color="black")  
        self.lname.place(relx=0.28,rely=0.3)  
        self.address=ctk.CTkEntry(self,placeholder_text="Delivery Address",width=385,height=50,fg_color="white",text_color="black")  
        self.address.place(relx=0.12,rely=0.4)  
        self.cell=ctk.CTkEntry(self,placeholder_text="Phone Number",width=180,fg_color="white",text_color="black")
        self.cell.place(relx=0.12,rely=0.5)
       #combobox for payment method
        label=ctk.CTkLabel(self,text="Payment Method:",font=("Arial",16,"bold"),fg_color="white",text_color="black")
        label.place(relx=0.12,rely=0.56)

        payment_method=ctk.CTkComboBox(self,values=["Cash on Delivery","Visa","Bkash"],width=200,fg_color="white",text_color="black")
        payment_method.place(relx=0.12,rely=0.6)
        
    def go_to_home(self):
        self.destroy()
    def update_cart(self):
        for widget in self.cart_frame.winfo_children():
            widget.destroy()

        for idx, product in enumerate(self.shopping_cart.products):
            product_frame = ctk.CTkFrame(self.cart_frame,fg_color="white")
            product_frame.pack(fill=X,padx=10, pady=5)

            product_label = ctk.CTkLabel(product_frame,fg_color="white",text_color="black", text=f"{product['name']} - {product['quantity']} x {product['price']}Tk")
            product_label.pack(side=LEFT, padx=10, pady=10)

            remove_button = ctk.CTkButton(product_frame, text="Remove",fg_color="black",text_color="white", command=lambda p=product: self.remove_product(p))
            remove_button.pack(side=RIGHT, padx=10, pady=10)

    def remove_product(self, product):
        self.shopping_cart.products.remove(product)
        self.update_cart()

    def checkout(self):
        if not self.shopping_cart.products:
            messagebox.showinfo("Checkout", "Your cart is empty!")
            return

          
        total_price = sum(item['price'] * item['quantity'] for item in self.shopping_cart.products)
        messagebox.showinfo("Checkout", f"Checkout successful! Total Price: {total_price}Tk")
        self.shopping_cart.products.clear()
        self.update_cart()
        self.fname.delete(0,END)
        self.lname.delete(0,END)
        self.address.delete(0,END)
        self.cell.delete(0,END)

        
        

    def add_product(self, name, price, quantity):
        self.shopping_cart.add_product(name, price, quantity)
        self.update_cart()
