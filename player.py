import tanks, interface, init, random

turn = 0
active = None
power = 0
angle = 0
movesLeft = 5

def nextPlayer():
    global turn,power,angle, movesLeft, active
    
    if init.rules['wind change']:
        init.rules['wind']=random.randint(init.rules['wind low'],init.rules['wind high'])
        
    turn+=1
    if turn>tanks.players:
        turn = 1
    power = 0
    angle = 0
    movesLeft = 5
    interface.toLinear()
    def activePlayer():
        for team in tanks.tanks:
            for tank in team:
                if tank["turn"]==turn:
                    return tank
                
    active = activePlayer()
    if active['dead']:
        nextPlayer()