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
#Etapa 3 - listagem de livros
def listar_livros():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros")
    for linha in cursor.fetchall():
        print(f" ID {linha[0]} | TITULO {linha[1]} | AUTOR {linha[2]} | ANO {linha[3]} | DISPONIVEL {linha[4]}")

#Etapa 4 - Atualização de disponibilidade
def alte_dispo():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()
    
    id_livro = int(input("Digite o ID do livro que deseja alterar: "))

    cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (id_livro,))
    resultado = cursor.fetchone()

    if resultado is None:
        print("Livro não encontrado")
    else:
        dispo_atual = resultado[0]
        if dispo_atual == "Sim":
            novo_status = "Não"
        elif dispo_atual == "Não":
            novo_status = "Sim"
        else:
            print("Valor de disponibilidade inválido")
        return
    cursor.execute("""
        UPDATE livros
        SET disponivel = ?
        WHERE id = ?
        """, (novo_status, id_livro))
    conexao.commit()
    conexao.close()
    alte_dispo()
    