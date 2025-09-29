import sqlite3




#"Etapa 1 - Criação do banco e tabela"
def criar_tabela():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT
        )
    """)
    conexao.commit()
#Etapa 2 - Cadastro de livros
def cadastra_livro():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()
    
    titu = input("Digite o titulo do livro: ")
    aut = input("Digite o nome do autor: ")
    ano = int(input("Digite o ano do livro: "))
    dispo = input("Digite se o livro está disponivel: ")
    cursor.execute("""
    INSERT INTO livros (titulo, autor, ano, disponivel)
    VALUES (?, ?, ?, ?)
    """, (titu, aut, ano, dispo)
    )
    conexao.commit()
    conexao.close()
cadastra_livro()