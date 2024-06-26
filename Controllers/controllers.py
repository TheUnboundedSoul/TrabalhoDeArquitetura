from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from Models.livroModel import Livro, LivroBuilder
from Models.utilizadorModel import Utilizador, UtilizadorValidator, PasswordValidationStrategy
from extensions import db

# Decorator para verificar se o usuário está autenticado
def login_required(f):
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            flash('Você precisa estar logado para acessar esta página.', 'warning')
            return redirect(url_for('main.login'))
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__  # Necessário para o Flask
    return wrapper

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    livros = Livro.query.all()
    return render_template('index.html', livros=livros)
    #return render_template('index.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Utilizador.get_by_username(username)
        if user and user.password == password:
            session['user_id'] = user.id
            flash('Login bem-sucedido', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Nome de usuário ou senha inválidos', 'danger')
    return render_template('login.html')

@main_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Você saiu da sessão.', 'info')
    return redirect(url_for('main.login'))

@main_bp.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if Utilizador.get_by_username(username):
            flash('Nome de usuário já existe', 'danger')
        else:
            # Validando a senha utilizando UtilizadorValidator
            validator = UtilizadorValidator(PasswordValidationStrategy())
            is_valid_password = validator.validate_password(password)
            print(f'A senha do utilizador é válida: {is_valid_password}')
            
            if is_valid_password:
                new_user = Utilizador.create(username, password)
                db.session.add(new_user)
                db.session.commit()
                flash('Usuário adicionado com sucesso', 'success')
                return redirect(url_for('main.login'))
            else:
                flash('A senha não atende aos requisitos mínimos', 'danger')

    return render_template('add_user.html')

@main_bp.route('/pesquisar', methods=['GET', 'POST'])
@login_required
def pesquisar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        autor = request.form.get('autor')
        estilo_livro = request.form.get('estilo_livro')
        query = Livro.query
        if nome:
            query = query.filter(Livro.titulo.ilike(f'%{nome}%'))
        if autor:
            query = query.filter(Livro.autor.ilike(f'%{autor}%'))
        if estilo_livro:
            query = query.filter(Livro.estilo_livro.ilike(f'%{estilo_livro}%'))
        livros = query.all()
        return render_template('resultado_pesquisa.html', livros=livros)
    return render_template('pesquisar.html')

@main_bp.route('/requisitar', methods=['GET', 'POST'])
@login_required
def requisitar():
    if request.method == 'POST':
        id_livro = request.form['id_livro']
        livro = Livro.get_by_id(id_livro)
        if livro and livro.requisitar(utilizador_id=session['user_id']):
            flash(f'Livro {livro.titulo} requisitado com sucesso!', 'success')
        else:
            flash('Livro não disponível ou não encontrado.', 'danger')
    return render_template('requisitar.html')

@main_bp.route('/entregar', methods=['GET', 'POST'])
@login_required
def entregar():
    if request.method == 'POST':
        id_livro = request.form['id_livro']
        livro = Livro.get_by_id(id_livro)
        if livro and livro.entregar():
            flash(f'Livro {livro.titulo} entregue com sucesso! Coloque na estante {livro.estante}.', 'success')
        else:
            flash('Livro não encontrado ou já entregue.', 'danger')
    return render_template('entregar.html')


@main_bp.route('/adicionar', methods=['GET', 'POST'])
@login_required
def adicionar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        estilo_livro = request.form.get('estilo_livro')
        estante = request.form.get('estante')
        
        # Cria um novo Livro usando LivroBuilder
        livro_builder = LivroBuilder(titulo, autor)
        
        # Define os campos opcionais
        if estilo_livro:
            livro_builder.set_estilo_livro(estilo_livro)
        if estante:
            livro_builder.set_estante(estante)
        
        novo_livro = livro_builder.build()
        
        # Adiciona o novo livro ao banco de dados
        try:
            db.session.add(novo_livro)
            db.session.commit()
            flash('Livro adicionado com sucesso', 'success')
            return redirect(url_for('main.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao adicionar livro: {str(e)}', 'danger')
    
    return render_template('adicionar.html')

@main_bp.route('/remover_livro', methods=['GET'])
@login_required
def remover_livro():
    livros = Livro.query.all()
    return render_template('remover.html', livros=livros)

@main_bp.route('/confirmar_remover', methods=['POST'])
@login_required
def confirmar_remover():
    livro_id = request.form.get('livro_id')
    livro = Livro.get_by_id(livro_id)
    
    if not livro:
        flash('Livro não encontrado.', 'danger')
    else:
        try:
            db.session.delete(livro)
            db.session.commit()
            flash(f'Livro "{livro.titulo}" removido com sucesso.', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao remover livro: {str(e)}', 'danger')

    return redirect(url_for('main.index'))