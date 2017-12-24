import pygame,init, mapDraw, colors

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
    #pygame.transform.scale(init.surface, (init.screen[0] / init.res["width"], init.screen[1] / init.res["height"]), DestSurface=init.surface)
    init.gameDisplay.blit(init.surface, (0, 0))
    pygame.display.update()
    
    clock.tick(60)

pygame.quit()