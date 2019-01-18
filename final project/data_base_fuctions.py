import sqlite3 as sq


def dataBase_in(playerID=str, game=str, score=int):

    db = sq.connect('Game_Username_and_Scores.db')
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS game_data(username, game, score)")
    c.execute("INSERT INTO game_data(username, game, score)VALUES(:username, :game, :score)",
            {'username':playerID, 'game':game, 'score':score })
    db.commit()


class Give_Highscores():
        game = str
        def __init__(self,game):
                self.game = game       
        
        def give_name(self,game):
                self.game = game
                try:
                        db = sq.connect('Game_Username_and_Scores.db')
                        c = db.cursor()
                        c.execute("SELECT * FROM game_data WHERE game= '%s' order by score desc limit 1"% self.game)
                        return (c.fetchone()[0]) 
                except:
                        pass
        
        def give_score(self,game):
                self.game = game
                try:
                        db = sq.connect('Game_Username_and_Scores.db')
                        c = db.cursor()
                        c.execute("SELECT * FROM game_data WHERE game= '%s' order by score desc limit 1"%self.game)
                        return  (c.fetchone()[2]) 
                except:
                        pass



