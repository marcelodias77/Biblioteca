import sqlite3

conexao = sqlite3.connect("biblioteca.db")

cursor = conexao.cursor()

def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT
        )
    """)