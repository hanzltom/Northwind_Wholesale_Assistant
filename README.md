# Northwind Wholesale Assistant

This project is a multi-agent AI sales assistant built with LangGraph for Northwind Traders, a B2B specialty foods distributor. It acts as an autonomous proxy for Account Representatives, handling client communications, dynamic quoting, and data analysis while enforcing strict Human-in-the-Loop (HITL) approval gates for critical actions.

## Capabilities

*   **Request for Quote (RFQ) Processing**: Automatically reads incoming emails, verifies database inventory, calculates exact totals using a sandboxed Code Interpreter, enforces mathematical reviews, and drafts replies.
*   **Customer Onboarding**: Identifies new email leads, queries the system, securely inserts new records (pending human approval), and dispatches sanitized HTML welcome emails.
*   **Newsletter Generation**: Uses autonomous web research to gather industry trends, drafts B2B content in Markdown, and converts it to formatted HTML before saving.
*   **Visual Reporting**: Generates dynamic Python-based charts from live SQL database metrics and saves the image files directly to a restricted local directory.

## Agent Architecture

The system operates on a hub-and-spoke model. The central Manager orchestrates complex workflows using dynamically loaded YAML playbooks and delegates narrow tasks to four specialized subagents:

*   **database-analyst**: Manages all SQLite interactions (inventory checks, price lookups, and customer creation).
*   **inbox-manager**: Interfaces with the external Mail system via the Model Context Protocol (MCP).
*   **quote-reviewer**: Acts as a strict mathematical gatekeeper to verify all pricing and volume discounts.
*   **trend-researcher**: Searches the live internet for supply chain and culinary news.

## Setup Instructions

The assistant runs entirely locally and employs a "default deny" filesystem permissions model, ensuring the AI can only write to designated directories. 

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hanzltom/Northwind_Wholesale_Assistant.git
   cd Northwind_Wholesale_Assistant
    ```
   
2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
   
3. **Install dependencies:**
    ```bash
   pip install -r requirements.txt
    ```
   
4. **Make the script executable:**
    ```bash
   chmod +x start.sh
    ```
   
5. **Visit ChatUI interface:**
    https://agentchat.vercel.app