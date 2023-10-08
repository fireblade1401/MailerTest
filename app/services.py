import smtplib
from .config import (EMAIL_HOST, EMAIL_HOST_PASSWORD, EMAIL_HOST_USER, EMAIL_PORT)


def send_email(email):
    msg = f"Subject: {email.subject}\n\n{email.message}"
    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        smtp.sendmail(EMAIL_HOST_USER, email.to, msg.encode('utf-8'))
