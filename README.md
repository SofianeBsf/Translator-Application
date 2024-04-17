Translator Application

Overview
This is a simple GUI application built using Python's Tkinter library for translating text between different languages. The application utilizes Google Translate API through the googletrans library and TextBlob for text manipulation. It also incorporates speech synthesis feature using pyttsx3 for reading out the translated text.

Features
1. Translate text from one language to another.
2. Speech synthesis for reading out the translated text.
3. Ability to switch between original and target languages.
4. Clear functionality to erase input and output text.
5. Colorful and intuitive user interface.

Dependencies
'tkinter': Python's standard GUI library.
'googletrans': A Python wrapper for Google Translate API.
'textblob': A library for processing textual data.
'pyttsx3': A text-to-speech conversion library.

How to Use
Clone the repository to your local machine.
Ensure you have Python installed.
Install the required dependencies using pip:

pip install googletrans==4.0.0-rc1 textblob pyttsx3

Run the translator.py script:

python translator.py

Enter the text you want to translate in the left text box.
Select the original and target languages from the dropdown menus.
Click on the "Translate" button to translate the text.
Click on the "SWITCH" button to swap between original and target languages.
Click on the "CLEAR" button to clear both input and output text fields.

Note
Ensure you have a stable internet connection as the translation functionality relies on Google Translate API.
The speech synthesis feature may not work properly in all environments and may require additional setup.

License
This project is licensed under the MIT License - see the LICENSE file for details.