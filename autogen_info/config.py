import autogen
from dotenv import load_dotenv

load_dotenv()

config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST.json",
    filter_dict={
        "model": ["gpt-3.5-turbo"],
    },
)

# config_list = autogen.config_list_from_json(
#     "OAI_CONFIG_LIST.json",
#     filter_dict={
#         "model": ["phi2"],
#     },
# )

web_scrape_config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST.json",
    filter_dict={
        "model": ["gpt-3.5-turbo"],
    },
)

# web_scrape_config_list = autogen.config_list_from_json(
#     "OAI_CONFIG_LIST.json",
#     filter_dict={
#         "model": ["phi2"],
#     },
# )

llm_config = {
    "timeout": 600,
    "config_list": config_list,
    "temperature": 0,
}
