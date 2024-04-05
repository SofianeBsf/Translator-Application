from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob

root = Tk()
root.geometry("700x400")
root.title("Language Translator")
root.config(bg = '#D3D3D3')

Label(root, text = "Language Translator-PythonFlood", font = ('Arial, bold', 20), bg = '#8B8B7A')