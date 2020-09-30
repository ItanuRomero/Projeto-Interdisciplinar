import sqlite3

database = 'database/database.db'
conn = sqlite3.connect(database)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS categoria (
  descricao TEXT NOT NULL
);''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS pergunta (
  id_categoria INTEGER NOT NULL,
  descricao TEXT NOT NULL,
  FOREIGN KEY (id_categoria) REFERENCES categoria(rowid) ON UPDATE CASCADE ON DELETE CASCADE
);''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS resposta (
  id_pergunta INTEGER PRIMARY KEY,
  descricao TEXT NOT NULL,
  favorito int DEFAULT 0,
  FOREIGN KEY (id_pergunta) REFERENCES pergunta(rowid) ON UPDATE CASCADE ON DELETE CASCADE
);''')
conn.commit()


def select_category_by_id(category_id):
    c.execute("SELECT rowid, descricao FROM categoria WHERE rowid = ?;", str(category_id))
    return c.fetchall()


def select_all_categories():
    c.execute("SELECT rowid, descricao FROM categoria;")
    return c.fetchall()


def insert_category(category):
    c.execute(f"INSERT INTO categoria VALUES('{category}');")
    conn.commit()


def delete_category(category_id):
    c.execute(f"DELETE FROM categoria WHERE rowid = ?;", str(category_id))
    conn.commit()


def select_question_by_id(question_id):
    c.execute("SELECT rowid, descricao FROM pergunta WHERE rowid = ?;", str(question_id))
    return c.fetchall()


def select_all_questions_by_category(category_id):
    c.execute("SELECT rowid, descricao FROM pergunta WHERE id_categoria = ?;", str(category_id))
    return c.fetchall()


def insert_question(category_id, question):
    c.execute(f"INSERT INTO pergunta VALUES('{category_id}', '{question}');")
    conn.commit()


def delete_question(question_id):
    c.execute(f"DELETE FROM pergunta WHERE rowid = ?;", str(question_id))
    conn.commit()


def select_answer_by_id(answer_id):
    c.execute("SELECT rowid, descricao FROM resposta WHERE rowid = ?;", str(answer_id))
    return c.fetchall()


def select_all_answers_by_question_id(question_id):
    c.execute("SELECT rowid, descricao FROM resposta WHERE id_pergunta = ? ORDER BY favorito DESC;", str(question_id))
    return c.fetchall()


def insert_answer(answer_id, answers):
    c.execute(f"INSERT INTO resposta VALUES('{answer_id}', '{answers}', 0);")
    conn.commit()


def increment_answer_rank(answer_id):
    c.execute(f"UPDATE resposta set favorito = favorito + 1 where rowid = ?;", answer_id)
    conn.commit()


def delete_answer(answer_id):
    c.execute(f"DELETE FROM resposta WHERE rowid = ?;", str(answer_id))
    conn.commit()
