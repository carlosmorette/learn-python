import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def create_table():
    conn.execute("""CREATE TABLE Pessoas(
        ID_pessoas INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Nome VARCHAR(100) NOT NULL,
        Email VARCHAR NOT NULL,
        Senha VARCHAR NOT NULL);""")
    conn.commit()
    # conn.close()


def insert_table():
    conn.execute(
        """INSERT INTO Pessoas VALUES (NULL, "Carlos", "carlos.email@outlook.com", "senha123")""")
    conn.commit()
    # conn.close()


def list_table():
    conn.execute("SELECT * FROM Pessoas")
    print(cursor.fetchall())
