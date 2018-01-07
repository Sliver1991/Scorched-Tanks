import init,draw,colors

def drawMap():
    draw.drawPoly(colors.BROWN,init.gameMap)

def gameFrame():
    draw.drawImage(init.sky,init.gameSize['x'],init.gameSize['y'], True,init.gameSize['width']-init.gameSize['x'],init.gameSize['height']-init.gameSize['y'])