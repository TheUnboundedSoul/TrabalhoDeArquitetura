from extensions import db

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    disponivel = db.Column(db.Boolean, default=True)
    requisitado_por = db.Column(db.String(100), nullable=True)

    def __init__(self, titulo, autor, disponivel=True, requisitado_por=None):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel
        self.requisitado_por = requisitado_por

def get_livro_by_titulo(titulo):
    return Livro.query.filter_by(titulo=titulo).first()
