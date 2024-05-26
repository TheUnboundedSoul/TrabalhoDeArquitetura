import os

class config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'biblioteca.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
