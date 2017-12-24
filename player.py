import tanks
turn = 0
active = None
def nextPlayer():
    global turn,power,angle, movesLeft, active
    turn+=1
    if turn>tanks.players:
        turn = 1
    power = 0
    angle = 0
    movesLeft = 5
    def activePlayer():
        for team in tanks.tanks:
            for tank in team:
                if tank["turn"]==turn:
                    return tank
                
    active = activePlayer()