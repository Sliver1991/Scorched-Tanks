import init,text,colors,player

def drawInterface():
    text.message_display("Power:",50,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+40)
    text.message_display("Angle:",50,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+200)
    text.message_display("Firing Mode:",50,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+70,init.gameSize["y"]+450)
    text.button("Linear",init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+510,100,30,colors.BLACK,30,colors.GRAY,colors.RED1)
    text.button("Ballistic",init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+560,100,30,colors.BLACK,30,colors.GRAY,colors.RED1)
    text.button("Guided",init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+610,100,30,colors.BLACK,30,colors.GRAY,colors.RED1)
    text.button("Crazy",init.gameSize["x"]+init.gameSize["width"]+30,init.gameSize["y"]+660,100,30,colors.BLACK,30,colors.GRAY,colors.RED1)
    
    text.button("Pass",init.gameSize["x"]+init.gameSize["width"]-20,init.gameSize["y"]+800,200,100,colors.BLACK,60,colors.RED1,colors.RED2,player.nextPlayer)
def drawStats(p,a):
    text.message_display(str(p),30,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+10,init.gameSize["y"]+100)
    text.message_display(str(a),30,colors.RED1,init.gameSize["x"]+init.gameSize["width"]+10,init.gameSize["y"]+300)
    

        