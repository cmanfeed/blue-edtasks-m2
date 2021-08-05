from flask import Flask, render_template, redirect, request
# Importa o Mail e o Message do flask_mail para facilitar o envio de emails
from flask_mail import Mail, Message


app = Flask(__name__)

# Configuração do envio de email.
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
}

# atualizar as configurações do app com o dicionário mail_settings
app.config.update(mail_settings)
mail = Mail(app)  # atribuir a class Mail o app atual.


# Classe para capturar as informações do formulário de forma mais organizada
class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

# Rota principal apenas para renderizar a página principal.


@app.route('/')
def index():
    return render_template('index.html')

# Rota de envio de email.


@app.route('/contact', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        # Capiturando as informações do formulário com o request do Flask e criando o objeto formContato
        formContato = Contato(
            request.form['name'],
            request.form['email'],
            request.form['content']
        )

        # Criando o objeto msg, que é uma instancia da Class Message do Flask_Mail
        msg = Message(
            subject='Contato do seu Portfólio de teste',  # Assunto do email
            # Quem vai enviar o email, pega o email configurado no app (mail_settings)
            sender=app.config.get("MAIL_USERNAME"),
            # Quem vai receber o email, mando pra mim mesmo, posso mandar pra mais de um email.
            recipients=[app.config.get("MAIL_USERNAME")],
            # Corpo do email.
            body=f'''O {formContato.nome} com o email {formContato.email}, te mandou a seguinte mensagem: 
         
               {formContato.mensagem}'''
        )
        # envio efetivo do objeto msg através do método send() que vem do Flask_Mail
        mail.send(msg)
    # Renderiza a página de confirmação de envio.
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
