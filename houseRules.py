import init, text, colors, pygame, textInput, draw , time

def rulesMenu():
    
    def health():
        hp = textInput.textBox("Enter Starting Health",str(init.rules['health']))
        if hp=="":
            return
        try:
            hp = int(hp)
        except:
            health()
            return
        if hp<=0:
            health()
            return
        init.rules['health']=hp
        
    def radius():
        rad = textInput.textBox("Enter Blast Radius",str(init.rules['radius']))
        if rad=="":
            return
        try:
            rad = int(rad)
        except:
            radius()
            return
        if rad<=0:
            radius()
            return
        init.rules['radius']=rad
        
    def damage():
        dmg = textInput.textBox("Enter Blast Damage",str(init.rules['damage']))
        if dmg=="":
            return
        try:
            dmg = int(dmg)
        except:
            damage()
            return
        if dmg<=0:
            damage()
            return
        init.rules['damage']=dmg
        
    def gravity():
        grv = textInput.textBox("Enter Gravity (Normal Gravity is negative)",str(init.rules['gravity']))
        if grv=="":
            return
        try:
            grv = round(float(grv),2)
        except:
            gravity()
            return
        init.rules['gravity']=grv
        
    def windMode():
        
        def constant():
            init.rules['wind change']=False
            
        def changing():
            init.rules['wind change']=True
            
        def wind():
            wnd = textInput.textBox("Enter Constant Wind Value",str(init.rules['wind']))
            if wnd=="":
                return
            try:
                wnd = int(wnd)
            except:
                wind()
                return
            init.rules['wind']=min(max(wnd,-100),100)
            
        def windLow():
            wnd = textInput.textBox("Enter Low Wind Limit Value",str(init.rules['wind low']))
            if wnd=="":
                return
            try:
                wnd = int(wnd)
            except:
                windLow()
                return
            init.rules['wind low']=min(max(wnd,-100),100)
            windCheck()
            
        def windHigh():
            wnd = textInput.textBox("Enter High Wind Limit Value",str(init.rules['wind high']))
            if wnd=="":
                return
            try:
                wnd = int(wnd)
            except:
                windHigh()
                return
            init.rules['wind high']=min(max(wnd,-100),100)
            windCheck()
            
        def windCheck():
            if init.rules['wind change']==True:
                if init.rules['wind high']==init.rules['wind low']:
                    init.rules['wind change']=False
                    init.rules['wind']=init.rules['wind high']
                elif init.rules['wind high']<init.rules['wind low']:
                    init.rules['wind high'],init.rules['wind low'] = init.rules['wind low'],init.rules['wind high']
        
        
        state = True
        while state:
            change = init.rules['wind change']
            constColor = colors.GREEN if not change else colors.GRAY            
            changeColor = colors.GREEN if change else colors.GRAY
            draw.drawSquare(400,300,init.screen[0]-800,400,colors.BLACK)
            text.message_display("Choose Wind Mode",60,colors.WHITE,init.screen[0]//2,350)
            
            text.button("Constant",init.screen[0]//2-400,400,200,50,colors.BLACK,40,constColor,colors.GREEN,constant)
            text.button("Changing",init.screen[0]//2+200,400,200,50,colors.BLACK,40,changeColor,colors.GREEN,changing)
            
            if not change:
                text.button("Constant Wind: {}".format(init.rules['wind']),init.screen[0]//2-100,500,400,50,colors.BLACK,40,colors.WHITE,colors.GREEN,wind)
            
            else:
                text.button("Low Wind: {}".format(init.rules['wind low']),init.screen[0]//2-500,600,400,50,colors.BLACK,40,colors.WHITE,colors.GREEN,windLow)
                text.button("High Wind: {}".format(init.rules['wind high']),init.screen[0]//2+300,600,400,50,colors.BLACK,40,colors.WHITE,colors.GREEN,windHigh)
           
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        state = False
            
            pygame.transform.scale(init.surface, (init.screen[0], init.screen[1]))
            init.gameDisplay.blit(init.surface, (0, 0))
            pygame.display.update()
            
            init.clock.tick(60)
        
    
    def mapMode():
        
        def mixed():
            init.rules['map']='mixed'
            nonlocal state
            state = False
            
        def straight():
            init.rules['map']='straight'
            nonlocal state
            state = False
            
        def slope():
            init.rules['map']='round'
            nonlocal state
            state = False
        state = True
        while state:
            draw.drawSquare(400,300,init.screen[0]-800,400,colors.BLACK)
            text.message_display("Choose Map Generation Mode",60,colors.WHITE,init.screen[0]//2,350)
            
            text.button("mixed",init.screen[0]//2-500,400,200,50,colors.BLACK,40,colors.LIGHTGREY,colors.GREEN,mixed)
            text.button("straights",init.screen[0]//2-100,400,200,50,colors.BLACK,40,colors.LIGHTGREY,colors.GREEN,straight)
            text.button("slopes",init.screen[0]//2+300,400,200,50,colors.BLACK,40,colors.LIGHTGREY,colors.GREEN,slope)
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        state = False
            
            pygame.transform.scale(init.surface, (init.screen[0], init.screen[1]))
            init.gameDisplay.blit(init.surface, (0, 0))
            pygame.display.update()
            
            init.clock.tick(60)
        
        
    def done():
        nonlocal status
        status = "continue"
    
    status = "menu"
    while status=="menu":
        init.surface.fill(colors.BLACK)
        text.message_display("House Rules",50,colors.WHITE,init.screen[0]//2,100)
        
        text.button("Starting Health: {}".format(init.rules["health"]),500,250,init.screen[0]-1000,50,colors.BLACK,45,colors.WHITE,colors.GREEN, health)
        text.button("Blast Radius: {}".format(init.rules["radius"]),500,320,init.screen[0]-1000,50,colors.BLACK,45,colors.WHITE,colors.GREEN,radius)
        text.button("Blast Damage: {}".format(init.rules["damage"]),500,390,init.screen[0]-1000,50,colors.BLACK,45,colors.WHITE,colors.GREEN,damage)
        text.button("Gravity: {}".format(init.rules["gravity"]),500,460,init.screen[0]-1000,50,colors.BLACK,45,colors.WHITE,colors.GREEN,gravity)
        text.button("{} Wind".format("Changing" if init.rules['wind change'] else "Constant"),500,530,init.screen[0]-1000,50,colors.BLACK,45,colors.WHITE,colors.GREEN, windMode)
        text.button("Map Generating: {}".format(init.rules["map"]),500,600,init.screen[0]-1000,50,colors.BLACK,45,colors.WHITE,colors.GREEN,mapMode)
        
        text.button("Continue",init.screen[0]//2-200,800,400,70,colors.BLACK,60,colors.WHITE,colors.GREEN, done)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    status = "quit"
        
        pygame.transform.scale(init.surface, (init.screen[0], init.screen[1]))
        init.gameDisplay.blit(init.surface, (0, 0))
        pygame.display.update()
        
        init.clock.tick(60)
    
    return status