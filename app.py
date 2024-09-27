from chains import translate_chain
from choices import languages


def translate(text, language):
    return translate_chain.invoke({"text": text, "language": language})


def get_languages():
    return languages
