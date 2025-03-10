from app import db

class Employe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    poste = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Employe('{self.nom}', '{self.prenom}', '{self.email}', '{self.poste}')"

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    entreprise = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Client('{self.nom}', '{self.prenom}', '{self.email}', '{self.entreprise}')"

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    chemin = db.Column(db.String(255), nullable=False)
    date_upload = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"Document('{self.nom}', '{self.chemin}', '{self.date_upload}')"