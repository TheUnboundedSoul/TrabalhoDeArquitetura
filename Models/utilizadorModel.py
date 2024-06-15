from extensions import db

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
