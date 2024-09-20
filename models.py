from database import db

class Planetas(db.Model):
    __tablename__= "planetas"
    id_planeta = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    distancia_sol = db.Column(db.Integer)
    numero_satelites = db.Column(db.Integer)

    # construtor
    def __init__(self, nome, distancia_sol, numero_satelites):
        self.nome = nome
        self.distancia_sol = distancia_sol
        self.numero_satelites = numero_satelites

    # representação do objeto criado...
    def __repr__(self):
        return "<Planeta {}>".format(self.nome)