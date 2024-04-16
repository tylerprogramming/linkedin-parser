import autogen

from autogen_info import config

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=config.llm_config,
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config=False,
    system_message="""
    Reply TERMINATE if the task has been solved at full satisfaction.
    Otherwise, reply CONTINUE, or the reason why the task is not solved yet.
    """,
)

# Create web scrapper agent.
data_parser_assistant = autogen.ConversableAgent(
    "DataParser",
    llm_config={"config_list": config.web_scrape_config_list},
    system_message="You are an agent that parses data.",
)

# Create user proxy agent.
data_parser_user_proxy = autogen.ConversableAgent(
    "UserProxy",
    llm_config=False,
    human_input_mode="NEVER",
    code_execution_config=False,  # No code execution for this agent.
    is_termination_msg=lambda x: x.get("content", "") is not None and "terminate" in x["content"].lower(),
    default_auto_reply="Please continue if not finished, otherwise return 'TERMINATE'.",
)
