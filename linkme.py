from dotenv import load_dotenv

from autogen_info import agents
from linkedin_scripts.linkedin_lookup import lookup
from linkedin_scripts.linkedin_scrape import scrape_linkedin_profile


def start_scraping(name: str) -> str:
    linkedin_username = lookup(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_user_id=linkedin_username)

    response = agents.user_proxy.initiate_chat(
        agents.assistant,
        message=f"""
        Given the linkedin information {linkedin_data} about a person, I want you to put this information into json 
        format:
         1. A short summary
         2. Two interesting facts about them
         3. What is their Education?
         4. How many posts or activities do they have?
         
         Only give me the json back.  Do not write any code.  Do not write python or shell scripts.
         
        """,
        max_turns=2
    )

    summary = response.summary
    return summary


if __name__ == "__main__":
    load_dotenv()

    print("Commence the Scrape!")
    start_scraping("Tyler Reed AI")
