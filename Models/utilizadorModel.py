from extensions import db

# Design Pattern - Strategy

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

class PasswordValidationStrategy:
    @staticmethod
    def is_valid(password):
        # Implementação básica de validação de senha
        return len(password) >= 6

class UtilizadorValidator:
    def __init__(self, validation_strategy):
        self.validation_strategy = validation_strategy

    def validate_password(self, password):  
        print(f'Validando senha com estratégia: {self.validation_strategy.__class__.__name__}')
        return self.validation_strategy.is_valid(password)