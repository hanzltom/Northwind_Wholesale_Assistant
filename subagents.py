from langchain.chat_models import init_chat_model

from pathlib import Path

from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env", override=True)

from tools.sql import read_sql, insert_sql, inspect_schema
from sys_prompts import database_agent_system_prompt

model = init_chat_model("gpt-5-mini")

research_subagent = {
    "name": "database-agent",
    "description": "Used to query the Northwind Wholesale database.",
    "system_prompt": database_agent_system_prompt,
    "tools": [read_sql, insert_sql , inspect_schema],
    "model": model,
}

subagents = [research_subagent]