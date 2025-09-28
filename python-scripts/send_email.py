import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ---------------- Configuration ----------------
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'your-email@gmail.com'        # Replace with your Gmail address
SENDER_PASSWORD = 'your-app-password'        # Replace with your Gmail App Password

# ---------------- Function to Send Email ----------------
def send_email(to_email, subject, body):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject

        # Add human-friendly greeting
        body_text = f"Hello,\n\n{body}\n\nBest regards,\nTeam"
        msg.attach(MIMEText(body_text, 'plain'))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"✅ Email successfully sent to {to_email}!")
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}. Error: {e}")

# ---------------- Main Program ----------------
if __name__ == "__main__":
    print("=== Automatic Form Submission Email Sender ===")
    
    # Take input from user
    recipient = input("Enter recipient email: ").strip()
    subject = input("Enter email subject: ").strip()
    body = input("Enter email body/message: ").strip()

    # Send the email
    send_email(recipient, subject, body)
