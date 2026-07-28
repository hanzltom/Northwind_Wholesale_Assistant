from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model

from pathlib import Path

from dotenv import load_dotenv

from tools.sql import read_sql, insert_sql, inspect_schema
from sys_prompts import database_agent_system_prompt
from deepagents.backends import CompositeBackend, StateBackend, FilesystemBackend
from deepagents import MemoryMiddleware, FilesystemPermission
from langgraph.checkpoint.memory import MemorySaver



load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env", override=True)
_memories_dir = Path(__file__).resolve().parent.parent / "memories"
_memories_dir.mkdir(exist_ok=True)

model = init_chat_model("gpt-5-mini")

_backend = CompositeBackend(
    default=StateBackend(),
    routes={
        "/memories/": FilesystemBackend(root_dir=str(_memories_dir), virtual_mode=True)
    }
)

agent = create_deep_agent(
    model=model,
    tools=[read_sql, insert_sql, inspect_schema],
    system_prompt=database_agent_system_prompt,
    backend=_backend,
    middleware=[
        MemoryMiddleware(
            backend=_backend,
            sources=["/memories/AGENTS.md"],
        )
    ],
    interrupt_on={"insert_sql": True},
    checkpointer=MemorySaver(),
)

config = {"configurable": {"thread_id": "2"}}
print("HA")

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Insert into SHIPPERS id: 888, name: ahoj, phone: 123. Then output all the shippers.",
            }
        ]
    },
    config = config,
    version="v1",
)

print(result)

