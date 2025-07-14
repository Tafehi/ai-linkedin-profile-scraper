import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()


def get_profile_url(name: str) -> str:
    """Get LinkedIn profile URL for a given name."""
    tavily = TavilySearch(api_key=os.getenv("TAVILY_API_KEY"))

    # Use .invoke() instead of .search()
    results = tavily.invoke({"query": name})

    if results and "results" in results and len(results["results"]) > 0:
        return results["results"][0]["url"]
    else:
        return "No LinkedIn profile found."
