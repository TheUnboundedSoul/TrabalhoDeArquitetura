from flask import render_template

def render_index(livros):
    return render_template('index.html', livros=livros)

def render_livro_detalhe(livro):
    return render_template('livro_detalhe.html', livro=livro)
