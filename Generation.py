from agno.agent import Agent, RunResponse 
from agno.models.google import Gemini
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GOOGLE_API_KEY"] = ""


def generate_summary(data: str) -> str:
   
    agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    instructions=["Your task is to summarise the the invoice and classify it into the correct category."],
)
    response=agent.run(data)
    print(response.content)
    return response.content