from abc import ABC, abstractmethod
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama, HuggingFaceEndpoint
from langchain_community.chat_models.huggingface import ChatHuggingFace

class LLM(ABC):
    def __init__(self, name: str):
        self.name = name
        self.llm = None
        self.embeddings = None

    def get_name(self):
        return self.name

    def get_llm(self):
        return self.llm

    def get_embeddings(self):
        return self.embeddings


class OllamaModel(LLM):
    def __init__(self, name: str):
        super().__init__(name)
        self.llm = Ollama(model=self.name)
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


class HFModel(LLM):
    def __init__(self, name, token):
        super().__init__(name)
        self.llm = ChatHuggingFace(llm=HuggingFaceEndpoint(
            huggingfacehub_api_token=f"{token}",
            repo_id=self.name,
            task="text-generation",
            max_new_tokens=512,
            top_k=30,
            temperature=0.1,
            repetition_penalty=1.03,
        ))
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")