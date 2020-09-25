import sqlite3
from sqlite3 import Error

def createBanco(db_file):
    conn = None 
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS 
                        categoria (
                            descricao text NOT NULL
                        );
                    ''')
        conn.commit()
        conn.commit()
        c.execute('''CREATE TABLE IF NOT EXISTS 
                        pergunta (
                            id_categoria int,
                            descricao text NOT NULL,
                            FOREIGN KEY (id_categoria) REFERENCES categoria (rowid)
                        ); 
                    ''')
        conn.commit()
        c.execute('''CREATE TABLE IF NOT EXISTS 
                        resposta (
                            id_pergunta int,
                            descricao text NOT NULL,
                            favorito int DEFAULT 0,
                            FOREIGN KEY (id_pergunta) REFERENCES pergunta (rowid)
                        ); 
                    ''')
        conn.commit()   
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()    

def inserirCategoria(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute("INSERT INTO categoria (descricao) VALUES ('teste9?');")
        conn.commit()
        c.execute("SELECT rowid, descricao FROM categoria;")
        print(c.fetchall())            
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()