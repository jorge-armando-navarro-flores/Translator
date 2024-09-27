from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


class Chain:
    def __init__(self, api_key):
        self.set_model(api_key)
        self.set_translate_chain()

    def set_model(self, api_key):
        self.model = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key)

    def set_translate_chain(self):

        parser = StrOutputParser()
        system_template = "Translate the following into {language}:"
        prompt_template = ChatPromptTemplate.from_messages(
            [("system", system_template), ("user", "{text}")]
        )

        self.chain = prompt_template | self.model | parser

    def get_chain(self):
        return self.chain
