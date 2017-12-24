import shelve, init, tanks, player

def save():
    db = shelve.open('save')
    db['rules'] = init.rules
    db['tanks'] = tanks.tanks
    db['map'] = init.gameMap
    db['turn'] = player.turn
    db.close()
    
def load():
    db = shelve.open()
    global rules, tanks, gameMap,turn
    rules = db['rules']
    tanks = db['tanks']
    gameMap = db['map']
    turn = db['turn']