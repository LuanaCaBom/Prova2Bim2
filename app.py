from flask import Flask, render_template, request, flash, redirect
from database import db
from flask_migrate import Migrate
from models import Planetas

app = Flask(__name__)
app.config['SECRET_KEY'] = '9ebe6f92407c97b3f989420e0e6bebcf9d1976b2e230acf9faf4783f5adffe1b'

# --> drive://usuario:senha@servidor/banco_de_dados

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/Planetas"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def planetas():
    u = Planetas.query.all()
    return render_template("planetas_lista.html", dados = u)

@app.route("/planetas/add")
def planetas_add():
    return render_template("planetas_add.html")

@app.route("/planetas/save", methods=['POST'])
def planetas_save():
    nome = request.form.get('nome')
    distancia_sol = request.form.get('distancia_sol')
    numero_satelites = request.form.get('numero_satelites')
    if nome and distancia_sol and numero_satelites:
        planetas = Planetas(nome, distancia_sol, numero_satelites)
        db.session.add(planetas)
        db.session.commit()
        flash('Planeta salvo com sucesso!!!')
        return redirect('/')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/planetas/add')

if __name__ == '__main__':
    app.run()