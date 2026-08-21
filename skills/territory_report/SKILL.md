---
name: territory-report
description: Use whenever Nancy asks for a visual chart, graph, or sales report of her territory or products.
---

# Skill: Visual Territory Reporting

Use this playbook whenever you are asked to generate a visual chart or sales report.

## Step 1: Gather the Data
1. Delegate to the database-analyst.
2. Ask it to query the database for the specific metrics requested (for example, the top 5 products by inventory value, or sales by category).
3. Wait for the analyst to return the raw data numbers.

## Step 2: Render the Chart (Code Interpreter)
1. Use your Python Code Interpreter tool.
2. Write a Python script using matplotlib to generate a clear, visually appealing chart (bar chart, pie chart, etc.) based on the data provided by the analyst.
3. Ensure the chart includes a title, labeled axes, and formatted numbers.
4. Instruct the script to save the figure as a PNG file directly to the /reports/ directory (e.g. /reports/top_products.png). 
5. Do not try to display the chart to the screen using plt.show(), just save it to the file.

## Step 3: Summarize for Nancy
1. Once the file is successfully saved, write a brief Markdown summary of the findings.
2. Tell Nancy the exact file path where the generated chart was saved so she can open it.