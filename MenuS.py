# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import text,init,colors,pygame,time
clock = pygame.time.Clock()
while True:
    init.surface.fill(colors.BLACK)
    	
    text.button("Start Game" , 650 , 100 , 550 , 100, colors.BLACK , 80 , colors.GRAY , colors.RED1)
    text.button("Load Game" , 650 , 300 , 550 , 100 , colors.BLACK , 80 , colors.GRAY , colors.RED1)
    text.button("Leaderboards" , 650 , 500 , 550 , 100 , colors.BLACK , 80 , colors.GRAY , colors.RED1)
    text.button("Exit",650,700,550,100,colors.BLACK,80,colors.GRAY,colors.RED1)
    
    pygame.transform.scale(init.surface, (init.screen[0], init.screen[1]))
    init.gameDisplay.blit(init.surface, (0, 0))
    pygame.display.update()
    clock.tick(60)
	
