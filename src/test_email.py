import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

msg = MIMEText("Test email depuis ton projet DevOps 🚀")
msg["Subject"] = "Test Alert"
msg["From"] = EMAIL
msg["To"] = EMAIL

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
    server.quit()
    print("✅ Email envoyé")
except Exception as e:
    print("❌ Erreur :", e)