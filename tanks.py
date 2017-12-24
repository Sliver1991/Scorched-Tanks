import init, pygame

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
        t.append({"player":p,"turn":i, "health":init.rules["health"]})
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
    hit = []
    for tank in tankPos:
        if tank[1]-50<x<tank[1]+50 and tank[2]-50<y<tank[2]+50:
            hit.append(tank[0])
    if len(hit)==0:
        return None
    else:
        return hit

def drawTank(tank,angle=15):
    if angle<90:
        init.surface.blit(pygame.image.load(theme[tank["turn"]-1]+".png"), (tank['x'],tank['y']-100))
    else:
        init.surface.blit(pygame.image.load(theme[tank["turn"]-1]+"mirror.png"), (tank['x'],tank['y']-100))

def checkEnd():
    players = []
    for team in teams:
        t = []
        for tank in team:
            if tank["health"]>0:
                t.append(tank)
        players.append(t)
    if len(players)==0:
        return True
    return False
    
    
