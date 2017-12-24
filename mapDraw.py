import init,draw,colors

def drawMap():
    draw.drawPoly(colors.BEIGE,init.gameMap)

def gameFrame():
    draw.drawSquare(init.gameSize['x'],init.gameSize['y'],init.gameSize['width'],init.gameSize['height'],colors.PINK)