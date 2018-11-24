import sqlite3 as sq
from Final_Project import screen_pw, screen_us


def dataBase_in():

    db = sq.connect('Game_Username_and_Password.db')
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS player_data(username, password)")
    c.execute("INSERT INTO player_data(username, password)VALUES(:username, :password)",
            {'username':screen_us.return_username(),'password':screen_pw.return_password()})
    db.commit()