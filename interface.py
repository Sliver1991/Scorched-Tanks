import init,text,colors,saveLoad, tanks,equ,draw, player, pygame, os

def drawInterface(test=False):
    if test:
        return test
    text.message_display("Firing Mode:",50,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+70,init.gameSize["y"]+450)
    text.button("Linear",init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+510,100,30,linear,30,colors.GRAY,colors.RED1,toLinear)
    text.button("Ballistic",init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+560,100,30,ballistic,30,colors.GRAY,colors.RED1,toBallistic)
    text.button("Guided",init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+610,100,30,guided,30,colors.GRAY,colors.RED1, toGuided)
    text.button("Crazy",init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+660,100,30,crazy,30,colors.GRAY,colors.RED1, toCrazy)
    text.button("Save",init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+860,100,30,colors.BLACK,30,colors.GRAY,colors.RED1, saveLoad.allSaves)
    text.button("-",init.gameSize["width"]+20,init.gameSize["y"]+80,25,30,colors.WHITE,25,colors.BLACK,colors.RED1, decPwr,0)
    text.button("+",init.gameSize["width"]+259,init.gameSize["y"]+80,25,30,colors.WHITE,25,colors.BLACK,colors.RED1, incPwr,0)
    text.button("+",init.gameSize["width"]+140,init.gameSize["y"]+230,25,30,colors.WHITE,25,colors.BLACK,colors.RED1, incAng,0)
    text.button("-",init.gameSize["width"]+140,init.gameSize["y"]+300,25,30,colors.WHITE,25,colors.BLACK,colors.RED1, decAng,0)
    text.message_display("Wind:",40,colors.GRAY,init.gameSize['x']+100,init.gameSize['height']+50)
    
def drawStats(p,a,n,test=False):
    if test:
        return test
    text.message_display("Power:",50,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+40)
    drawPwr(p)
    text.message_display(str(p),30,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+10,init.gameSize["y"]+130)
    text.message_display("Angle:",50,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+200)
    drawAngle(a)
    text.message_display(str(a),30,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+120,init.gameSize["y"]+300)
    text.message_display(n["player"]+"'s turn",50,colors.RED1,(init.gameSize["x"]+init.gameSize["width"])/2,init.gameSize["y"]+50)
    tanks.drawCurr(n)
    wind = init.rules["wind"]
    if wind>0:
        direction = "right"
    elif wind<0:
        direction = "left"
        wind*=-1
    else:
        direction = None
    wind = wind//20+1
    for i in range(wind):
        if direction=="right":
            draw.drawRightArrow(colors.GREEN,init.gameSize['x']+100+i*15,init.gameSize['height']+100)
        elif direction=='left':
            draw.drawLeftArrow(colors.GREEN,init.gameSize['x']+100-i*15,init.gameSize['height']+100)
        else:
            draw.drawCircle(init.gameSize['x']+100,init.gameSize['height']+100,30,colors.WHITE)
            draw.drawCircle(init.gameSize['x']+100,init.gameSize['height']+100,25,colors.BLACK)
            
def drawPwr(p):
    x = init.gameSize["width"]+50
    y = init.gameSize["y"]+80
    draw.drawSquare(x,y,204,30,colors.RED1)
    draw.drawSquare(x+1,y+1,p*2,28,colors.GREEN)
    
def incPwr():
    if player.power<100:
        player.power+=1
    
def decPwr():
    if player.power>0:
        player.power-=1   
        
def drawAngle(a):
    angle =  pygame.image.load("." +os.sep+"assets"+os.sep+"angle.png")
    init.surface.blit(angle, (init.gameSize["width"]+30,init.gameSize["y"]+230))
    x1,y1 = init.gameSize["width"]+80,init.gameSize["y"]+280
    x2,y2 = equ.linear(a,-1,7)
    x2+=x1
    y2 = y1-y2
    draw.drawLine(x1,y1,x2,y2,3,colors.BLUE)
    
def incAng():
    if player.angle<200:
        player.angle+=1
    
def decAng():
    if player.angle>-20:
        player.angle-=1 
    
attack = equ.linear
on = colors.RED1
off = colors.BLACK
linear = on
ballistic = off
guided = off
crazy = off
def allOff():
    global linear,ballistic,guided,crazy
    linear=ballistic=guided=crazy=off

def toLinear():
    global attack,linear
    attack = equ.linear
    allOff()
    linear = on
    
def toBallistic():
    global attack,ballistic
    allOff()
    attack = equ.ballistic
    ballistic = on
    
def toGuided():
    global attack, guided
    allOff()
    attack = equ.guided
    guided = on
    
def toCrazy():
    global attack, crazy
    allOff()
    attack = equ.crazy
    crazy = on