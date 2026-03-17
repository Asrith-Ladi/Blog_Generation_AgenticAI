from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

class GroqLLM:
    def __init__(self):
        load_dotenv()
    
    def get_llm(self):
        try:
            os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
            llm = ChatGroq(model_name= "llama-3.1-8b-instant")
            return llm
        except Exception as e:
            raise ValueError("Error occured with exception : {e}")
            