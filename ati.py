from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

root = Tk()
root.title('Translator')
root.iconbitmap('#')
root.geometry('880x300')

original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, padx=10, pady=20)