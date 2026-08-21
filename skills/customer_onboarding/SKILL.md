---
name: customer-onboarding
description: Use whenever you need to check if a sender is a new customer, add them to the database, and send them a welcome email.
---

# Skill: Customer Onboarding Pipeline

Use this playbook whenever you process an email from a potential new client, or are explicitly asked to onboard a new customer.

## Step 1: Extract Sender Details
1. Instruct the inbox-manager to read the new email.
2. Extract the sender contact name, email address, and company name.

## Step 2: Check Customer Database
1. Delegate to the database-analyst.
2. Ask it to query the Customers table to see if the company or contact already exists.
3. If the customer already exists, stop this playbook here and handle their request normally.

## Step 3: Insert New Customer
1. If the customer does not exist, instruct the database-analyst to insert a new record into the Customers table.
2. Provide the analyst with the extracted company name and contact name.
3. This will trigger a database approval gate. Wait for the tool to return success (meaning Nancy approved the insertion) before proceeding.

## Step 4: Draft Welcome Email
1. Draft a warm Welcome to Northwind Wholesale email in Markdown format.
2. Include a brief introduction to our B2B specialty foods catalog and let them know Nancy is their dedicated Account Representative.

## Step 5: Dispatch
1. Instruct the inbox-manager to send the email using send_email with the subject Welcome to Northwind Traders.
