# Translator Application

## Declaration of own work
I confirm that this assignment is my own work. Where I have referred to academic sources, I have provided in-text citations and included the sources in the final reference list.

## Introduction
Welcome to the Translator Application README of Sofiane Boussouf with P number P434602 in the module of Intro To Programming IY499! This project aims to provide users with a simple yet powerful tool for translating text between different languages using Python's Tkinter library. With features like speech synthesis and intuitive UI, this application offers a seamless translation experience.

## Overview
This is a simple GUI application built using Python's Tkinter library for translating text between different languages. The application utilizes Google Translate API through the googletrans library and TextBlob for text manipulation. It also incorporates speech synthesis feature using pyttsx3 for reading out the translated text.
This application enables users to input text in one language, select a target language, and translate the text instantly. With intuitive controls, users can choose from a wide range of supported languages for both input and output. The translated text is displayed in real-time, facilitating effective communication across language barriers.

## Features
1. Translate text from one language to another.
2. Speech synthesis for reading out the translated text.
3. Ability to switch between original and target languages.
4. Clear functionality to erase input and output text.
5. Colorful and intuitive user interface.
6. Error handling for seamless user experience
7. Support for a vast array of languages

## Dependencies
1. [tkinter](https://docs.python.org/3/library/tkinter.html): Python's standard GUI library.
2. [googletrans](https://pypi.org/project/googletrans/): A Python wrapper for Google Translate API.
3. [textblob](https://textblob.readthedocs.io/en/dev/): A library for processing textual data.
4. [pyttsx3](https://pypi.org/project/pyttsx3/): A text-to-speech conversion library.

## Installation
Clone the repository to your local machine.
Ensure you have Python installed.

Install the required dependencies using [pip](https://pip.pypa.io/en/stable/):

```bash
pip install tkinter
```
```bash
pip install googletrans==4.0.0-rc1
```
```bash
pip install textblob
```
```bash
pip install pyttsx3
```

Run the translator.py script:

```bash
python translator.py
```

## Usage
1. Enter the text you want to translate in the left text box.
2. Select the original and target languages from the dropdown menus.
3. Click on the "Translate" button to translate the text.
4. Click on the "SWITCH" button to swap between original and target languages.
5. Click on the "CLEAR" button to clear both input and output text fields.

## Note
Ensure you have a stable internet connection as the translation functionality relies on Google Translate API.
The speech synthesis feature may not work properly in all environments and may require additional setup.

## Troubleshooting
If you encounter any issues while using the application, here are some common troubleshooting steps:

* Check your internet connection to ensure it's stable.
* Ensure that you have installed all dependencies correctly.
* If the speech synthesis feature doesn't work, check the configuration of your audio output device.

## Contributing
Contributions are welcome! If you'd like to contribute to the project, feel free to submit bug reports, feature requests, or pull requests through GitHub.

## License
This project is licensed under the MIT License - see the LICENSE file for details.