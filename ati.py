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

# Define function to perform translation
def translate_it():
    translated_text.delete(1.0, END)  # Clear the translated text box
    try:
        from_lang = original_combo.get()  # Get the selected original language
        to_lang = translated_combo.get()  # Get the selected target language
        input_text = textblob.TextBlob(original_text.get(1.0, END).strip())  # Get the input text
        
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
    # Clear both the original and translated text boxes
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

# Function to switch between original and translated languages
def switch_languages():
    original_lang = original_combo.get()
    translated_lang = translated_combo.get()
    original_combo.set(translated_lang)
    translated_combo.set(original_lang)

# Get the list of languages available for translation
languages = googletrans.LANGUAGES
language_list = list(languages.values())

# Create the original text input box
original_text = Text(root, height=10, width=40, font=("Arial", 11))
original_text.grid(row=0, column=0, padx=10, pady=20)

# Create the translate button
translate_button = Button(root, text="TRANSLATE!", font=("Arial", 24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

# Create the translated text output box
translated_text = Text(root, height=10, width=40, font=("Arial", 11))
translated_text.grid(row=0, column=2, padx=10, pady=20)

# Create the combo boxes for selecting languages
original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)  # Set the default selection for original language
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)  # Set the default selection for target language
translated_combo.grid(row=1, column=2)

# Create a switch button
switch_button = Button(root, text="SWITCH", command=switch_languages)
switch_button.grid(row=1, column=1)

# Create the clear button
clear_button = Button(root, text="clear", command=clear)
clear_button.grid(row=2, column=1)

# Start the Tkinter event loop
root.mainloop()
