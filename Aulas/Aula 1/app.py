from flask import Flask, render_template, request, redirect
from send_mail import send_email

app = Flask(__name__)


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
