import os
from langchain_core.tools import tool
from tavily import TavilyClient

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])


@tool
def internet_search(query: str, max_results: int = 5) -> dict:
    """Search the internet for information on a specific topic."""
    return tavily_client.search(query, max_results=max_results, topic="news")