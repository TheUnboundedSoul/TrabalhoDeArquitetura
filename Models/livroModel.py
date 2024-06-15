from extensions import db

# Design Patterns - Builder

class Livro(db.Model):
    __tablename__ = 'livro'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    estilo_livro = db.Column(db.String(50), nullable=True)
    estante = db.Column(db.String(50), nullable=True)
    disponivel = db.Column(db.Boolean, default=True)
    requisitando_por = db.Column(db.Integer, nullable=True)
    requisitado_por = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<Livro {self.titulo}>'

    @staticmethod
    def get_by_id(livro_id):
        return Livro.query.get(livro_id)

    @staticmethod
    def get_by_titulo(titulo):
        return Livro.query.filter_by(titulo=titulo).first()

    @staticmethod
    def get_all():
        return Livro.query.all()

    def requisitar(self, utilizador_id):
        if self.disponivel:
            self.disponivel = False
            self.requisitando_por = utilizador_id
            db.session.commit()
            return True
        return False

    def entregar(self):
        if not self.disponivel:
            self.disponivel = True
            self.requisitando_por = None
            db.session.commit()
            return True
        return False

class LivroBuilder:
    def __init__(self, titulo, autor):
        self._livro = Livro(titulo=titulo, autor=autor, disponivel=True)

    def set_estilo_livro(self, estilo_livro):
        self._livro.estilo_livro = estilo_livro
        return self

    def set_estante(self, estante):
        self._livro.estante = estante
        return self

    def set_disponivel(self, disponivel):
        self._livro.disponivel = disponivel
        return self

    def set_requisitando_por(self, requisitando_por):
        self._livro.requisitando_por = requisitando_por
        return self

    def set_requisitado_por(self, requisitado_por):
        self._livro.requisitado_por = requisitado_por
        return self

    def build(self):
        return self._livro