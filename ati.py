from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

root = Tk()
root.title('Translator')
root.iconbitmap('#')
root.geometry('880x300')

def translate():
    pass

original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, padx=10, pady=20)

translate_button = Button(root, text="TRANSLATE!", font=("Arial", 24), command=translate)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, padx=10, pady=20)

