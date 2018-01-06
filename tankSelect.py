import pygame, init, os, text, colors

def tankSelect(player):
    files = list(f[:-4] for f in os.listdir('.'+os.sep+'assets'+os.sep+'tanks') if os.path.isfile(os.path.join('.'+os.sep+'assets'+os.sep+'tanks',f)))
    i=0
    status = True
    
    while status:
        init.surface.fill(colors.BLACK)
        text.message_display("{} Select Tank".format(player['name']),50,colors.WHITE,init.screen[0]//2,100)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
        
        pygame.transform.scale(init.surface, (init.screen[0], init.screen[1]))
        init.gameDisplay.blit(init.surface, (0, 0))
        pygame.display.update()
        
        init.clock.tick(60)
    return status