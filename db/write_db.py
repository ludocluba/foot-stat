import sqlite3

def write_player(id, surname, name, age, goal, win, loss):
    conn = sqlite3.connect('../data/player.db')
    sql = "INSERT INTO PLAYER (ID,SURNAME,LASTNAME,AGE,GOAL,WIN,LOSS) \
      VALUES (%d,'%s','%s', %d, %d, %d, %d) " % (id, surname, name, age, goal, win, loss)
    conn.execute(sql)
    conn.commit()

def add_goal(id):
    conn = sqlite3.connect('../data/player.db')
    sql = "UPDATE PLAYER SET GOAL = GOAL + 1 WHERE ID = %d;" % id
    conn.execute(sql)
    conn.commit()

def add_win(id, win):
    conn = sqlite3.connect('../data/player.db')
    sql = "UPDATE PLAYER SET WIN = WIN + 1 WHERE ID = %d;" % id
    conn.execute(sql)
    conn.commit()

if __name__ == "__main__":
    #write_player(0, "ludo", "drouineau", 43, 0, 0, 0)
    write_player(1, "gael", "billant", 28, 0, 0, 0)