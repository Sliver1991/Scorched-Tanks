import pygame,init, mapDraw, colors,tanks

clock = pygame.time.Clock()
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                  game = False
                  
    init.surface.fill(colors.BLACK)
    mapDraw.gameFrame()
    mapDraw.drawMap()
    for team in tanks.tanks:
        for tank in team:
            tanks.drawTank(tank)
    pygame.transform.scale(init.surface, (init.screen[0], init.screen[1]))
    init.gameDisplay.blit(init.surface, (0, 0))
    pygame.display.update()
    
    clock.tick(60)

#print(init.gameMap)
pygame.quit()