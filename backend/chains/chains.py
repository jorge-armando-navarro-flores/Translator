from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint


class Chain:
    def __init__(self):
        self.model = None
        self.chain = None

    def set_model(self, api_key, model, source):
        if source == "OpenAI":
            self.model = ChatOpenAI(model=model, api_key=api_key)
        elif source == "Groq":
            self.model = ChatGroq(model=model, api_key=api_key)
        elif source == "MistralAI":
            self.model = ChatMistralAI(model=model, api_key=api_key)
        elif source == "HuggingFace":
            llm = HuggingFaceEndpoint(
                repo_id=model,
                max_length=128,
                temperature=0.5,
                huggingfacehub_api_token=api_key,
            )

            self.model = ChatHuggingFace(llm=llm)

    def set_translate_chain(self):

        parser = StrOutputParser()
        system_template = "Translate the following into {language}:"
        prompt_template = ChatPromptTemplate.from_messages(
            [("system", system_template), ("user", "{text}")]
        )

        self.chain = prompt_template | self.model | parser

    def get_chain(self):
        return self.chain
