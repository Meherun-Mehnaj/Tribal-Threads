# from pathlib import Path
# import tkinter as tk
# # from tkinter import *
# # Explicit imports to satisfy Flake8
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import pandas as pd
# from data import *


# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


# def relative_to_assets(path: str) -> Path:
#     return ASSETS_PATH / Path(path)


# window = Tk()

# window.geometry("1280x720")
# window.configure(bg = "#2A2F4F")


# canvas = Canvas(
#     window,
#     bg = "#2A2F4F",
#     height = 720,
#     width = 1280,
#     bd = 0,
#     highlightthickness = 0,
#     relief = "ridge"
# )

# canvas.place(x = 0, y = 0)
# canvas.create_rectangle(
#     0.0,
#     0.0,
#     1280.0,
#     72.0,
#     fill="#E5BEEC",
#     outline="")

# canvas.create_text(
#     83.0,
#     16.0,
#     anchor="nw",
#     text="Tribal Threads",
#     fill="#000000",
#     font=("Inter Bold", 30 * -1)
# )

# image_image_1 = PhotoImage(
#     file=relative_to_assets("image_1.png"))
# image_1 = canvas.create_image(
#     170.0,
#     143.0,
#     image=image_image_1
# )

# image_image_2 = PhotoImage(
#     file=relative_to_assets("image_2.png"))
# image_2 = canvas.create_image(
#     170.0,
#     364.0,
#     image=image_image_2
# )

# image_image_3 = PhotoImage(
#     file=relative_to_assets("image_3.png"))
# image_3 = canvas.create_image(
#     830.0,
#     364.0,
#     image=image_image_3
# )

# image_image_4 = PhotoImage(
#     file=relative_to_assets("image_4.png"))
# image_4 = canvas.create_image(
#     498.0,
#     364.0,
#     image=image_image_4
# )

# image_image_5 = PhotoImage(
#     file=relative_to_assets("image_5.png"))
# image_5 = canvas.create_image(
#     498.0,
#     143.0,
#     image=image_image_5
# )

# image_image_6 = PhotoImage(
#     file=relative_to_assets("image_6.png"))
# image_6 = canvas.create_image(
#     830.0,
#     142.0,
#     image=image_image_6
# )

# canvas.create_text(
#     68.0,
#     117.0,
#     anchor="nw",
#     text="Revenue",
#     fill="#FFFFFF",
#     font=("Inter Bold", 10 * -1)
# )

# canvas.create_text(
#     396.0,
#     117.0,
#     anchor="nw",
#     text="Customers",
#     fill="#FFFFFF",
#     font=("Inter Bold", 10 * -1)
# )

# canvas.create_text(
#     728.0,
#     116.0,
#     anchor="nw",
#     text="Products Sold",
#     fill="#FFFFFF",
#     font=("Inter Bold", 10 * -1)
# )

# canvas.create_text(
#     54.0,
#     136.0,
#     anchor="nw",
#     text="4938",
#     fill="#FFFFFF",
#     font=("Inter Bold", 22 * -1)
# )

# canvas.create_text(
#     382.0,
#     136.0,
#     anchor="nw",
#     text="19",
#     fill="#FFFFFF",
#     font=("Inter Bold", 22 * -1)
# )

# canvas.create_text(
#     714.0,
#     135.0,
#     anchor="nw",
#     text="20",
#     fill="#FFFFFF",
#     font=("Inter Bold", 22 * -1)
# )

# # image_image_7 = PhotoImage(
# #     file=relative_to_assets("image_7.png"))
# # image_7 = canvas.create_image(
# #     59.0,
# #     123.0,
# #     image=image_image_7
# # )

# canvas.create_text(
#     237.0,
#     126.0,
#     anchor="nw",
#     text="5.8%",
#     fill="#D9FFCA",
#     font=("Inter Bold", 20 * -1)
# )

# canvas.create_text(
#     565.0,
#     126.0,
#     anchor="nw",
#     text="9.4%",
#     fill="#D9FFCA",
#     font=("Inter Bold", 20 * -1)
# )

# canvas.create_text(
#     897.0,
#     125.0,
#     anchor="nw",
#     text="3.6%",
#     fill="#D9FFCA",
#     font=("Inter Bold", 20 * -1)
# )

# canvas.create_text(
#     237.0,
#     151.0,
#     anchor="nw",
#     text="Past Week",
#     fill="#FFFFFF",
#     font=("Inter Bold", 7 * -1)
# )

# canvas.create_text(
#     565.0,
#     151.0,
#     anchor="nw",
#     text="Past Week",
#     fill="#FFFFFF",
#     font=("Inter Bold", 7 * -1)
# )

# canvas.create_text(
#     897.0,
#     150.0,
#     anchor="nw",
#     text="Past Week",
#     fill="#FFFFFF",
#     font=("Inter Bold", 7 * -1)
# )

# image_image_8 = PhotoImage(
#     file=relative_to_assets("image_8.png"))
# image_8 = canvas.create_image(
#     219.0,
#     136.0,
#     image=image_image_8
# )

# # image_image_9 = PhotoImage(
# #     file=relative_to_assets("image_9.png"))
# # image_9 = canvas.create_image(
# #     547.0,
# #     136.0,
# #     image=image_image_9
# # )

# image_image_10 = PhotoImage(
#     file=relative_to_assets("image_10.png"))
# image_10 = canvas.create_image(
#     879.0,
#     135.0,
#     image=image_image_10
# )

# image_image_11 = PhotoImage(
#     file=relative_to_assets("image_11.png"))
# image_11 = canvas.create_image(
#     718.0,
#     122.0,
#     image=image_image_11
# )

# # image_image_12 = PhotoImage(
# #     file=relative_to_assets("image_12.png"))
# # image_12 = canvas.create_image(
# #     56.0,
# #     31.0,
# #     image=image_image_12
# # )

# image_image_13 = PhotoImage(
#     file=relative_to_assets("image_13.png"))
# image_13 = canvas.create_image(
#     386.0,
#     123.0,
#     image=image_image_13
# )

# # Creating Area Chart

# revenue_data = pd.DataFrame(revenue)
# revenue_data["date"] = pd.to_datetime(revenue_data["date"])

# fig_1 = Figure(figsize=(2.5, 2.2), facecolor="#917FB3")
# ax_1 = fig_1.add_subplot()
# ax_1.set_facecolor("#917FB3")
# ax_1.fill_between(x=revenue_data["date"], y1=revenue_data["amount"], alpha=0.7)
# ax_1.tick_params(labelsize=7, colors="white")
# fig_1.autofmt_xdate()
# ax_1.plot(revenue_data["date"], revenue_data["amount"], color="deepskyblue")
# ax_1.grid(visible=True)

# canvas = FigureCanvasTkAgg(figure=fig_1, master=window)
# canvas.draw()
# canvas.get_tk_widget().place(x=40, y=220)

# # Creating Circular Bar Chart
# fig_2 = Figure(figsize=(2.5, 2.2), facecolor="#917FB3")
# ax_2 = fig_2.add_subplot(projection="polar")
# ax_2.set_facecolor("#917FB3")
# ax_2.bar(x=sales["angles"], height=sales["revenue"], color=sales["colors"])
# ax_2.set_frame_on(False)
# ax_2.set_xticks([])
# ax_2.tick_params(labelsize=2, colors="white")
# ax_2.grid(alpha=0.7)

# for angle, label, rotation in zip(sales["angles"], sales["products"], sales["rotation"]):
#     ax_2.text(x=angle, y=max(sales["revenue"]) + 30, s=label, rotation=rotation, ha="center", va="center", color="white", fontsize=8)

# canvas = FigureCanvasTkAgg(figure=fig_2, master=window)
# canvas.draw()
# canvas.get_tk_widget().place(x=700, y=220)

# # Creating Table

# table = ttk.Treeview(master=window, columns=table_columns, show="headings")

# for column in table_columns:
#     table.heading(column=column, text=column)
#     table.column(column=column, width=70)

# for row_data in table_data:
#     table.insert(parent="", index="end", values=row_data)

# style = ttk.Style()
# style.theme_use("default")
# style.configure("Treeview", background="#917FB3", fieldbackground="#917FB3", foreground="white")
# style.configure("Treeview.Heading", background="#917FB3", fieldbackground="#917FB3", foreground="white")
# style.map("Treeview", background=[("selected", "#E5BEEC")])

# table.place(x=395, y=225, height=260)

# window.resizable(True, True)
# window.mainloop()



from pathlib import Path
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from data import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class TribalThreadsApp(tk.Toplevel):
    def __init__(self, master):
        self.master = master
        self.master.geometry("1280x720")
        self.master.configure(bg="#2A2F4F")

        self.setup_ui()

    def setup_ui(self):
        
        canvas = tk.Canvas(
            self.master,
            bg="#2A2F4F",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            0.0,
            0.0,
            1280.0,
            72.0,
            fill="#E5BEEC",
            outline=""
        )

        canvas.create_text(
            83.0,
            16.0,
            anchor="nw",
            text="Tribal Threads",
            fill="#000000",
            font=("Inter Bold", 30 * -1)
        )

        image_image_1 = tk.PhotoImage(
            file=relative_to_assets("image_1.png"))
        canvas.create_image(
            170.0,
            143.0,
            image=image_image_1
        )

        image_image_2 = tk.PhotoImage(
            file=relative_to_assets("image_2.png"))
        canvas.create_image(
            170.0,
            364.0,
            image=image_image_2
        )

        image_image_3 = tk.PhotoImage(
            file=relative_to_assets("image_3.png"))
        canvas.create_image(
            830.0,
            364.0,
            image=image_image_3
        )

        image_image_4 = tk.PhotoImage(
            file=relative_to_assets("image_4.png"))
        canvas.create_image(
            498.0,
            364.0,
            image=image_image_4
        )

        image_image_5 = tk.PhotoImage(
            file=relative_to_assets("image_5.png"))
        canvas.create_image(
            498.0,
            143.0,
            image=image_image_5
        )

        image_image_6 = tk.PhotoImage(
            file=relative_to_assets("image_6.png"))
        canvas.create_image(
            830.0,
            142.0,
            image=image_image_6
        )

        canvas.create_text(
            68.0,
            117.0,
            anchor="nw",
            text="Revenue",
            fill="#FFFFFF",
            font=("Inter Bold", 10 * -1)
        )

        canvas.create_text(
            396.0,
            117.0,
            anchor="nw",
            text="Customers",
            fill="#FFFFFF",
            font=("Inter Bold", 10 * -1)
        )

        canvas.create_text(
            728.0,
            116.0,
            anchor="nw",
            text="Products Sold",
            fill="#FFFFFF",
            font=("Inter Bold", 10 * -1)
        )

        canvas.create_text(
            54.0,
            136.0,
            anchor="nw",
            text="4938",
            fill="#FFFFFF",
            font=("Inter Bold", 22 * -1)
        )

        canvas.create_text(
            382.0,
            136.0,
            anchor="nw",
            text="19",
            fill="#FFFFFF",
            font=("Inter Bold", 22 * -1)
        )

        canvas.create_text(
            714.0,
            135.0,
            anchor="nw",
            text="20",
            fill="#FFFFFF",
            font=("Inter Bold", 22 * -1)
        )

        canvas.create_text(
            237.0,
            126.0,
            anchor="nw",
            text="5.8%",
            fill="#D9FFCA",
            font=("Inter Bold", 20 * -1)
        )

        canvas.create_text(
            565.0,
            126.0,
            anchor="nw",
            text="9.4%",
            fill="#D9FFCA",
            font=("Inter Bold", 20 * -1)
        )

        canvas.create_text(
            897.0,
            125.0,
            anchor="nw",
            text="3.6%",
            fill="#D9FFCA",
            font=("Inter Bold", 20 * -1)
        )

        canvas.create_text(
            237.0,
            151.0,
            anchor="nw",
            text="Past Week",
            fill="#FFFFFF",
            font=("Inter Bold", 7 * -1)
        )

        canvas.create_text(
            565.0,
            151.0,
            anchor="nw",
            text="Past Week",
            fill="#FFFFFF",
            font=("Inter Bold", 7 * -1)
        )

        canvas.create_text(
            897.0,
            150.0,
            anchor="nw",
            text="Past Week",
            fill="#FFFFFF",
            font=("Inter Bold", 7 * -1)
        )

        image_image_8 = tk.PhotoImage(
            file=relative_to_assets("image_8.png"))
        canvas.create_image(
            219.0,
            136.0,
            image=image_image_8
        )

        image_image_10 = tk.PhotoImage(
            file=relative_to_assets("image_10.png"))
        canvas.create_image(
            879.0,
            135.0,
            image=image_image_10
        )

        image_image_11 = tk.PhotoImage(
            file=relative_to_assets("image_11.png"))
        canvas.create_image(
            718.0,
            122.0,
            image=image_image_11
        )

        image_image_13 = tk.PhotoImage(
            file=relative_to_assets("image_13.png"))
        canvas.create_image(
            386.0,
            123.0,
            image=image_image_13
        )

        self.create_area_chart()
        self.create_circular_bar_chart()
        self.create_table()
      
        

    
    def create_area_chart(self):
        revenue_data = pd.DataFrame(revenue)
        revenue_data["date"] = pd.to_datetime(revenue_data["date"])

        fig_1 = Figure(figsize=(2.5, 2.2), facecolor="#917FB3")
        ax_1 = fig_1.add_subplot()
        ax_1.set_facecolor("#917FB3")
        ax_1.fill_between(x=revenue_data["date"], y1=revenue_data["amount"], alpha=0.7)
        ax_1.tick_params(labelsize=7, colors="white")
        fig_1.autofmt_xdate()
        ax_1.plot(revenue_data["date"], revenue_data["amount"], color="deepskyblue")
        ax_1.grid(visible=True)

        canvas = FigureCanvasTkAgg(figure=fig_1, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().place(x=40, y=220)

    def create_circular_bar_chart(self):
        fig_2 = Figure(figsize=(2.5, 2.2), facecolor="#917FB3")
        ax_2 = fig_2.add_subplot(projection="polar")
        ax_2.set_facecolor("#917FB3")
        ax_2.bar(x=sales["angles"], height=sales["revenue"], color=sales["colors"])
        ax_2.set_frame_on(False)
        ax_2.set_xticks([])
        ax_2.tick_params(labelsize=2, colors="white")
        ax_2.grid(alpha=0.7)

        for angle, label, rotation in zip(sales["angles"], sales["products"], sales["rotation"]):
            ax_2.text(x=angle, y=max(sales["revenue"]) + 30, s=label, rotation=rotation, ha="center", va="center", color="white", fontsize=8)

        canvas = FigureCanvasTkAgg(figure=fig_2, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().place(x=700, y=220)

    def create_table(self):
        table = ttk.Treeview(master=self.master, columns=table_columns, show="headings")

        for column in table_columns:
            table.heading(column=column, text=column)
            table.column(column=column, width=70)

        for row_data in table_data:
            table.insert(parent="", index="end", values=row_data)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#917FB3", fieldbackground="#917FB3", foreground="white")
        style.configure("Treeview.Heading", background="#917FB3", fieldbackground="#917FB3", foreground="white")
        style.map("Treeview", background=[("selected", "#E5BEEC")])

        table.place(x=395, y=225, height=260)


if __name__ == "__main__":
    window = tk.Tk()
    app = TribalThreadsApp(window)
    window.resizable(True, True)
    window.mainloop()
