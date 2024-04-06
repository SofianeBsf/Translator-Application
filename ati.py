from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

root = Tk()
root.title('Translator')
# root.iconbitmap('#')
root.geometry('880x300')

def translate():
    try:
        # get the languages from dictionary keys
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key
        
        for key, value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key

        # turn original text into a textblob
        words = textblob.TextBlob(original_text.get(1.0, END))

    except Exception as e:
        messagebox.showerror("Translator", e)

def clear():
    # clear the text boxes
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

# grab languages list from googletrans
languages = googletrans.LANGUAGES

# convert the languages dictionary to a list with values only
language_list = list(languages.values())

# text boxes
original_text = Text(root, height=10, width=40, font=("Arial", 11))
original_text.grid(row=0, column=0, padx=10, pady=20)

translate_button = Button(root, text="TRANSLATE!", font=("Arial", 24), command=translate)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40, font=("Arial", 11))
translated_text.grid(row=0, column=2, padx=10, pady=20)

#combo boxes
original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1, column=2)

# clear button
clear_button = Button(root, text="clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()