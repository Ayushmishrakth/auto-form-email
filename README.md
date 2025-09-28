readme_content = """
Automatic Form Fill & Confirmation Email Automation

Project Overview
This project automates Google Form submissions by:
- Logging responses automatically in Google Sheets
- Sending a confirmation email to respondents via Python + SMTP
- Optional AI integration for processing form responses

The automation workflow is built using n8n to watch for new Google Sheet rows and trigger a Python script for sending emails.

Features
- Automatic logging of Google Form submissions
- Immediate email confirmation to users
- Beginner-friendly Python + n8n integration
- Optional AI processing for advanced workflows

Folder Structure

auto-form-email/
├── python-scripts/
│   └── send_email.py        # Python script to send email
├── n8n-workflows/
│   └── google-form-workflow.json   # n8n workflow to watch Google Sheet
├── README.txt

Prerequisites
- Python 3.x installed
- n8n installed (locally or via Docker)
- Gmail account for sending emails (App Password required)
- Google Form linked to Google Sheet
- Basic knowledge of running Python scripts

Step 1: Google Form & Sheet Setup
1. Create a Google Form with fields such as:
   - Name
   - Email
   - Feedback (optional)
2. Link the Form responses to a Google Sheet:
   - Open Google Form → Responses → Link to Google Sheet
3. Ensure the Sheet has a column named Email for the Python script to read.

Step 2: Python Script Setup
1. Navigate to the python-scripts folder:
cd python-scripts

2. Open send_email.py and update your Gmail credentials:

SENDER_EMAIL = 'your-email@gmail.com'
SENDER_PASSWORD = 'your-app-password'  # use Gmail App Password

3. Test the script manually:
python send_email.py

- You should receive a test email at the recipient@example.com defined in the script.

Step 3: n8n Workflow Setup
1. Open n8n → Workflows → Import → n8n-workflows/google-form-workflow.json.
2. Update the Google Sheets Trigger Node:
   - Replace <YOUR_GOOGLE_SHEET_ID> with your Google Sheet ID (from URL: https://docs.google.com/spreadsheets/d/<SHEET_ID>/edit).
3. Make sure your Google Sheet columns match the workflow fields (Email column must exist).

Workflow Steps in n8n:
1. Watch Google Sheet: Watches for new rows (form submissions)
2. Get Email: Extracts the Email from the new row
3. Send Email Script: Calls Python script to send a confirmation email

Step 4: Run the Automation
1. Activate the n8n workflow.
2. Submit a response in the Google Form.
3. Verify:
   - New row appears in Google Sheet
   - Python script runs via n8n and sends a confirmation email
   - Email is received by the user

Optional AI Integration
- You can add AI processing in n8n or Python:
  - Summarize form responses
  - Detect keywords or sentiment
  - Generate insights or reports automatically

Notes & Tips
- Gmail App Password: Required for secure SMTP email sending.
- LF → CRLF warnings: Normal on Windows, can be ignored.
- Ensure your n8n server has access to the Python interpreter.
- Test each part individually: Google Form → Sheet → Python → Email.

References
- n8n Documentation: https://docs.n8n.io
- Python smtplib Docs: https://docs.python.org/3/library/smtplib.html
- Google Forms & Sheets Integration: https://support.google.com/docs/answer/6281888
"""


