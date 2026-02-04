import requests
from django.shortcuts import render, redirect

URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "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" # Replace with your real key

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost:8000",
    "X-Title": "AI Chatbot for Khata Accounting & Inventory System",
}

# 1. THE MANUAL DATA
MANUAL_DATA = khata_manual = """
Software User Manual

(Account & Inventory Management System)

URL: https://khatasystem.com

Khata Accounting Software is a comprehensive and highly automated accounting and inventory management system designed to meet the needs of diverse business sectors, including manufacturers, traders, distributors, retailers, importers, and service providers. It delivers an integrated solution covering financial accounting, inventory control, invoicing, VAT accounting, receivables, payables, and MIS reporting. Built on modern, upgradable technology, Khata emphasizes simplicity, flexibility, security, and reliability while adhering strictly to accounting principles. Its advanced features, analytical reports, and customer-driven enhancements make it a robust, user-friendly, and competitive business management solution.

Purpose:

Facilitate accurate financial record-keeping
Simplify inventory and stock management
Automate sales, purchase, and voucher operations
Provide real-time reporting for management decisions
Maintain audit trails and regulatory compliance

Scope:
This manual provides step-by-step instructions for all users, including:

Administrators
Accountants
Sales and purchase staff
Managers and auditors
IT support personnel

Key Features:

Multi-level User Privileges and access control
Master Data Management for products, categories, units, brands, locations
Comprehensive Entry Menu for vouchers, purchases, sales, manufacturing, and services
Audit and Financial Reports for IRD compliance, P&L, Balance Sheet, Cash Flow
Inventory Reports including opening stock, stock transfer, stock value, and adjustments
Customizable Settings for barcode, print layout, POS, SQL analysis, and global system defaults
Help and support including manuals, FAQs, feedback, and release notes

Intended Users:

Internal staff responsible for financial, inventory, or operational management
External auditors requiring system transparency
New employees for onboarding and training

System Requirements:

Operating System: Windows 10 or later
Database: SQL Server 2016 or later
Web Browser: Chrome, Edge, Firefox (latest versions)
Internet connectivity for updates and IRD synchronization

Tips for Users:

Follow steps in sequence for each menu operation
Check user privileges before accessing modules
Always verify data entries for accuracy
Use the Help / Support menu for additional guidance


Home Menu

The Home menu is the starting point of the KHATA System. It gives access to core administrative functions such as fiscal year management, user setup, tax configuration, and menu access privileges. Proper use of this menu ensures that the system is configured correctly before entering transactions.

Fiscal Year Setup

The Fiscal Year Setup menu allows administrators to create, edit, or close fiscal years, which is foundational for all accounting and reporting in the system. Accurate fiscal year setup ensures that all vouchers, transactions, and reports are aligned with the correct period.

Purpose & Context:
Used at the beginning of every Nepal fiscal year to ensure all transactions are recorded in the correct accounting period.

Steps:

Navigate: Home → Fiscal Year → Fiscal Year Setup
Click Add New to create a fiscal year.
Enter start date, end date, and other required fields.
Click Save to store the fiscal year.

Example Scenario:
An accounting administrator prepares the system for the new fiscal year 2083/84. All subsequent vouchers automatically align with this fiscal year.

Tips:
Avoid overlapping fiscal years.
Verify dates before saving.


Change Fiscal Year

This menu allows users to switch the active fiscal year in the system.

Purpose & Context:
Used when reviewing previous years’ reports or entering historical data.

Steps:

Navigate: Home → Fiscal Year → Change Fiscal Year
Select the desired fiscal year from the list.
Click Confirm.

Tips:
Always verify the fiscal year before switching.
Avoid changing during active transaction posting.


User Setup

The User Setup menu allows administrators to create, edit, or deactivate system users.

Purpose & Context:
Used to manage system users and access rights.

Steps:

Navigate: Home → User Setup
Click Add New User
Fill in user details
Click Save

Tips:
Use strong passwords.
Review active users regularly.


Tax Setup

The Tax Setup menu allows administrators to configure VAT and other taxes.

Steps:

Navigate: Home → Tax Setup
Click Add New Tax
Enter tax name, percentage, and type
Click Save

Tips:
Keep tax rates updated.
Verify taxes in a test invoice.


Company Info

The Company Info menu allows administrators to update company details used in invoices and reports.

Steps:

Navigate: Home → Company Info
Edit company details
Click Save


Master Menu

The Master Menu manages all master data, including accounts, products, and locations.

Account Ledger Creation

Steps:

Navigate: Master → Account → Account Ledger Creation
Click Add New Ledger
Enter ledger details
Click Save


Product Creation

Steps:

Navigate: Master → Product → Product Creation
Click Add New Product
Enter product details
Click Save


Entry Menu

The Entry Menu handles vouchers, purchases, sales, manufacturing, and services.

Voucher Draft

Steps:

Navigate: Entry → Voucher → Voucher Draft
Click Add New Voucher
Enter details
Save as Draft


Audit Menu

Used for financial review, compliance, and regulatory reporting.

Trial Balance

Steps:

Navigate: Audit → Financial → Trial Balance
Select date range
Generate Report


Report Menu

Provides transaction, statement, and inventory reports.

Inventory Reports include:

Opening Stock Report
Stock Transfer Report
Stock Summary Report
Stock Value Report
Stock Adjustment Report


Setting Menu

Used to configure system-wide preferences and security settings.

Backup & Restore

Steps:

Navigate: Setting → Backup & Restore
Click Backup Now


Help / Support Menu

Provides user manuals, FAQs, contact support, and release notes.

User Manual

Navigate: Help → User Manual

FAQs

Navigate: Help → FAQs

Contact Support

Navigate: Help → Contact Support

System Updates

Navigate: Help → System Updates / Release Notes
"""


IDENTITY_PROMPT = (
    "You are a helpful assistant. Reply in plain text only. "
    "You are an expert in the Khata Accounting & Inventory System software. Your task is to assist users by answering questions about this software based on the provided MANUAL DATA. "
    "You are not affiliated with OpenAI. Keep replies under 100 words. "
    "Do not use markdown like hashes (#) or asterisks (*). "
    "Do not use bullet points or numbered lists, and tables and code snippets. "
    "Use the following MANUAL DATA to answer questions about the software: "
)

def chatbot(request):
    if "chat_history" not in request.session:
        request.session["chat_history"] = []
    
    messages = request.session["chat_history"]

    if request.method == "POST":
        if "clear_chat" in request.POST:
            request.session["chat_history"] = []
            return redirect("chatbot")

        user_input = request.POST.get("user_text")
        if user_input:
            messages.append({"role": "user", "content": user_input})
            
            # Combine Identity + Manual into one System Message
            combined_system_message = {"role": "system", "content": IDENTITY_PROMPT + MANUAL_DATA}
            
            try:
                # 3. THE API CALL (Combining system prompt + history)
                response = requests.post(
                    URL, 
                    headers=HEADERS, 
                    json={
                        "model": "openai/gpt-4o-mini", 
                        "messages": [combined_system_message] + messages
                    },
                    timeout=120 
                )
                
                if response.status_code == 200:
                    data = response.json()
                    ai_reply = data["choices"][0]["message"]["content"]
                    messages.append({"role": "assistant", "content": ai_reply})
                    request.session["chat_history"] = messages
                    request.session.modified = True
                else:
                    messages.append({"role": "assistant", "content": "Error: API connection failed."})
            
            except Exception:
                messages.append({"role": "assistant", "content": "The request timed out. Please try again."})

    return render(request, "chatbot.html", {"messages": messages})