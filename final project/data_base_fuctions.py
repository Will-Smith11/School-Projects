import sqlite3 as sq
from Final_Project import username

game = 'snake'
best_score = 4

def dataBase_in():

    db = sq.connect('Game_Username_and_HighScores.db')
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS game_high_scores(username, game, best_score)")
    c.execute("INSERT INTO game_high_scores(username, game, best_score)VALUES(:username, :game, :best_score)",
            {'username':username.return_username(), 'game':game, 'best_score':best_score })
    db.commit()

dataBase_in()