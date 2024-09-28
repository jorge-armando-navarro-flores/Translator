---
title: Translator
emoji: 🌖
colorFrom: yellow
colorTo: blue
sdk: docker
pinned: false
---

# Translator

Simple translator

## Demo

[Live Demo](https://huggingface.co/spaces/JanfNavf/Translator)

## Setup and Installation

### Linux

1. **Clone the Repository**

   ```sh
   git clone https://github.com/jorge-armando-navarro-flores/Translator.git

   cd Translator
   ```

2. **Create a Virtual Environment**

   ```sh
   python -m venv venv

   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Chatbot**
   ```sh
   python app.py
   ```

### Windows

1. **Install Python**

   - [Download Python](https://www.python.org/ftp/python/3.10.0/python-3.10.0rc2-amd64.exe)
   - Execute "python-3.10.0rc2-amd64.exe" from Downloads

2. **Install git**

   - [Download git](https://github.com/git-for-windows/git/releases/download/v2.46.2.windows.1/Git-2.46.2-64-bit.exe)
   - Execute "Git-2.46.2-64-bit.exe" from Downloads

3. **Open CMD**

   - Click the taskbar
   - Type "cmd" in the search field
   - Click "Command Prompt" to run with standard user rights
   - Right-click "Command Prompt" and select "Run as administrator" to run with administrator rights

     You can also open the command prompt by:
     Pressing the "Windows logo" key and "R" at the same time, then typing "CMD" into the search bar
     Pressing the "Windows logo" key and "X" simultaneously, then pressing "Command Prompt (Admin)" in the power menu

4. **Clone the Repository**

   ```sh
   git clone https://github.com/jorge-armando-navarro-flores/Translator.git

   cd Translator
   ```

5. **Create a Virtual Environment**

   ```sh
   python -m venv venv
   source venv\Scripts\activate
   ```

6. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

7. **Run the Chatbot**
   ```sh
   python app.py
   ```

## Customization

To add more characters or modify the list, edit the `choices.py` file, where you can define each character’s unique style and manage their availability in the list.

Example for adding a new language:

```python
languages = [
    "Mandarin Chinese",
    "Spanish",
    "English",
    "Hindi",
    "Bengali",
    "Portuguese",
    "Russian",
    "Japanese",
    "Western Punjabi",
    "Marathi",
    "Telugu",
    "Turkish",
    "Korean",
    "French",
    "German",
    "Vietnamese",
    "Tamil",
    "Italian",
    "Urdu",
    "Javanese",
    # Add more languages here
]
```

## Technologies

- **Python**
- **OpenAI API** – For IA and LLMs.
- **Gradio** – For the interactive interface.
- **Langchain** – For orchestration
