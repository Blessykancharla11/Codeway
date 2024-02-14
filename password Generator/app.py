import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
import random
from tkinter import PhotoImage
import string
import pyautogui

ventana = tk.Tk()
ventana.title("Password Generator")
logo = PhotoImage(file="icono.png")
ventana.iconphoto(False, logo)
ventana.resizable(width=False, height=False)
ventana.geometry("400x300")  # Set window size

# Function to generate password
def generar_func():
    tam = tam_variable.get()
    caja_contra.delete('1.0', tk.END)
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    chars = lower + upper + num + symbols
    temp = random.sample(chars, tam)
    lol = "".join(temp)
    
    caja_contra.insert(tk.END, lol)
   
    ventana.clipboard_clear() 
    ventana.clipboard_append(lol)
    
    pyautogui.alert(text="Generated password copied to clipboard.", title="Password Generator")

# Entry for password length
tam_entry = ttk.Entry(ventana)
tam_variable = tk.IntVar()
tam_entry.configure(justify="center", textvariable=tam_variable)
tam_entry.place(anchor="nw", relx=0.32, rely=0.12, x=0, y=0)

# Button to generate password
generar_button = ttk.Button(ventana, text='Generate Password', command=generar_func)
generar_button.place(anchor="nw", relx=0.40, rely=0.37, x=0, y=0)

# Text area to display generated password
caja_contra = ScrolledText(ventana)
caja_contra.place(anchor="nw", relheight=0.23, relwidth=0.68, relx=0.24, rely=0.68, x=0, y=0)

# Start GUI loop
if __name__ == "__main__":
    ventana.mainloop()
