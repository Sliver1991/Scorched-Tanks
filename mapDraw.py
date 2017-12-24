import init,draw,colors

def drawMap():
    draw.drawPoly(colors.BROWN,init.gameMap)

def gameFrame():
    draw.drawSquare(init.gameSize['x'],init.gameSize['y'],init.gameSize['width']-init.gameSize['x'],init.gameSize['height']-init.gameSize['y'],colors.WHITE)
    draw.drawSquare(100,150,100,150,colors.WHITE)