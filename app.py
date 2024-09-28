import os
from chains import Chain
from choices import languages, openai_chat_models

chain = Chain()


def set_openai_api_key(api_key, model):
    chain.set_model(api_key, model)
    chain.set_translate_chain()


def translate(text, language):
    try:
        return chain.get_chain().invoke({"text": text, "language": language})
    except Exception as e:
        return str(e)


def get_languages():
    return languages


def get_models():
    return openai_chat_models
