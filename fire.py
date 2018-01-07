import equ,tanks,init,draw,colors,pygame,text,math

rules = init.rules

def fire(tank,eq,angle,power=None):
    """Handles Fire mechanism,
    tank - active player firing
    eq - function handling the firing equation
    angle - angle of firing
    power - power of firing"""
    init_x, init_y = tank['x'], tank['y']
    x, y, t = 0, 0, 0
    while tanks.tankHit(x+init_x,init_y-y,tank):
        t+=1
        if eq.__name__ != 'crazy':
            x,y=equ.linear(angle,-1,t)
        else:
            x,y=equ.linear(0,-1,t)
#        draw.drawPixel(x+init_x,init_y-y,colors.RED1)
    init_x, init_y  = init_x+x, init_y-y
    line = (init_x, init_y)
    t = 0
    while not tanks.hitAnyTank(x+init_x,init_y-y)  and init.gameSize['x']<x+init_x<init.gameSize["width"] and -500<init_y-y<tanks.findHeight(x+init_x) :
        t+=1
        x,y=eq(angle,power,t)
        line = line[-2:]+(init_x+x,init_y-y)
        if init.gameSize['x']<line[0]<init.gameSize['x']+init.gameSize['width'] \
            and init.gameSize['y']<line[1]: 
                draw.drawLine(*line,2,colors.RED1)
        pygame.transform.scale(init.surface, (init.res["width"],init.res["height"])) 
        init.gameDisplay.blit(init.surface, (0, 0))
        pygame.display.update()
    
        init.clock.tick(60)
    flag, deathCount = tanks.tanksDamaged(x+init_x,init_y-y)
    if tank['dead']==True:
        deathCount-=2
    tank["kills"]+=deathCount
    damageMap(x+init_x,init_y-y)
    i=0
    
    while i<init.rules['radius']:
        i+=init.rules['radius']//30
        draw.drawCircle(int(x+init_x),int(init_y-y),i,colors.RED4)
        pygame.transform.scale(init.surface, (init.res["width"],init.res["height"])) 
        init.gameDisplay.blit(init.surface, (0, 0))
        pygame.display.update()
        init.clock.tick(60)
        
    if not flag:
        text.message_display("Missed!",30,colors.RED1,tank['x'],tank['y']-80)
    
    pygame.transform.scale(init.surface, (init.res["width"],init.res["height"])) 
    init.gameDisplay.blit(init.surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(1000)

def updateHeight(hit_x,hit_y,x):
    """Function updates the height at x coord in map according to hit spot"""
    loc = [x,tanks.findHeight(x)]
    y = loc[1]
    index = init.gameMap.index(loc,1)
    b,c = hit_x-x,init.rules['radius']
    a = int(math.sqrt(c**2-b**2))
    destUpper, destLower = hit_y-a, hit_y+a
    if y<destUpper:
        init.gameMap[index][1]+=2*a
    elif y<destLower:
        init.gameMap[index][1]+=(destLower-y)
    if init.gameMap[index][1]>init.gameSize['height']-50:
        init.gameMap[index][1]=init.gameSize['height']-50
        
def damageMap(hit_x,hit_y):
    for x in range(max(init.gameSize['x'],hit_x-init.rules['radius']),min(init.gameSize['width'],hit_x+init.rules['radius'])):
        updateHeight(hit_x,hit_y,x)
    for team in tanks.tanks:
        for tank in team:
            tank["y"]=tanks.findHeight(tank["x"])-50