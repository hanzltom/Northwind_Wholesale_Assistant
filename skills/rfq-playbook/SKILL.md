---
name: rfq-playbook
description: Use whenever a client emails requesting pricing, bulk discounts, or a formal quote for products.
---

# Skill: Request for Quote Pipeline

Use this playbook whenever a client emails requesting pricing, bulk discounts, or a formal quote for products. 

You must strictly follow this sequence to ensure exact math, verified inventory, and proper human-in-the-loop approvals.

## Step 1: Extract Request Details
1. Instruct the inbox-manager to read the unread email using read_email.
2. Extract the client requested products and desired quantities.

## Step 2: Verify Inventory and Pricing
1. Instruct the database-analyst to query the Products table.
2. Obtain the exact UnitPrice and UnitsInStock for every requested item.
3. If UnitsInStock is less than the requested quantity, note the shortage and adjust the quote to reflect only what can be fulfilled.

## Step 3: Calculate Totals
1. You must use your Python Code Interpreter to calculate the exact totals.
2. Multiply Quantity by UnitPrice, then apply any discount.
3. Assume a zero percent discount unless the client specifically requests one or Nancy previously approved a specific rate.
4. Sum the line items into a final grand total.

## Step 4: Mathematical Sanity Check
1. Delegate to the quote-reviewer.
2. Pass the reviewer the raw inputs and your calculated line-item totals and grand total.
3. Do not proceed to Step 5 until the quote-reviewer explicitly approves the math. If it rejects the math, recalculate in Step 3.

## Step 5: Dispatch the Quote
1. Once approved by the reviewer, write a warm, professional email response detailing the quote.
2. Instruct the inbox-manager to use send_email to reply to the client.
3. This will trigger the HITL gate for Nancy to review. Once the tool returns success, consider the RFQ complete.