import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root=ctk.CTk()
root.geometry("500x500")
root.title("Gui")

label=ctk.CTkLabel(root, text="Hello", font=('Roboto',30))
label.pack(padx=10, pady=10)

button=ctk.CTkButton(root, text="Click", font=('Roboto',20))
button.pack(padx=10, pady=10)

root.mainloop()
