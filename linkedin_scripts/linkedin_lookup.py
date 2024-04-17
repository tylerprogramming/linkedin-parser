import os
import re

from dotenv import load_dotenv
from tavily import TavilyClient

import autogen_info.agents as agents

load_dotenv()


def lookup(name: str) -> str:
    tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    response = tavily.search(
        query=
        f"""
            Crawl Google for a LinkedIn Profile Page with the username {name}.  
        """
    )

    data = response["results"]
    print(data)

    chat_result = agents.data_parser_user_proxy.initiate_chat(
        agents.data_parser_assistant,
        message=f"""For the data found with {data}, can you parse this and give me the best possible result for a
                linkedin profile with valid url for {name}?  ONLY return the users linkedin url such as 
                https://www.linkedin.com/in/elonmusk, with no extra text or messages.""",
        summary_method="reflection_with_llm"
    )

    result = chat_result.summary

    # Regular expression pattern to find the username after '/in/'
    pattern = r'/in/(\w+)'

    # Search for the pattern in the input string
    match = re.search(pattern, result)
    username = match.group(1)

    # Extract the username from the URL
    # username = result[start_index + len("https://www.linkedin.com/in/"):end_index]

    return username


if __name__ == "__main__":
    linkedin_url = lookup(name="Tyler Reed AI")
