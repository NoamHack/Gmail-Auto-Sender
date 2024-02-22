import smtplib
import time
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
import os

def send_email(subject, from_email, to_email, body, attachment_paths):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(body)

    # Add attachments to the email
    for filepath in attachment_paths:
        with open(filepath, 'rb') as file:
            file_data = file.read()
            file_type, _ = mimetypes.guess_type(filepath)
            if file_type is None:
                file_type = 'application/octet-stream'
            main_type, sub_type = file_type.split('/', 1)
            filename = os.path.basename(filepath)

        msg.add_attachment(file_data, maintype=main_type, subtype=sub_type, filename=filename)

    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Credentials should be an environment variable or secured storage in actual usage
    username = 'YOUR_EMAIL'
    password = 'YOUR_PASSWORD'  # Use an App Password if 2FA is enabled

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Upgrade the connection to secure
        server.login(username, password)  # Login to the server
        server.send_message(msg)  # Send the email

        print('Email sent successfully')

def main():
    subject = "YOUR_SUBJECT"
    from_email = "FROM_EMAIL"
    to_email = "TO_EMAIL"
    body = "EMAIL_BODY"
    attachment_paths = ["FILE_PATH"]

    send_interval = 60 * 60  # send every 60 minutes

    while True:
        send_email(subject, from_email, to_email, body, attachment_paths)
        time.sleep(send_interval)

if __name__ == "__main__":
    main()
