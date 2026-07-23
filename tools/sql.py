import sqlite3
import json
from sqlite3 import Cursor
from pathlib import Path
from langchain.tools import tool

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / 'data' / 'northwind.db'
DB_URI = f"file:{DB_PATH}?mode=ro"

def _create_connection() -> sqlite3.Connection:
    """Create a READ-ONLY database connection to a SQLite database"""
    return sqlite3.connect(DB_URI, uri=True)


@tool
def read_sql(query: str) -> str:
    """Run a read-only SELECT query against the Northwind Wholesale database."""
    try:
        # Pass the Path object directly
        connection = _create_connection()
        cursor = connection.cursor()

        cursor.execute(query)
        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        return json.dumps(rows)

    except sqlite3.Error as e:
        return json.dumps(f'Error occurred: {e}')


