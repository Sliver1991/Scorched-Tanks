import shelve, init, tanks, player, textInput, os, draw, text, colors,pygame

status = True

def save(file=""):
    """Saves data into file with name used from textInput.textbox"""
    global status
    if file=="":
        file = textInput.textBox("Enter Save Name")
    db = shelve.open(".\\saves\\"+file)
    db['rules'] = init.rules
    db['tanks'] = tanks.tanks
    db['map'] = init.gameMap
    db['turn'] = player.turn
    db['active'] = player.active
    db['moves'] = player.movesLeft
    status = False
    db.close()
    
def load(file):
    """Loads data from file with name used from textInput.textbox"""
    global status
    db = shelve.open(".\\saves\\"+file)
    init.rules = db['rules']
    tanks.tanks = db['tanks']
    init.gameMap = db['map']
    player.turn = db['turn']
    player.active = db['active']
    player.movesLeft = db['moves']
    status = False
    db.close()
    
def allLoad():
    files = list(set(f[:-4] for f in os.listdir('.\\saves\\') if os.path.isfile(os.path.join('.\\saves\\',f))))
    files.sort(key = lambda x:os.path.getmtime(os.path.join('.\\saves\\',x+".dat")),reverse=True )
    i=0
    global status
    status = True
    load1 = lambda: load(files[i])
    load2 = lambda: load(files[i+1])
    load3 = lambda: load(files[i+2])
    load4 = lambda: load(files[i+3])
    load5 = lambda: load(files[i+4])
    
    def inc():
        nonlocal i
        if i+5<len(files):
            i+=1
    
    def dec():
        nonlocal i
        if i>0:
            i-=1
    
    while status:
        draw.drawSquare(200,50,init.screen[0]-400,init.screen[1]-100,colors.BLACK)
        text.message_display("Load Game",60,colors.WHEAT,init.screen[0]//2,150)
        draw.drawSquare(350,340,init.screen[0]-700,400,colors.BLACK)
        text.message_display("Saves",40,colors.WHEAT,init.screen[0]//2,360)
        if len(files)>0:
            text.button(files[i],360,410,80,30,colors.WHITE,25,colors.BLACK,colors.BLUE,action=load1)
        if len(files)>1:
            text.button(files[i+1],360,450,80,30,colors.WHITE,25,colors.BLACK,colors.BLUE,action=load2)
        if len(files)>2:
            text.button(files[i+2],360,490,80,30,colors.WHITE,25,colors.BLACK,colors.BLUE,action=load3)
        if len(files)>3:
            text.button(files[i+3],360,540,80,30,colors.WHITE,25,colors.BLACK,colors.BLUE,action=load4)
        if len(files)>4:
            text.button(files[i+4],360,590,80,30,colors.WHITE,25,colors.BLACK,colors.BLUE,action=load5)
        text.button("up",550,410,60,30,colors.WHITE,25,colors.GRAY,colors.BLUE,action=dec)
        text.button("down",550,480,60,30,colors.WHITE,25,colors.GRAY,colors.BLUE,action=inc)
        
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    status = False
    
        pygame.transform.scale(init.surface, (init.screen[0], init.screen[1]))
        init.gameDisplay.blit(init.surface, (0, 0))
        pygame.display.update()
        init.clock.tick(60)        
            
    
def allSaves():
    files = list(set(f[:-4] for f in os.listdir('.\\saves\\') if os.path.isfile(os.path.join('.\\saves\\',f))))
    files.sort(key = lambda x:os.path.getmtime(os.path.join('.\\saves\\',x+".dat")),reverse=True )
    i=0
    global status
    status = True
    save1 = lambda: save(files[i])
    save2 = lambda: save(files[i+1])
    save3 = lambda: save(files[i+2])
    save4 = lambda: save(files[i+3])
    save5 = lambda: save(files[i+4])
    
    def inc():
        nonlocal i
        if i+5<len(files):
            i+=1
    
    def dec():
        nonlocal i
        if i>0:
            i-=1
        
    while status:
        draw.drawSquare(200,50,init.screen[0]-400,init.screen[1]-100,colors.BLACK)
        text.message_display("Save Game",60,colors.WHEAT,init.screen[0]//2,150)
        text.button("New Save",250,250,200,50,colors.WHITE,40,colors.GRAY,colors.BLUE,action=save)
        draw.drawSquare(350,340,init.screen[0]-700,400,colors.BLACK)
        text.message_display("Overwrite Saves",40,colors.WHEAT,init.screen[0]//2,360)
        if len(files)>0:
            text.button(files[i],360,410,80,30,colors.WHITE,25,colors.BLACK,colors.BLUE,action=save1)
        if len(files)>1:
            text.button(files[i+1],360,450,80,30,colors.WHITE,25,colors.BLACK,colors.BLUE,action=save2)
        if len(files)>2:
            text.button(files[i+2],360,490,80,30,colors.WHITE,25,colors.BLACK,colors.BLUE,action=save3)
        if len(files)>3:
            text.button(files[i+3],360,540,80,30,colors.WHITE,25,colors.BLACK,colors.BLUE,action=save4)
        if len(files)>4:
            text.button(files[i+4],360,590,80,30,colors.WHITE,25,colors.BLACK,colors.BLUE,action=save5)
        text.button("up",550,410,60,30,colors.WHITE,25,colors.GRAY,colors.BLUE,action=dec)
        text.button("down",550,480,60,30,colors.WHITE,25,colors.GRAY,colors.BLUE,action=inc)
        
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    status = False
    
        pygame.transform.scale(init.surface, (init.screen[0], init.screen[1]))
        init.gameDisplay.blit(init.surface, (0, 0))
        pygame.display.update()
        init.clock.tick(60)