from flask import render_template

# Função para renderizar a página inicial com a lista de livros
def render_index(livros):
    return render_template('index.html', livros=livros)

# Função para renderizar a página de detalhes de um livro específico
def render_livro_detalhe(livro):
    return render_template('livro_detalhe.html', livro=livro)

# Função para renderizar a página de login
def render_login():
    return render_template('login.html')

# Função para renderizar a página de adição de um novo utilizador
def render_add_user():
    return render_template('add_user.html')

# Função para renderizar a página de pesquisa de livros
def render_pesquisar():
    return render_template('pesquisar.html')

# Função para renderizar os resultados da pesquisa de livros
def render_resultado_pesquisa(livros):
    return render_template('resultado_pesquisa.html', livros=livros)

# Função para renderizar a página de requisição de um livro
def render_requisitar():
    return render_template('requisitar.html')

# Função para renderizar a página de devolução de um livro
def render_entregar():
    return render_template('entregar.html')

def render_adicionar():
    return render_template('adicionar.html')

def render_remover():
    return render_template('remover.html')