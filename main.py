from flask import Flask, render_template

app = Flask(__name__)


# Configuração para servir arquivos estáticos
app.static_folder = 'static'

@app.route("/") #Rota estatica com Flask
def hello_world():
    return "index"


@app.route("/noticia/<param>") #Rotas com Parametros
def noticia(param):
    return "Noticia: "+param



@app.route("/sobre")
def sobre():
    return render_template("index.html", content=['Julio', 'Kelly', 'Laura', 'Ravi']) # Salvar htmls na pasta templates

@app.route("/contato")
def contato():
    return "<h2>Contato</h2>"