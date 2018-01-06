import init, pygame, equ,colors,text, draw, random

def findHeight(x):
    """Finds terrain height in given value of x"""
    for pos_x,pos_y in init.gameMap[1:-1]:
        if pos_x == x:
            return pos_y
tanks = []
teams = []
players = 0

def turnOrder(playerCount):
    turn = list(range(1,players+1))
    random.shuffle(turn)
    return turn

def orderPlayers():
    i=0
    turn = turnOrder(players)
    for team in tanks:
        for tank in team:
            tank['turn']=turn[i]
            i+=1
            
def genPos(tank):
    x = random.randint(init.gameSize["x"]+60,init.gameSize['width']-60)
    y = findHeight(x)-50
    if hitAnyTank(x,y) or hitAnyTank(x-50,findHeight(x-50)-50) or hitAnyTank(x+50,findHeight(x+50)-50):
        genPos(tank)
    else:
        tank['x']=x
        tank['y']=y
            
def genTanks():        
    global tanks
    tanks = []
    for team in teams:
        t = []
        for p in team:
            t.append({"player":p[0], "tank":p[1], "health":init.rules["health"], "dead":False, "kills":0, "x":-1000, "y":-1000})
        tanks.append(t)
    orderPlayers()
    for team in tanks:
        for tank in team:
            genPos(tank)

#    tankPos = []
#    for team in tanks:
#        for tank in team:
#            tank["x"]=tank["turn"]*300
#            tank["y"]=findHeight(tank["x"])-50
#            tankPos.append([tank,tank["x"],tank["y"]])

def tanksDamaged(x,y):
    """Handles damaging mechanism. Using the blast center, updates HP of all damaged tanks.
    Returns true if any tank is damaged, false otherwise"""
    flag = False
    deathCount = 0
    for team in tanks:
        for tank in team:
            if not tank['dead']:
                damage = int(init.rules['damage']*tankDamage(x,y,tank))
                if damage>0:
                    text.message_display(str(damage),30,colors.RED1,tank['x'],tank['y']-80)
                    if updateHP(tank,damage):
                        deathCount+=1
                    flag = True
    return flag,deathCount

def updateHP(tank,damage):
    """Updates HP of damaged tank. If tank is destroyed, updates stat and moves to graveyard"""
    tank['health']=max(tank['health']-damage,0)
    if tank['health']==0:
        tank['dead']=True
        return True
    return False

def tankDamage(x,y, tank):
    """Returns how close a tank is to the blast center in relation to radius"""
    dist = max(equ.distance(tank['x'],tank['y'],x,y)-50,0)
    if dist<init.rules['radius']:
        return 1-(dist/init.rules['radius'])
    else:
        return 0
    
def hitAnyTank(x,y):
    """Returns true if any tank is located at x,y"""
    for team in tanks:
        for tank in team:
            if tankHit(x,y,tank):
                return True
    return False
    
def tankHit(x,y,tank):
    """Returns true if tank is located at x,y"""
    return tank['x']-50<=x<=tank['x']+50 and tank['y']-50<=y<=tank['y']+50 and not tank['dead']

def drawTank(tank,angle=15):
    """Draws tank to map"""
    if tank['dead']:
        return
    drawHP(tank)
    image = tank['tank']
    if angle>90:
        image = pygame.transform.flip(image,True,False)    
    init.surface.blit(image, (tank['x']-50,tank['y']-50))
    
def drawHP(tank):
    x = tank['x']-50
    y = tank['y']-70
    hp = int(tank['health']/init.rules['health']*98)
    draw.drawSquare(x,y,100,15,colors.RED1)
    draw.drawSquare(x+1,y+1,hp,13,colors.GREEN)
    
def drawCurr(tank):
    x = tank['x']
    y = tank['y']-80
    poly = [(x,y),(x+45,y-20),(x+20,y-20),(x+20,y-50),(x-20,y-50),(x-20,y-20),(x-45,y-20)]
    draw.drawPoly(colors.GREEN,poly)