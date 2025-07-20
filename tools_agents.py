from langchain.agents import AgentType,Tool,initialize_agent
from langchain_community.utilities import GoogleSearchAPIWrapper
from llm import get_llm
from dotenv import load_dotenv
load_dotenv()

def create_agent():
    
    google_tool = [Tool(
        name="Google",
        func=GoogleSearchAPIWrapper().run,
        description="Useful for retrieving information from google.")]
    
    agent = initialize_agent(
        tools=google_tool,
        llm=get_llm(),
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True)

    return agent