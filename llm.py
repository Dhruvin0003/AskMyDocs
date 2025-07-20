from langchain_cohere import ChatCohere
import os
from dotenv import load_dotenv
load_dotenv()

def get_llm():
    return ChatCohere(model="command-r-plus",temperature=0.7,cohere_api_key=os.environ.get("CO_API_KEY"))
