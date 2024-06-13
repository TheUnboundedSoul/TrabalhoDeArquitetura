from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_mail import Mail

# Inicializa a extensão SQLAlchemy para gerenciar a base de dados
db = SQLAlchemy()

# Inicializa a extensão Babel para suporte a internacionalização
babel = Babel()

# Inicializa a extensão Mail para enviar e-mails
mail = Mail()
