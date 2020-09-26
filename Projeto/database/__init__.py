import sqlite3
from sqlite3 import Error

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

def selectCategoryById(categoryId):
  c.execute("SELECT rowid, descricao FROM categoria WHERE rowid = ?;", str(categoryId))
  return c.fetchall()

def selectAllCategories():
  c.execute("SELECT rowid, descricao FROM categoria;")
  return c.fetchall()

def insertCategory(category):
  c.execute(f"INSERT INTO categoria VALUES('{category}');")
  conn.commit()

def deleteCategory(categoryId):
  c.execute(f"DELETE FROM categoria WHERE rowid = ?;", str(categoryId))
  conn.commit()


def selectQuestionById(questionId):
  c.execute("SELECT rowid, descricao FROM pergunta WHERE rowid = ?;", str(questionId))
  return c.fetchall()

def selectAllQuestionsByCategory(categoryId):
  c.execute("SELECT rowid, descricao FROM pergunta WHERE id_categoria = ?;", str(categoryId))
  return c.fetchall()

def insertQuestion(categoryId, question):
  c.execute(f"INSERT INTO pergunta VALUES('{categoryId}', '{question}');")
  conn.commit()

def deleteQuestion(questionId):
  c.execute(f"DELETE FROM pergunta WHERE rowid = ?;", str(questionId))
  conn.commit()


def selectAnswerById(answerId):
  c.execute("SELECT rowid, descricao FROM resposta WHERE rowid = ?;", str(answerId))
  return c.fetchall()

def selectAllAnswersByQuestionId(questionId):
  c.execute("SELECT rowid, descricao FROM resposta WHERE id_pergunta = ? ORDER BY favorito DESC;", str(questionId))
  return c.fetchall()

def insertAnswer(answerId, answers):
  c.execute(f"INSERT INTO resposta VALUES('{answerId}', '{answers}', 0);")
  conn.commit()

def incrementAnswerRank(answerId):
  c.execute(f"UPDATE resposta set favorito = favorito + 1 where rowid = ?;", answerId)
  conn.commit()

def deleteAnswer(answerId):
  c.execute(f"DELETE FROM resposta WHERE rowid = ?;", str(answerId))
  conn.commit()