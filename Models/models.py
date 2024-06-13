from extensions import db

class Livro(db.Model):
    __tablename__ = 'livro'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    estilo_livro = db.Column(db.String(50), nullable=True)  # Altere aqui para corresponder ao nome da coluna
    estante = db.Column(db.String(50), nullable=True)
    disponivel = db.Column(db.Boolean, default=True)
    requisitando_por = db.Column(db.Integer, nullable=True)
    requisitado_por = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<Livro {self.titulo}>'

    @staticmethod
    def create(titulo, autor, estilo_livro=None, estante=None, disponivel=True, requisitando_por=None, requisitado_por=None):
        return Livro(titulo=titulo, autor=autor, estilo_livro=estilo_livro, estante=estante, disponivel=disponivel, requisitando_por=requisitando_por, requisitado_por=requisitado_por)

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

class Utilizador(db.Model):
    __tablename__ = 'utilizador'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Utilizador {self.username}>'

    @staticmethod
    def create(username, password):
        return Utilizador(username=username, password=password)

    @staticmethod
    def get_by_id(utilizador_id):
        return Utilizador.query.get(utilizador_id)

    @staticmethod
    def get_by_username(username):
        return Utilizador.query.filter_by(username=username).first()

    @staticmethod
    def get_all():
        return Utilizador.query.all()
