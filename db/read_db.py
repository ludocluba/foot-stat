import sqlite3

def read_players():
    conn = sqlite3.connect('./data/player.db')

    sql = "SELECT * FROM PLAYER;"
    cursor = conn.cursor()

    cursor.execute(sql)
    return cursor.fetchall()