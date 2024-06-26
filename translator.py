# Import necessary modules
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import googletrans
import pyttsx3

# Create the main window
root = tk.Tk()
root.title('Translator')  # Set the title of the window
root.geometry('880x500')  # Set the initial size of the window

# Define a colorful theme
root.configure(bg="#F5F5F5")  # Set background color of the main window

# Get the list of languages available for translation
languages = googletrans.LANGUAGES
language_list = list(languages.values())

# Creating a function to sort the languages list alphabetically
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
    style.configure('TButton', foreground='#000000', background='#4CAF50', font=('Arial', 12), padding=10)

    # Configure combo boxes
    style.configure('TCombobox', foreground='#000000', background='#E0E0E0', font=('Arial', 11), fieldbackground='#E0E0E0')

    # Configure text widgets
    style.configure('TText', foreground='#000000', background='#E0E0E0', font=('Arial', 11))

# Call the function to set style
set_style()

# Function to perform translation for the TRANSLATE button
def translate_it():
    translated_text.config(state='normal')  # Enable the text widget for insertion
    translated_text.delete(1.0, tk.END)  # Clear the translated text box
    
    try:
        from_lang = original_combo.get()  # Get the selected original language
        to_lang = translated_combo.get()  # Get the selected target language
        input_text = original_text.get(1.0, tk.END).strip()  # Get the input text
        
        # Ensure input text is not empty
        if not input_text:
            messagebox.showwarning("Translator", "Please enter text to translate.")
            return

        # Create a translator object
        translator = googletrans.Translator()
        # Translate the input text from the original language to the target language
        translation = translator.translate(input_text, src=from_lang, dest=to_lang)
        
        # Insert the translated text into the text box
        translated_text.insert(1.0, translation.text)

        # Initialize the speech engine
        engine = pyttsx3.init()

        # Pass text to speech engin
        engine.say(translated_text.get(1.0, tk.END))

        # Run the engine
        engine.runAndWait()

    except Exception as e:
        # Display an error message if translation fails
        messagebox.showerror("Translator", f"Translation failed. Error: {e}")

    finally:
        translated_text.config(state='disabled')  # Disable the text widget after insertion

# Define function to clear text boxes
def clear():
    # Clear both the original and translated text boxes for the CLEAR button
    original_text.delete(1.0, tk.END)
    translated_text.config(state='normal')  # Enable the text widget for insertion
    translated_text.delete(1.0, tk.END)  # Clear the translated text box
    translated_text.config(state='disabled')  # Disable the text widget after insertion

# Function toswitch between original and translated languages for the SWITCH button
def switch_languages():
    # Get the currently selected original language from the original combo box
    original_lang = original_combo.get()
    # Get the currently selected target language from the translated combo box
    translated_lang = translated_combo.get()
    # Set the value of the original combo box to the currently selected target language
    original_combo.set(translated_lang)
    # Set the value of the translated combo box to the currently selected original language
    translated_combo.set(original_lang)

# Function to save translated text to favorites
def add_to_favorites():
    # Getting the original and translated text from their respective Text widgets, removing leading/trailing whitespace
    original = original_text.get(1.0, tk.END).strip()
    translated = translated_text.get(1.0, tk.END).strip()
    # Checking if both original and translated text exist
    if original and translated:
        # Check if the translation already exists in favorites
        with open("favorites.txt", "r") as file:
            if any(f"{original} : {translated}" in line for line in file):
                # Translation already exists in favorites
                messagebox.showinfo("Translator", "Translation already added to favorites.")
            else:
                # Append the translation to the "favorites.txt" file
                with open("favorites.txt", "a") as file:
                    file.write(f"{original} : {translated}\n")
                # Show an information messagebox confirming successful addition
                messagebox.showinfo("Translator", "Translation added to favorites.")
    else:
        # Show a warning messagebox if either original or translated text is missing
        messagebox.showwarning("Translator", "Please perform a translation first.")

# Function to delete translation from favorites
def delete_from_favorites(original, translated):
    # Asking for confirmation before deletion
    deletion_confirmation = messagebox.askyesno("Delete from Favorites", "Are you sure you want to delete this translation from favorites?")
    if deletion_confirmation:
        # Reading all lines from "favorites.txt"
        with open("favorites.txt", "r") as file:
            lines = file.readlines()
        # Writing all lines back to "favorites.txt" except the one to be deleted
        with open("favorites.txt", "w") as file:
            for line in lines:
                if f"{original} : {translated}" not in line:
                    file.write(line)
        # Showing an information messagebox confirming successful deletion
        messagebox.showinfo("Translator", "Translation deleted from favorites.")

# Function to load and edit favorite translation
def edit_favorite():
    # Creating a new window to display favorites
    favorites_window = tk.Toplevel(root)
    favorites_window.title("Edit Favorites")
    favorites_window.geometry("400x300")

    # Adding a scrollbar to navigate through the list of favorites
    scroll = tk.Scrollbar(favorites_window)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # Creating a listbox to display the favorites
    favorites_listbox = tk.Listbox(favorites_window, yscrollcommand=scroll.set)
    favorites_listbox.pack(fill=tk.BOTH, expand=1)

    # Reading all lines from "favorites.txt" and populating the listbox with them
    with open("favorites.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        favorites_listbox.insert(tk.END, line.strip())

    # Function to handle the editing of a selected favorite translation
    def on_edit():
        # Getting the index of the selected item in the listbox
        selected_index = favorites_listbox.curselection()
        if selected_index:
            # Getting the selected item and splitting it into original and translated parts
            selected_item = favorites_listbox.get(selected_index)
            original, translated = selected_item.split(" : ")
            # Asking the user for a new translation
            new_translation = simpledialog.askstring("Edit Translation", "Enter the new translation:", initialvalue=translated)
            if new_translation:
                # Updating the selected translation with the new one in "favorites.txt"
                with open("favorites.txt","r") as file:
                    lines = file.readlines()
                with open("favorites.txt", "w") as file:
                    for line in lines:
                        if line.strip() == selected_item.strip():
                            file.write(f"{original} : {new_translation}\n")
                        else:
                            file.write(line)
                # Showing an information messagebox confirming successful editing
                messagebox.showinfo("Translator", "Translation edited in favorites.")
                # Clearing and repopulating the listbox with updated favorites
                favorites_listbox.delete(0, tk.END)
                with open("favorites.txt", "r") as file:
                    lines = file.readlines()
                for line in lines:
                    favorites_listbox.insert(tk.END, line.strip())

    # Function to handle the deletion of a selected favorite translation
    def on_delete():
        # Getting the index of the selected item in the listbox
        selected_index = favorites_listbox.curselection()
        if selected_index:
            # Getting the selected item and splitting it into original and translated parts
            selected_item = favorites_listbox.get(selected_index)
            original, translated = selected_item.split(" : ")
            # Calling the delete_from_favorites function to remove the selected translation from "favorites.txt"
            delete_from_favorites(original, translated)
            # Deleting the selected item from the listbox
            favorites_listbox.delete(selected_index)

    # Button to trigger the edit function
    edit_button = tk.Button(favorites_window, text="Edit", command=on_edit)
    edit_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Button to trigger the delete function
    delete_button = tk.Button(favorites_window, text="Delete", command=on_delete)
    delete_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Configuring the scrollbar to work with the listbox
    scroll.config(command=favorites_listbox.yview)

# Create the original text input box
original_text = tk.Text(root, height=10, width=40, font=("Arial", 12, "bold"))
original_text.grid(row=0, column=0, padx=10, pady=20)

# Color the border of the text input field
original_text.config(highlightbackground="#4CAF50", highlightthickness=2)

# Create the translate button
translate_button = ttk.Button(root, text="TRANSLATE", command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

# Create the translated text output box
translated_text = tk.Text(root, height=10, width=40, font=("Arial", 12, "bold"), state='disabled')
translated_text.grid(row=0, column=2, padx=10, pady=20)

# Create the combo boxes for selecting languages
original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)  # Set the default selection for original language 'english'
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)  # Set the default selection for target language 'french'
translated_combo.grid(row=1, column=2)

# Create a switch button
switch_button = ttk.Button(root, text="SWITCH", command=switch_languages)
switch_button.grid(row=1, column=1, pady=5)

# Create the clear button
clear_button = ttk.Button(root, text="CLEAR", command=clear)
clear_button.grid(row=2, column=1, pady=5)

# Create the add to favorites button
add_to_favorites_button = ttk.Button(root, text="Add to Favorites", command=add_to_favorites)
add_to_favorites_button.grid(row=2, column=0, padx=5)

# Create the edit favorites button
edit_favorites_button = ttk.Button(root, text="Edit Favorites", command=edit_favorite)
edit_favorites_button.grid(row=2, column=2, padx=5)

# Start the Tkinter event loop
root.mainloop()