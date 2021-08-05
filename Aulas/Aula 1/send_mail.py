import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content


def send_email(name, subject, content):
    my_sg = sendgrid.SendGridAPIClient(
        api_key=os.environ.get('SENDGRID_API_KEY'))

    # Change to your verified sender
    from_email = Email("caiomanfredini.15@gmail.com")

    # Change to your recipient
    to_email = To("caiomanfredini.15@gmail.com")

    subject = f'Você recebeu uma mensagem!'
    content = f'De: {name}\nEmail: {subject}\n{content}'

    content = Content("text/plain", content)

    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = my_sg.client.mail.send.post(request_body=mail_json)
