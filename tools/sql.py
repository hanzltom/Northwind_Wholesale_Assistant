import sqlite3
import json
from sqlite3 import Cursor
from pathlib import Path
from langchain.tools import tool

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / 'data' / 'northwind.db'
DB_URI_RO = f"file:{DB_PATH}?mode=ro"
DB_URI_RW = f"file:{DB_PATH}?mode=rw"

def _create_connection(URI: str) -> sqlite3.Connection:
    """Create a READ-ONLY database connection to an SQLite database"""
    return sqlite3.connect(URI, uri=True)


@tool
def read_sql(query: str) -> str:
    """Run a read-only SELECT query against the Northwind Wholesale database."""
    try:
        connection = _create_connection(DB_URI_RO)
        cursor = connection.cursor()

        cursor.execute(query)
        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        return json.dumps({
            "status": "success",
            "message": "Query read successfully",
            "data": rows
        })

    except sqlite3.Error as e:
        return json.dumps({
            "status": "success",
            "message": f"Error occurred: {e}",
        })

@tool
def insert_sql(query: str) -> str:
    """Run an INSERT query to add a new Customer, Product, Supplier, etc. [HITL]"""
    try:
        connection = _create_connection(DB_URI_RW)
        cursor = connection.cursor()

        cursor.execute(query)
        connection.commit()

        cursor.close()
        connection.close()

        return json.dumps({
            "status": "success",
            "message": "Query inserted successfully"
        })


    except sqlite3.Error as e:

        return json.dumps({

            "status": "success",

            "message": f"Error occurred: {e}",

        })

@tool
def inspect_schema() -> str:
    """Inspect the schema of the Northwind Wholesale database.
        Call this tool once to learn the schema and save it to memories/AGENTS.md
        so you don't have to call it again."""
    try:
        connection = _create_connection(DB_URI_RO)
        cursor = connection.cursor()

        cursor.execute("SELECT name, sql FROM sqlite_master "
                       "WHERE type='table' ORDER BY name")
        rows = cursor.fetchall()
        res = "\n\n".join([f"{row[0]}:\n{row[1]}" for row in rows])

        cursor.close()
        connection.close()

        return res

    except sqlite3.Error as e:
        return json.dumps({
            "status": "success",
            "message": f"Error occurred: {e}",
        })


