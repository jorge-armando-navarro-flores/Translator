import os
from chains import Chain
from choices import languages, chat_models

chain = Chain()


def set_openai_api_key(api_key, model, source):
    chain.set_model(api_key, model, source)
    chain.set_translate_chain()


def translate(text, language):
    try:
        return chain.get_chain().invoke({"text": text, "language": language})
    except Exception as e:
        return "There is somenting wrong with your OpenAI API Key"


def get_languages():
    return languages


def get_models(source):
    return chat_models[source]
