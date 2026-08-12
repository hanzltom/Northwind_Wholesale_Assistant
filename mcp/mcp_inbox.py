
import json
from pathlib import Path
from typing import List, Dict, Any
from fastmcp import FastMCP

mcp = FastMCP(name="MockMailServer")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INBOX_FILE = DATA_DIR / "inbox.json"
OUTBOX_FILE = DATA_DIR / "outbox.json"

@mcp.tool
def list_inbox() -> List[Dict[str, str]] | Dict[None, Any]:
    """List all incoming email summaries in the inbox."""
    with open(INBOX_FILE, "r", encoding="utf-8") as f:
        inbox =  json.load(f)

    return [
        {
            "id": msg_id,
            "sender": data["sender"],
            "subject": data["subject"],
            "status": data["status"]
        }
        for msg_id, data in inbox.items()
    ]


@mcp.tool
def read_email(email_id: str) -> Dict[str, Any]:
    """Read the full subject and body of a specific email by ID. Automatically marks it as 'read'."""
    with open(INBOX_FILE, "r", encoding="utf-8") as f:
        inbox = json.load(f)

    if email_id not in inbox:
        raise ValueError(f"Email with ID {email_id} not found.")

    inbox[email_id]["status"] = "read"
    with open(INBOX_FILE, "w", encoding="utf-8") as f:
        json.dump(inbox, f)

    return inbox[email_id]


@mcp.tool
def send_email(to_email: str, subject: str, body: str) -> str:
    """Send an email reply to a customer and record it in the outbox. [HITL]"""
    new_message = {
        "to": to_email,
        "subject": subject,
        "body": body
    }

    try:
        with open(OUTBOX_FILE, "r", encoding="utf-8") as f:
            outbox = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        outbox = []

    outbox.append(new_message)

    with open(OUTBOX_FILE, "w", encoding="utf-8") as f:
        json.dump(outbox, f)

    return f"Successfully sent email to {to_email} with subject '{subject}'."


if __name__ == "__main__":
    mcp.run(transport="sse", host="127.0.0.1", port=5002)