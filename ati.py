from tkinter import *
import googletrans
from tkinter import ttk, messagebox
import textblob

root = Tk()
root.title('Translator')
root.geometry('880x300')

def translate_it():
    translated_text.delete(1.0, END)
    try:
        from_lang = original_combo.get()
        to_lang = translated_combo.get()
        input_text = textblob.TextBlob(original_text.get(1.0, END).strip())
        
        translator = googletrans.Translator()
        translation = translator.translate(str(input_text), src=from_lang, dest=to_lang)
        
        translated_text.insert(1.0, translation.text)
    except Exception as e:
        messagebox.showerror("Translator", f"Translation failed. Error: {e}")

def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

languages = googletrans.LANGUAGES
language_list = list(languages.values())

original_text = Text(root, height=10, width=40, font=("Arial", 11))
original_text.grid(row=0, column=0, padx=10, pady=20)

translate_button = Button(root, text="TRANSLATE!", font=("Arial", 24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40, font=("Arial", 11))
translated_text.grid(row=0, column=2, padx=10, pady=20)

original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1, column=2)

clear_button = Button(root, text="clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()