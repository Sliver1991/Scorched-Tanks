import pygame,init, mapDraw, colors,tanks, interface, player


clock = pygame.time.Clock()
game = True

player.nextPlayer()


            
while game:
    active = player.active
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False
            
            if event.key == pygame.K_UP:
                if player.power<100:
                    player.power += 5
                
            if event.key == pygame.K_DOWN:
                if player.power>0:
                    player.power -= 5
                
            if event.key == pygame.K_LEFT:
                if player.angle>-20:
                    player.angle -= 5
                if player.angle==90:
                    player.angle==85    
            
            if event.key == pygame.K_RIGHT:
                if player.angle < 200:
                    player.angle += 5
                if player.angle==90:
                    player.angle==95
                    
            if event.key == pygame.K_p:
                player.nextPlayer()
                
            if event.key == pygame.K_d:
                if player.movesLeft>0 and active["x"]>init.gameSize["x"]:
                    player.movesLeft-=1
                    active["x"]+=10
                    active["y"]=tanks.findHeight(active["x"])
              
            if event.key == pygame.K_a:
                if player.movesLeft>0 and active["x"]<init.gameSize["width"]:
                    player.movesLeft-=1
                    active["x"]-=10
                    active["y"]=tanks.findHeight(active["x"])
        
              
    init.surface.fill(colors.BLACK)
    mapDraw.gameFrame()
    mapDraw.drawMap()
    for team in tanks.tanks:
        for tank in team:
            if tank==active:
                tanks.drawTank(tank,player.angle)
            else:
                tanks.drawTank(tank)
            
    interface.drawInterface()
    interface.drawStats(player.power,player.angle,player.active["player"])
    pygame.transform.scale(init.surface, (init.screen[0], init.screen[1]))
    init.gameDisplay.blit(init.surface, (0, 0))
    pygame.display.update()
    
    clock.tick(60)

#print(init.gameMap)
pygame.quit()

