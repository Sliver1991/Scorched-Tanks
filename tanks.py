import draw, init, colors

def findHeight(x):
    for pos_x,pos_y in init.gameMap:
        if pos_x == x:
            return pos_y
        
tanks = []
teams = [["Slava"],["Daniel","Mathias"]]
i=1
for team in teams:
    t = []
    for player in team:
        t.append({"player":player,"turn":i})
        i+=1
    tanks.append(t)

for team in tanks:
    for tank in team:
        tank["x"]=tank["turn"]*300
        tank["y"]=findHeight(tank["x"])
        
players = i

def drawTank(tank):
    draw.drawCircle(tank["x"],tank["y"]-50,15,colors.BLUE)
    draw.drawSquare(tank["x"]-25,tank["y"]-50,50,50,colors.AQUA)
    
