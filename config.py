import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma-chave-secreta'  # Define uma chave secreta para a aplicação
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///biblioteca.db'  # URL do banco de dados
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance/biblioteca.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativa as notificações de modificação do SQLAlchemy
    DEBUG = False  # Desativa o modo de depuração

class DevelopmentConfig(Config):
    DEBUG = True  # Ativa o modo de depuração
    ENV = 'development'  # Define o ambiente como desenvolvimento

class TestingConfig(Config):
    TESTING = True  # Ativa o modo de teste
    DEBUG = False  # Desativa o modo de depuração para testes
    ENV = 'testing'  # Define o ambiente como teste

class ProductionConfig(Config):
    DEBUG = False  # Desativa o modo de depuração
    ENV = 'production'  # Define o ambiente como produção
