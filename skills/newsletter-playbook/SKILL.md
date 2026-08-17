---
name: newsletter-playbook
description: Use whenever you are asked to draft, save, or send the weekly Northwind Gourmet Dispatch newsletter.
---

# Skill: Gourmet Dispatch Newsletter Pipeline

Use this playbook whenever you are asked to draft, save, or send the weekly Northwind Gourmet Dispatch newsletter.

## Step 1: Research Culinary Trends
1. Delegate to the trend-researcher.
2. Ask it to search for current, relevant news in the food and beverage wholesale industry (e.g. current seafood supply chain trends).
3. Wait for the researcher to return the synthesized bullet points.

## Step 2: Draft the Content
1. Using the research provided, draft the newsletter in Markdown format.
2. Include a warm greeting to our B2B restaurant clients.
3. Use headers, bullet points, and bold text to make the trends easy to read.
4. Conclude with a call-to-action reminding them to reply to the email for bulk quotes on related items.

## Step 3: Convert to HTML
1. Use your markdown_to_html tool. 
2. Pass your Markdown draft into the tool to generate the final HTML string. Do not skip this step; raw Markdown does not render correctly in our clients inboxes.

## Step 4: Dispatch or Save the Newsletter
1. When sending, delegate to the inbox-manager. Provide the final HTML string as the body of the email. Set the subject line to Northwind Gourmet Dispatch. This will trigger the HITL gate for Nancy to review.
2. When saving, use your write_file tool to save the final HTML string directly to the filesystem. Save it in the /newsletters/ directory using a clear, dated filename.