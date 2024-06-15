from flask import Flask
from config import DevelopmentConfig  # Importa a configuração de desenvolvimento
from Controllers.controllers import main_bp  # Importa o blueprint principal
from extensions import db  # Importa a extensão do banco de dados

# Design Pattern SINGLETON

class FlaskAppSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FlaskAppSingleton, cls).__new__(cls)
            cls._instance.app = Flask(__name__, template_folder='Views', static_folder='static')
            cls._instance.app.config.from_object(DevelopmentConfig)  # Usa a configuração de desenvolvimento

            # Inicializa a extensão do banco de dados com a aplicação
            db.init_app(cls._instance.app)

            # Registra o blueprint
            cls._instance.app.register_blueprint(main_bp)
        return cls._instance

    def get_app(self):
        return self.app

def create_app():
    flask_app_singleton = FlaskAppSingleton()
    return flask_app_singleton.get_app()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados SQLite
    app.run(debug=True)
