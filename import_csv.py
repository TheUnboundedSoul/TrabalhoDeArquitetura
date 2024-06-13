import csv
import sqlite3

# Nome do arquivo CSV que contém os dados dos livros
CSV_FILE_PATH = 'livros.csv'

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Criar a tabela 'livro' se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        estilo TEXT,
        disponivel BOOLEAN DEFAULT 1,
        requisitado_por INTEGER,
        FOREIGN KEY (requisitado_por) REFERENCES utilizador(id)
    )
''')

# Criar a tabela 'utilizador' se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS utilizador (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Função para importar dados de um arquivo CSV
def importar_livros():
    with open(CSV_FILE_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute('''
                INSERT INTO livro (titulo, autor, estilo, disponivel)
                VALUES (?, ?, ?, ?)
            ''', (row['titulo'], row['autor'], row['estilo'], True))
        conn.commit()
    print(f"Dados importados com sucesso do arquivo {CSV_FILE_PATH}!")

# Chamar a função para importar os dados
importar_livros()

# Fechar a conexão com o banco de dados
conn.close()
