from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from deepagents import MemoryMiddleware
from deepagents.backends import CompositeBackend, StateBackend, FilesystemBackend
from deepagents.backends.protocol import BackendProtocol
from pathlib import Path

from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env", override=True)
_memories_dir = Path(__file__).resolve().parent.parent / "memories"
_memories_dir.mkdir(exist_ok=True)

from tools.sql import read_sql, insert_sql, inspect_schema
from tools.search import internet_search
from sys_prompts import database_agent_system_prompt, inbox_manager_system_prompt, quote_reviewer_system_prompt, search_agent_system_prompt

model = init_chat_model("gpt-5-mini")

def build_subagents(backend: BackendProtocol, mail_tools: list, search: bool = False):
    db_tools = [read_sql, insert_sql, inspect_schema]

    db_interrupts = {
        tool.name: True
        for tool in db_tools
        if "[HITL]" in tool.description
    }

    mail_interrupts = {
        tool.name: True
        for tool in mail_tools
        if "[HITL]" in tool.description
    }

    subagents = []
    database_analyst = {
        "name": "database-analyst",
        "model": model,
        "description": "Used to query the Northwind Wholesale database.",
        "system_prompt": database_agent_system_prompt,
        "tools": [read_sql, insert_sql , inspect_schema],
        "middleware" : [
            MemoryMiddleware(
                backend=backend,
                sources=["/memories/AGENTS.md"],
            )
        ],
        "interrupt_on" : db_interrupts,
    }

    inbox_manager = {
        "name": "inbox-manager",
        "model": model,
        "description": "Used to interact with mail services.",
        "system_prompt": inbox_manager_system_prompt,
        "tools": mail_tools,
        "interrupt_on": mail_interrupts,
    }

    quote_reviewer = {
        "name": "quote-reviewer",
        "model": model,
        "description": "Used to review a drafted quote (line items, discount, total) for correct arithmetic and sane pricing before it is sent. Send it the numbers.",
        "system_prompt": quote_reviewer_system_prompt,
    }

    if search:
        trend_researcher = {
            "name": "trend-researcher",
            "model": model,
            "description": "Used to search for information and trends across the internet.",
            "system_prompt": search_agent_system_prompt,
            "tools": [internet_search]
        }

        subagents.append(trend_researcher)

    subagents.extend([database_analyst, inbox_manager, quote_reviewer])
    return subagents