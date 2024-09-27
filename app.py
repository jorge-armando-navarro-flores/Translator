import os
from chains import Chain
from choices import languages

chain = Chain(api_key="")


def set_openai_api_key(api_key):
    chain.set_model(api_key)
    chain.set_translate_chain()


def translate(text, language):
    try:
        return chain.get_chain().invoke({"text": text, "language": language})
    except:
        return "There is somenting wrong with your OpenAI API Key"


def get_languages():
    return languages
