import os
import smtplib, ssl


def send_email(message_local):
    host = "smtp.gmail.com"
    port = 465
    username = "daithileonard@gmail.com"
    # password = os.getenv("PASSWORD")
    password = "ecwvfmndasfhrsmh"
    receiver = "daithileonard@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message_local)