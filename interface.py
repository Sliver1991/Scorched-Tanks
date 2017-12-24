import init,text,colors,saveLoad

def drawInterface():
    text.message_display("Power:",50,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+40)
    text.message_display("Angle:",50,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+200)
    text.message_display("Firing Mode:",50,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+70,init.gameSize["y"]+450)
    text.button("Linear",init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+510,100,30,colors.BLACK,30,colors.GRAY,colors.RED1,toLinear)
    text.button("Ballistic",init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+560,100,30,colors.BLACK,30,colors.GRAY,colors.RED1,toBallistic)
    text.button("Guided",init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+610,100,30,colors.BLACK,30,colors.GRAY,colors.RED1, toGuided)
    text.button("Crazy",init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+660,100,30,colors.BLACK,30,colors.GRAY,colors.RED1, toCrazy)
    text.button("Save",init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+860,100,30,colors.BLACK,30,colors.GRAY,colors.RED1, saveLoad.save)

def drawStats(p,a,n):
    text.message_display(str(p),30,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+10,init.gameSize["y"]+100)
    text.message_display(str(a),30,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+10,init.gameSize["y"]+300)
    text.message_display(str(n)+"'s turn",50,colors.RED1,(init.gameSize["x"]+init.gameSize["width"])/2,init.gameSize["y"]+50)
    
attack = "linear"

def toLinear():
    global attack
    attack = "linear"
    
def toBallistic():
    global attack
    attack = "ballistic"
    
def toGuided():
    global attack
    attack = "guided"
    
def toCrazy():
    global attack
    attack = "crazy"
    
