import equ,tanks, init,draw,colors,text,time,pygame

rules = init.rules

def fire(posx,posy,eq,angle,power=None):
    x = 1
    y = int(nexty(eq,x,angle,power))
    x,y = equ.coordinatefixer(x,y)
    print(posx,posy,x,y)
    traj = []
    while y>tanks.findHeight(x+posx) and tanks.tankHit(x+posx,y+posy)==None and x+posx<init.gameSize["width"]+init.gameSize["x"]: 
        traj.append((x,y))
        x+=1
        y = int(nexty(eq,x,angle,power))
        x,y = equ.coordinatefixer(x,y)
        draw.drawPixel(x+posx,y+posy,colors.BLACK)
        
    hitlist = []
    
    for xrad in range(x+(-1)*init.rules["radius"]//2,x+init.rules["radius"]//2):
        hit = tanks.tankHit(xrad,tanks.findHeight(xrad))
        if hit!=None:
            for tank in hit:
                if tank not in hitlist:
                    damage = rules["damage"]*(1-equ.distance(xrad,tanks.findHeight(xrad),tank['x'],tank['y'])/rules["radius"])
                    tank["health"]-=damage
                    text.message_display(str(damage),30,colors.RED1,tank['x'],tank['y']-90)
                    hitlist.append(tank)
    if len(hitlist)==0:
        text.message_display("MISSED",50,colors.RED1,(init.gameSize["x"]+init.gameSize["width"])/2,init.gameSize["y"]+200)
    pygame.transform.scale(init.surface, (init.screen[0], init.screen[1]))
    init.gameDisplay.blit(init.surface, (0, 0))
    pygame.display.update()
    time.sleep(1)
                    
    
def nexty(eq,x,angle,power=None):
    if eq == 'linear':
        y=equ.linear(angle,x)
    elif eq == 'ballistic':
        y=equ.ballistic(angle,power,x)
    elif eq == 'guided':
        y=equ.guided(angle,power,x)
    elif eq== 'crazy':
        y=equ.crazy(angle,power,x)
    return y