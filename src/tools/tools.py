from langchain.tools import tool
# from requests
from dotenv import load_dotenv
import os
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


# @tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic . Returns Titles , URLs and Snippets of the search results."""

    results = tavily.search(query=query, max_results=5)

    return str(results)


print(results)
