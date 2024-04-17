# Import necessary modules
from tkinter import *  # Import everything from the tkinter module
import googletrans  # Import the googletrans module
from tkinter import ttk, messagebox  # Import specific components from tkinter
import textblob  # Import the textblob module
import pyttsx3  # Import the pyttsx3 module

# Create the main window
root = Tk()
root.title('Translator')  # Set the title of the window
root.geometry('880x300')  # Set the initial size of the window

# Define a colorful theme
root.configure(bg="#88BEFF")  # Set background color of the main window

# Get the list of languages available for translation
languages = googletrans.LANGUAGES
language_list = list(languages.values())

# Creating a function to sort the languages list alphabetically
# I used here a bubble sorting
def languages_list_sorting(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Function to set style for all widgets
def set_style():
    style = ttk.Style()

    # Configure buttons
    style.configure('TButton', foreground='#0000', background='#3498db', font=('Arial', 12), padding=10)

    # Configure combo boxes
    style.configure('TCombobox', foreground='#0000', background='#34495e', font=('Arial', 11), fieldbackground='#34495e')

    # Configure text widgets
    style.configure('TText', foreground='#0000', background='#34495e', font=('Arial', 11))

    # Sort languages alphabetically for combo boxes
    languages_list_sorting(language_list)

# Call the function to set style
set_style()

# Define function to perform translation for the TRANSLATE button
def translate_it():
    translated_text.delete(1.0, END)  # Clear the translated text box
    try:
        from_lang = original_combo.get()  # Get the selected original language
        to_lang = translated_combo.get()  # Get the selected target language
        input_text = textblob.TextBlob(original_text.get(1.0, END).strip())  # Get the input text
        
        # Ensure input text is not empty
        if not input_text:
            messagebox.showwarning("Translator", "Please enter text to translate.")
            return

        # Create a translator object
        translator = googletrans.Translator()
        # Translate the input text from the original language to the target language
        translation = translator.translate(str(input_text), src=from_lang, dest=to_lang)
        
        # Insert the translated text into the text box
        translated_text.insert(1.0, translation.text)

        # Initialize the speech engine
        engine = pyttsx3.init()

        # Pass text to speech engin
        engine.say(translated_text.get(1.0, END))

        # Run the engine
        engine.runAndWait()

    except Exception as e:
        # Display an error message if translation fails
        messagebox.showerror("Translator", f"Translation failed. Error: {e}")

# Define function to clear text boxes
def clear():
    # Clear both the original and translated text boxes for the CLEAR button
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

# Function to switch between original and translated languages for the SWITCH button
def switch_languages():
    original_lang = original_combo.get()
    translated_lang = translated_combo.get()
    original_combo.set(translated_lang)
    translated_combo.set(original_lang)

# Create the original text input box
original_text = Text(root, height=10, width=40, font=("Arial", 11))
original_text.grid(row=0, column=0, padx=10, pady=20)

# Create the translate button
translate_button = Button(root, text="TRANSLATE", font=("Arial", 24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

# Create the translated text output box
translated_text = Text(root, height=10, width=40, font=("Arial", 11), state='disabled')
translated_text.grid(row=0, column=2, padx=10, pady=20)

# Create the combo boxes for selecting languages
original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)  # Set the default selection for original language 'english'
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)  # Set the default selection for target language 'french'
translated_combo.grid(row=1, column=2)

# Create a switch button
switch_button = Button(root, text="SWITCH", command=switch_languages)
switch_button.grid(row=1, column=1)

# Create the clear button
clear_button = Button(root, text="CLEAR", command=clear)
clear_button.grid(row=2, column=1)

# Start the Tkinter event loop
root.mainloop()
