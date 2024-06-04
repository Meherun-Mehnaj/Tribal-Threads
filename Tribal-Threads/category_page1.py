import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from ttkbootstrap import Style
import customtkinter as ctk
from cart_updated import EcommerceCart
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import messagebox

class Product:
    def __init__(self, name, price, image_path, description):
        self.name = name
        self.price = price
        self.image_path = image_path
        self.description = description

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product_name, product_price, quantity):
        for item in self.products:
            if item["name"] == product_name:
                item["quantity"] += quantity
                return
        self.products.append({"name": product_name, "price": product_price, "quantity": quantity})

class ProductWindow(tk.Toplevel):
    def __init__(self, master, product_info, cart, ecommerce_cart):
        super().__init__(master)
        self.title("Product Description")
        self.geometry("1280x720")
        
        self.configure(bg="white")        
        self.product_info = product_info
        self.cart = cart
        self.ecommerce_cart = ecommerce_cart

        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        back_button = ctk.CTkButton(self, text="Go back",fg_color="black",text_color="white",font=("Arial", 16), command=self.go_to_home)
        back_button.grid(row=0, column=0, padx=70, pady=30, sticky="nw")

        view_cart_button = ctk.CTkButton(self, text="View Cart", fg_color="black",text_color="white",font=("Arial", 16), command=self.open_cart)
        view_cart_button.grid(row=0, column=1, padx=70, pady=30, sticky="ne")
      
        product_picture = Image.open(self.product_info["image_path"])
        product_picture = product_picture.resize((400, 400), Image.LANCZOS)
        product_picture = ImageTk.PhotoImage(product_picture)
        picture_label = tk.Label(self, image=product_picture, bg="white")
        picture_label.image = product_picture
        picture_label.grid(row=1, column=0, rowspan=5, padx=70, pady=30, sticky="w")

        name_label = ctk.CTkLabel(self, text=self.product_info["name"], font=("Arial", 25, "bold"))
        name_label.grid(row=1, column=1, pady=(10, 5), sticky="w")

        price_label = ctk.CTkLabel(self, text=f"Price: {self.product_info['price']}Tk", font=("Arial", 18))
        price_label.grid(row=2, column=1, pady=5, sticky="w")

        description_label = ctk.CTkLabel(self, text=self.product_info["description"], font=("Arial", 14), wraplength=500, justify="left")
        description_label.grid(row=3, column=1, pady=10, sticky="w")

        quantity_frame = tk.Frame(self, bg="white")
        quantity_frame.grid(row=4, column=1, pady=5, sticky="w")

        quantity_label = ctk.CTkLabel(quantity_frame, text="Quantity:", font=("Arial", 16))
        quantity_label.pack(side="left")

        self.quantity_value = tk.IntVar()
        self.quantity_value.set(1)
        self.quantity_entry = ctk.CTkEntry(quantity_frame, textvariable=self.quantity_value, font=("Arial", 14))
        self.quantity_entry.pack(side="left", padx=5)

        quantity_decrease_button = ctk.CTkButton(quantity_frame, fg_color="black",text_color="white",text="-", font=("Arial", 14), width=3, command=self.decrease_quantity)
        quantity_decrease_button.pack(side="left")

        quantity_increase_button = ctk.CTkButton(quantity_frame, fg_color="black",text_color="white",text="+", font=("Arial", 14), width=3, command=self.increase_quantity)
        quantity_increase_button.pack(side="left")

        add_to_cart_button = ctk.CTkButton(self, text="Add to Cart", fg_color="black",text_color="white",font=("Arial", 16), command=self.add_to_cart)
        add_to_cart_button.grid(row=5, column=1, pady=10, sticky="w")
      
        meet_button = ctk.CTkButton(self, text="Meet the Artisan", fg_color="BROWN",text_color="white",font=("Arial", 20), command=self.open_artisan_info)
        meet_button.grid(row=7, column=1, pady=10, sticky="w")

     

  
    def open_artisan_info(self):
        artisan_info = {
            "name": "Jorina Kharshiing",
            "email": "Craftsman/Artisan",
            "phone": "123-456-7890",
            "address": "Jaflong, Sylhet, Bangladesh"
        }
  
        artisan_window = tk.Toplevel(self)
        artisan_window.title("Meet the Artisan")
        artisan_window.geometry("1280x720")
        artisan_window.configure(bg="white")
  
       
        canvas = tk.Canvas(artisan_window, bg="white")
        scrollbar = ttk.Scrollbar(artisan_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
  
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
  
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
  
       
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
  
        
        def go_back():
            artisan_window.destroy()
  
       
        back_button = ctk.CTkButton(scrollable_frame, text="Back",fg_color="black",text_color="white",font=("Arial", 16),  command=go_back)
        back_button.grid(row=0, column=0, pady=10, padx=10, sticky="w")
  
        
        self.bg_image = tk.PhotoImage(file=r"banner1280.png")
        self.bg_label = tk.Label(scrollable_frame, image=self.bg_image)
        self.bg_label.grid(row=1, column=0, columnspan=2, pady=10)
  
        
        self.image = tk.PhotoImage(file=r"khasi.png")
        self.label = tk.Label(scrollable_frame, image=self.image)
        self.label.grid(row=2, column=0, rowspan=4, pady=10, padx=10)
  
       
        artisan_name_label = ctk.CTkLabel(scrollable_frame, text=artisan_info["name"], font=("Arial", 25, "bold"))
        artisan_name_label.grid(row=2, column=1, pady=10, sticky="w")
  
        artisan_email_label = ctk.CTkLabel(scrollable_frame, text=artisan_info["email"], font=("Arial", 18))
        artisan_email_label.grid(row=3, column=1, pady=5, sticky="w")
  
        artisan_phone_label = ctk.CTkLabel(scrollable_frame, text=artisan_info["phone"], font=("Arial", 18))
        artisan_phone_label.grid(row=4, column=1, pady=5, sticky="w")
  
        artisan_address_label = ctk.CTkLabel(scrollable_frame, text=artisan_info["address"], font=("Arial", 18))
        artisan_address_label.grid(row=5, column=1, pady=5, sticky="w")
  
        
        header_font = ("League Gothic", 20, "bold")
        sub_header_font = ("League Gothic", 18, "bold")
        content_font = ("League Gothic", 16)
  
      
        def add_section(row, title, text):
            header_label = ctk.CTkLabel(scrollable_frame, text=title, font=header_font)
            header_label.grid(row=row, column=0, columnspan=2, pady=(20, 10), padx=20, sticky="w")
            content_label = ctk.CTkLabel(scrollable_frame, text=text, font=content_font, wraplength=1200, justify="left")
            content_label.grid(row=row + 1, column=0, columnspan=2, pady=10, padx=20, sticky="w")
  
        row = 6
        add_section(row, "\n\n\t\t\tEmbracing Tradition with Every Thread\n\n\t\t\tMeet the Artisan\n", "")
        row += 2
        add_section(row, "About Jorina", "Nestled in the picturesque hills of Jaflong, Sylhet, Jorina Kharshiing is a master artisan from the Khasi community, a group renowned for their rich cultural heritage and exquisite craftsmanship. Jorina’s journey into the world of traditional necklace making began at a young age, inspired by her mother and grandmother, who passed down the intricate skills and designs that define Khasi jewelry.")
        row += 2
        add_section(row, "Craftsmanship", "Jorina specializes in creating stunning Khasi traditional necklaces, known for their vibrant colors and intricate beadwork. Each piece is a testament to her dedication, patience, and deep respect for her cultural heritage. The necklaces are made using locally sourced materials, including glass beads, shells, and natural fibers, meticulously assembled to create patterns that tell stories of the Khasi people.")
        row += 2
        add_section(row, "The Process", "Design Inspiration: Jorina draws inspiration from the natural beauty surrounding her village, incorporating motifs of flora and fauna native to Jaflong.\nMaterial Selection: Sustainable and locally sourced materials are chosen with care, ensuring each necklace reflects the natural environment and traditions of the Khasi community.\nHandcrafting: Every necklace is handcrafted, with Jorina dedicating hours to threading beads and creating intricate designs that are both contemporary and timeless.")
        row += 2
        add_section(row, "Cultural Significance", "For the Khasi community, jewelry is not just an adornment but a symbol of identity and tradition. Jorina's necklaces are often worn during important ceremonies and celebrations, representing the wearer's heritage and pride. By preserving these traditional techniques, Jorina plays a crucial role in keeping her culture alive and thriving.")
        row += 2
        add_section(row, "Support Jorina's Craft", "By purchasing a necklace from Jorina, you are not only acquiring a beautiful piece of jewelry but also supporting sustainable practices and helping to preserve the rich cultural heritage of the Khasi community. Each necklace tells a story, woven with love and tradition, waiting to become a part of your own story.")
        row += 2
  
        
        final_section = """
        Explore Jorina’s collection on the Tribal Threads app and bring a piece of Khasi culture into your life.
        """
        connect_section = """
        Connect with Us:
  
        Instagram: @tribalthreads
        Facebook: Tribal Threads
        Website: www.tribalthreads.com
        """
  
        add_section(row, "Explore Jorina’s Collection", final_section)
        row += 2
  
        connect_label = ctk.CTkLabel(scrollable_frame, text="Connect with Us:", font=sub_header_font)
        connect_label.grid(row=row, column=0, columnspan=2, pady=(20, 10), padx=20, sticky="w")
  
        connect_info = ctk.CTkLabel(scrollable_frame, text=connect_section, font=content_font, wraplength=1200, justify="left")
        connect_info.grid(row=row + 1, column=0, columnspan=2, pady=10, padx=20, sticky="w")
  
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
  
    # Example usage:
    # root = tk.Tk()
    # app = YourAppClass(root)
    # root.mainloop()
  
    
  

    def open_cart(self):
        EcommerceCart(self, self.cart)

    def increase_quantity(self):
        current_quantity = self.quantity_value.get()
        self.quantity_value.set(current_quantity + 1)

    def decrease_quantity(self):
        current_quantity = self.quantity_value.get()
        if current_quantity > 1:
            self.quantity_value.set(current_quantity - 1)

    def add_to_cart(self):
        quantity = self.quantity_value.get()
        self.ecommerce_cart.add_product(self.product_info["name"], self.product_info["price"], quantity)
        # messagebox.showinfo("Success", f"Added {quantity} x {self.product_info['name']} to the cart.")
        self.quantity_value.set(0)
    def go_to_home(self):
        self.destroy()

class ProductApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Product App")
        self.master.geometry("1280x720")
        self.master.configure(bg="white")

        view_cart_button = ctk.CTkButton(self.master, text="View Cart", fg_color="black",text_color="white",font=("Arial", 16), command=self.open_cart)
        view_cart_button.pack(padx=30,pady=30, anchor="ne")
        b_button = ctk.CTkButton(self.master, text="Back to home", fg_color="black",text_color="white",font=("Arial", 16), command=self.d)
        b_button.place(relx=0.05,rely=0.05)
       
        self.bannerimage = PhotoImage(file="category1.png")
        self.banner = Label(self.master, image=self.bannerimage)
        self.banner.pack()

        self.style = Style(theme="flatly")
        self.products = [
            Product("Traditional Khasi Necklace", 450, "neck.png", "Crafted with meticulous attention to detail, this necklace typically features intricately designed coins strung together in a delicate arrangement. Each coin bears traditional motifs and symbols, reflecting the rich heritage and artistic craftsmanship of the Khasi community."),
            Product("Traditional adorb attacker", 2, "Hamster.png", "Just a Cute lil' Hamster"),
        ]

        

      
        self.shopping_cart = ShoppingCart()
        self.ecommerce_cart = EcommerceCart(self.master, self.shopping_cart)  # Create a single instance

        self.create_product_widgets()
    def d(self):
        self.master.destroy()
    def create_product_widgets(self):
        frame = ttk.Frame(self.master)
        frame.pack(pady=20)

        self.image_references = []

        for product in self.products:
            product_frame = ttk.Frame(frame)
            product_frame.pack(side=tk.LEFT, padx=(20, 10), pady=10)

            image = Image.open(product.image_path)
            image = image.resize((200, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.image_references.append(photo)
            image_label = ttk.Label(product_frame, image=photo)
            image_label.image = photo
            image_label.pack(side=tk.TOP, padx=10, pady=10)

            product_label = ttk.Label(product_frame, text=product.name, font=("Arial", 15))
            product_label.pack(side=tk.TOP)
            product_price = ttk.Label(product_frame, text=f"{product.price} Tk", font=("Arial", 15))
            product_price.pack(side=tk.TOP)

            details_button = ctk.CTkButton(product_frame, text="View Details", fg_color="black",font=("Arial", 16), command=lambda p=product: self.view_details(p))
            details_button.pack(side=tk.TOP, padx=10, pady=10)

   

    def view_details(self, product):
        product_window = ProductWindow(self.master, {
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "image_path": product.image_path
        }, self.shopping_cart, self.ecommerce_cart)

    def open_cart(self):
        EcommerceCart(self.master, self.shopping_cart)

def run_product_app():
    root = tk.Tk()
    app = ProductApp(root)
    root.mainloop()

# if __name__ == "__main__":
#     run_product_app()
