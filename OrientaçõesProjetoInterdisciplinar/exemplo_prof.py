import sqlite3
from sqlite3 import Error

banco = 'bdturmab/bancodb.db'
conn = None
conn = sqlite3.connect(banco)
print("Conexão estabelecida!")
c = conn.cursor()


def seleciona():
    result = c.execute("SELECT rowid, first_name, last_name FROM pessoas;")
    print(c.fetchall())

# seleciona()

def selecionaUm(nome):
    result = c.execute("SELECT * FROM pessoas where first_name like (?)", ('%'+nome+'%',))
    print(c.fetchall())

#nome = input("Indique o nome a pesquisar: ")
#selecionaUm(nome)

def criar_tabela():
    c.execute("CREATE TABLE pessoas (first_name TEXT NOT NULL,last_name TEXT NOT NULL);")
    conn.commit()
    print("Tabela Criada!")
    seleciona()

# criar_tabela()

def inserir_unico():
    c.execute("INSERT INTO pessoas (first_name, last_name) VALUES('Giancoli', 'Ana');")
    conn.commit()
    print('Registro inserido!')
    seleciona()

#inserir_unico()

def inserir_varios():
    pessoa = [('Ana', 'Giancoli'),
              ('Paula', 'Muller'),
              ('Ana Paula', 'Muller Giancoli'),
             ]
    c.executemany('INSERT INTO pessoas VALUES (?,?)', pessoa)
    conn.commit()
    print('Registros inseridos!')
    seleciona()

# inserir_varios()



def atualizar_tabela():
    last_name = input('Indique o sobrenome: ')
    x = input('Indique o id a ser atualizado: ')
    values = (last_name, x)
    c.execute("UPDATE pessoas SET last_name=? WHERE rowid=?;", values)
    conn.commit()
    seleciona()

#atualizar_tabela()

def excluir_registro():
    x = int(input('Indique o registro a excluir: '))
    values = (x,)
    c.execute("DELETE FROM pessoas WHERE rowid=?", values)
    conn.commit()
    print('Registro excluído!')
    seleciona()

# excluir_registro()