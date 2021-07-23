import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content


def send_email(name, subject, content):
    my_sg = sendgrid.SendGridAPIClient(
        api_key="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")

    # Change to your verified sender
    from_email = Email("caiomanfredini.15@gmail.com")

    # Change to your recipient
    to_email = To("caiomanfredini.15@gmail.com")

    subject = f'Oi! Meu nome é {name}!'
    content = f'Email: {subject}\n{content}'

    content = Content("text/plain", content)

    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = my_sg.client.mail.send.post(request_body=mail_json)
