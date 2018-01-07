import pygame, init, os, text, colors

def tankSelect(player):
    files = list(f for f in os.listdir('.'+os.sep+'assets'+os.sep+'tanks') if os.path.isfile(os.path.join('.'+os.sep+'assets'+os.sep+'tanks',f)))
    i=0
    pick = -1
    status = True
    
    def dec():
        nonlocal i
        if i>0:
            i-=1
            
    def inc():
        nonlocal i
        if i+5<len(files):
            i+=1
            
    def clicked(i):
        nonlocal pick, status
        pick = i
        status = False
    
    while status:
        init.surface.fill(colors.BLACK)
        text.message_display("{} Select Tank".format(player['name']),50,colors.WHITE,init.screen[0]//2,100)
        images = [pygame.image.load('.'+os.sep+'assets'+os.sep+'tanks'+os.sep+file) for file in files[i:i+5]]
        
        for t in range(len(images)):
            clickableImage(images[t],300+150*t,400, lambda: clicked(t))
        
        text.button("<",400,600,50,50,colors.WHITE,40,colors.BLACK,colors.GREEN,dec)
        text.button(">",500,600,50,50,colors.WHITE,40,colors.BLACK,colors.GREEN,inc)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        
        pygame.transform.scale(init.surface, (init.res["width"],init.res["height"])) 
        init.gameDisplay.blit(init.surface, (0, 0))
        pygame.display.update()
        
        init.clock.tick(60)
    player['tank']=images[pick]

def clickableImage(image,x,y, action=None):
    w,h = image.get_size()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    init.surface.blit(image,(x,y))
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()
            pygame.time.delay(200)
