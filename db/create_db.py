import sqlite3

def create_table():
    conn = sqlite3.connect('../data/player.db')

    sql = "CREATE TABLE PLAYER (ID INT PRIMARY KEY     NOT NULL, \
             SURNAME           TEXT    NOT NULL, \
             LASTNAME           TEXT    NOT NULL, \
             AGE            INT     NOT NULL, \
             GOAL        INT, \
             WIN         INT, \
             LOSS        INT);"
    conn.execute(sql)

if __name__ == "__main__":
    create_table()