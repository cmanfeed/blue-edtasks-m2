from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
from send_mail import send_email

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'seuemail@gmail.com',
    "MAIL_PASSWORD": 'Suasenha'
}

app.config.update(mail_settings)


@app.route('/')
def homepage():
    # renderizar pagina inicial
    return render_template('index.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    # enviar e-mail com informações do form
    if request.method == 'POST':
        # importar dados do formm
        name = request.form['name']
        subject = request.form['subject']
        content = request.form['content']
        # enviar e-mail
        send_email(name, subject, content)
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
