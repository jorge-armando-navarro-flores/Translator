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

1. **Clone the Repository**

   ```sh
   git clone https://github.com/jorge-armando-navarro-flores/Translator.git

   cd Translator
   ```

2. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Configure Environment Variables**
   Create a `.env` file in the root directory and add your email and OpenAI credentials:
   ```env
   OPENAI_API_KEY=Your_OpenAI_API_key
   ```
5. **Run the Chatbot**
   ```sh
   python app.py
   ```
