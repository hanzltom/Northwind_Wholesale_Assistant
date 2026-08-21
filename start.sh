#!/bin/bash

trap 'echo "Shutting down servers..."; kill $(jobs -p)' EXIT

echo "Starting Mail MCP Server..."
python3.11 mcp/mcp_inbox.py &

sleep 10

echo "Starting LangGraph Dev Server..."
langgraph dev