from flask import Blueprint, request, render_template, redirect, url_for
from models import get_livro_by_titulo, Livro
from extensions import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    livros = Livro.query.all()
    return render_template('index.html', livros=livros)

@main_bp.route('/pesquisar', methods=['POST'])
def pesquisar():
    titulo = request.form['titulo']
    livro = get_livro_by_titulo(titulo)
    if livro:
        return render_template('livro_detalhe.html', livro=livro)
    return "Livro não encontrado", 404

@main_bp.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        novo_livro = Livro(titulo=titulo, autor=autor)
        db.session.add(novo_livro)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('adicionar.html')