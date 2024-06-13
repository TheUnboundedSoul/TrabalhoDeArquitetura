from flask import Flask
from config import DevelopmentConfig  # Importa a configuração de desenvolvimento
from Controllers.controllers import main_bp  # Importa o blueprint principal
from extensions import db  # Importa a extensão do banco de dados

def create_app():
    app = Flask(__name__, template_folder='Views', static_folder='static')
    app.config.from_object(DevelopmentConfig)  # Usa a configuração de desenvolvimento

    # Inicializa a extensão do banco de dados com a aplicação
    db.init_app(app)

    # Registra o blueprint
    app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados SQLite
    app.run(debug=True)
