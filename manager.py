from langchain_mcp_adapters.client import MultiServerMCPClient
from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model
from deepagents.backends import FilesystemBackend

from subagents import build_subagents
from pathlib import Path

from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env", override=True)

THIS_FILE = Path(__file__).resolve().parent

model = init_chat_model("gpt-5-mini")

_backend = FilesystemBackend(root_dir=str(THIS_FILE), virtual_mode=True)


async def create_manager():
    client = MultiServerMCPClient({
        "MockMailServer": {
            "transport": "sse",
            "url": "http://127.0.0.1:5002/sse"
        }
    })
    mail_tools = await client.get_tools()

    return create_deep_agent(
        name="manager",
        model=model,
        system_prompt="You are a helpful manager for Northwind Wholesale.",
        subagents=build_subagents(backend= _backend, mail_tools=mail_tools),
        skills=["/skills"],
        memory=["/AGENTS.md"],
        backend=_backend,
    )