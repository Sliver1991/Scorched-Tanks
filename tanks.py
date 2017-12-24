import draw, init, colors, pygame

def findHeight(x):
    for pos_x,pos_y in init.gameMap:
        if pos_x == x:
            return pos_y
        
theme = ["bibitank","kimtank","putintank","trumptank"]
tanks = []
teams = [["Slava"],["Daniel","Matias"],["Nadin"]]
i=1
for team in teams:
    t = []
    for p in team:
        t.append({"player":p,"turn":i})
        i+=1
    tanks.append(t)

tankPos = []
for team in tanks:
    for tank in team:
        tank["x"]=tank["turn"]*300
        tank["y"]=findHeight(tank["x"])
        tankPos.append([tank,tank["x"],tank["y"]])
        
players = i-1

def tankHit(x,y):
    for tank in tankPos:
        if tank["x"]-50<x<tank["x"]+50 and tank["y"]-50<y<tank["y"]+50:
            return tank
    return None

def drawTank(tank,angle=15):
    if angle<90:
        init.surface.blit(pygame.image.load(theme[tank["turn"]-1]+".png"), (tank['x'],tank['y']-100))
    else:
        init.surface.blit(pygame.image.load(theme[tank["turn"]-1]+"mirror.png"), (tank['x'],tank['y']-100))
    #y = equ.linear(angle,20)
    #draw.drawLine(tank["x"],tank["y"]-60,tank["x"]+20,tank["y"]-y,5,colors.BLACK)
#    draw.drawCircle(tank["x"],tank["y"]-50,15,colors.BLUE)
#    draw.drawSquare(tank["x"]-25,tank["y"]-50,50,50,colors.AQUA)
    
    
    
    
    
