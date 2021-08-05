
from flask import Flask, render_template, redirect, request, session, flash
from flask_mail import Mail, Message #Importa o Mail e o Message do flask_mail para facilitar o envio de emails
from flask_sqlalchemy import SQLAlchemy # ORM responsável por realizar as operações do banco de dados via Python
# from mail_config import email, mail_senha # Módulo para esconder meu user e senha do email.

app = Flask(__name__)
app.secret_key = 'bluedtech' # Chave de criptografia para guardar sessão de login

# Configuração do envio de email.
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
   #  "MAIL_USERNAME": email,
   #  "MAIL_PASSWORD": mail_senha
}

app.config.update(mail_settings) #atualizar as configurações do app com o dicionário mail_settings
mail = Mail(app) # atribuir a class Mail o app atual.

# Conexão com o banco de dados, o nome entre os colchetes é padrão, o endereço do banco nós achamos nos Datails da instancia do nosso banco no ElephantSQL, no campo URL
# ATENÇÃO! A URL do ElephantSQL vem como postegres://(o resto da URL). 
# Modifique essa parte antes do // para postegresql://(o resto da URL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bktphuuo:JmaTz43tFPlkJ3TKKqFgNH51y2oHv4mq@tuffi.db.elephantsql.com/bktphuuo'
db = SQLAlchemy(app) # Instancia o objeto db na classe SQLAlchemy e adiciona essa aplicação nela.

#--------------------------------

# Classes:

class Contato:
   def __init__ (self, nome, email, mensagem):
      self.nome = nome
      self.email = email
      self.mensagem = mensagem

class Projeto(db.Model): # Projetos herda metodos de db.Model
   # Criação das colunas na tabela projetos:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    imagem = db.Column(db.String(500), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    link = db.Column(db.String(300), nullable=False)
   # Construção dos atributos da classe Projeto, que receberão os dados a serem inseridos nas colunas criadas acima
    def __init__(self, nome, imagem, descricao, link):
        self.nome = nome
        self.imagem = imagem
        self.descricao = descricao
        self.link = link

#ATENÇÃO os nomes das colunas tem que ser os mesmos nomes dos atributos da classe Projeto.
#--------------------------------

# Rota principal apenas para renderizar a página principal.
@app.route('/')
def index():
   session['usuario_logado'] = None
   projetos = Projeto.query.all()  # Busca todos os projetos no banco e coloca na veriável projetos, que se transforma em uma lista.
   return render_template('index.html', projetos=projetos) # Renderiza a página index.html mandando a lista de projetos

#--------------------------------

# Rota de envio de email.
@app.route('/send', methods=['GET', 'POST'])
def send():
   if request.method == 'POST':
      # Capiturando as informações do formulário com o request do Flask e criando o objeto formContato
      formContato = Contato(
         request.form['nome'],
         request.form['email'],
         request.form['mensagem']
      )

      # Criando o objeto msg, que é uma instancia da Class Message do Flask_Mail
      msg = Message(
         subject= 'Contato do seu Portfólio', #Assunto do email
         sender=app.config.get("MAIL_USERNAME"), # Quem vai enviar o email, pega o email configurado no app (mail_settings)
         recipients=[app.config.get("MAIL_USERNAME")], # Quem vai receber o email, mando pra mim mesmo, posso mandar pra mais de um email.
         # Corpo do email.
         body=f'''O {formContato.nome} com o email {formContato.email}, te mandou a seguinte mensagem: 
         
               {formContato.mensagem}''' 
         )
      mail.send(msg) #envio efetivo do objeto msg através do método send() que vem do Flask_Mail
   return render_template('send.html', formContato=formContato) # Renderiza a página de confirmação de envio.

#--------------------------------



@app.route('/adm') # Rota da administração
def adm():
   projetos = Projeto.query.all() # Busca todos os projetos no banco e coloca na veriável projetos, que se transforma em uma lista.
   return render_template('adm.html', projetos=projetos) # Caso esteja logado, renderiza a página adm.html passando a lista de projetos.

#--------------------------------



if __name__ == '__main__':
   db.create_all() # Cria o banco assim que a aplicação é ligada.
   app.run(debug=True)
