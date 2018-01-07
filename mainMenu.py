import text,init,colors,pygame

game = 'menu'

def menu():
    global game
    while game=='menu':
        init.surface.fill(colors.BLACK)
        	
        text.button("Start Game" , 650 , 100 , 550 , 100, colors.BLACK , 80 , colors.GRAY , colors.GREEN, newGame)
        text.button("Load Game" , 650 , 300 , 550 , 100 , colors.BLACK , 80 , colors.GRAY , colors.GREEN, loadGame)
        text.button("Leaderboards" , 650 , 500 , 550 , 100 , colors.BLACK , 80 , colors.GRAY , colors.GREEN,leaderboard)
        text.button("Exit",650,700,550,100,colors.BLACK,80,colors.GRAY,colors.RED1, exitGame)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game = False
        
        pygame.transform.scale(init.surface, (init.res["width"],init.res["height"])) 
        init.gameDisplay.blit(init.surface, (0, 0))
        pygame.display.update()
        init.clock.tick(60)
	
def exitGame():
    global game
    game = False

def leaderboard():
    global game
    game = 'leader'
    
def newGame():
    global game
    game = 'new'
    
def loadGame():
    global game
    game = 'load'