import smtplib
import sys
from unittest.mock import patch
from fastapi.testclient import TestClient

sys.path.append("/home/rusik/TestTask")
from app.main import app, Email

client = TestClient(app)


@patch("smtplib.SMTP")
def test_send_email_success(mock_smtp):
    mock_instance = mock_smtp.return_value
    mock_instance.sendmail.return_value = {}

    response = client.post(
        "/send_email",
        json={
            "to": ["test@example.com"],
            "subject": "Test Email",
            "message": "This is a test email."
        }
    )
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"status": "success"}


def test_send_email_invalid_email():
    response = client.post(
        "/send_email",
        json={
            "to": ["invalid_email"],
            "subject": "Test Email",
            "message": "This is a test email."
        }
    )

    assert response.status_code == 422



