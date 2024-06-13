from flask import Flask
from config import config
from controllers import main_bp
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(main_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados SQLite
    app.run(debug=True)


# O ruben esteve aqui