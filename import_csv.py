import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Adicionar a coluna 'requisitado_por'
cursor.execute("ALTER TABLE livro ADD COLUMN requisitado_por TEXT")

# Confirmar as mudanças e fechar a conexão
conn.commit()
conn.close()
