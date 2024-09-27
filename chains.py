from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


class Chain:
    def __init__(self):
        self.model = None
        self.chain = None

    def set_model(self, api_key, model):
        self.model = ChatOpenAI(model=model, api_key=api_key)

    def set_translate_chain(self):

        parser = StrOutputParser()
        system_template = "Translate the following into {language}:"
        prompt_template = ChatPromptTemplate.from_messages(
            [("system", system_template), ("user", "{text}")]
        )

        self.chain = prompt_template | self.model | parser

    def get_chain(self):
        return self.chain
