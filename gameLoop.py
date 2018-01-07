import pygame,init, mapDraw, draw,tanks, leaderboard
import interface,player,fire, endgame,mainMenu,saveLoad, newGame, houseRules, mapGen

def gameLoop():
    """Game LOOOOOOP"""
    global game            
    while game:
        active = player.active
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game = False
                
                if event.key == pygame.K_UP:
                    player.power += 5
                    if player.power>100:
                        player.power=100
                    
                if event.key == pygame.K_DOWN:
                    player.power -= 5
                    if player.power<0:
                        player.power=0
                    
                if event.key == pygame.K_LEFT:
                    player.angle -= 5 
                    if player.angle<-20:
                        player.angle = -20
                        
                if event.key == pygame.K_RIGHT:
                    player.angle += 5
                    if player.angle > 200:
                        player.angle = 200
                        
                if event.key == pygame.K_p:
                    player.nextPlayer()
                    
                if event.key == pygame.K_d:
                    if player.movesLeft>0 and active["x"]+60<init.gameSize["width"] \
                    and not tanks.hitAnyTank(active["x"]+60,tanks.findHeight(active["x"]+60)-50):
                        player.movesLeft-=1
                        active["x"]+=10
                        active["y"]=tanks.findHeight(active["x"])-50
                  
                if event.key == pygame.K_a:
                    if player.movesLeft>0 and active["x"]-60>init.gameSize["x"] \
                    and not tanks.hitAnyTank(active["x"]-60,tanks.findHeight(active["x"]-60)-50):
                        player.movesLeft-=1
                        active["x"]-=10
                        active["y"]=tanks.findHeight(active["x"])-50
                
                if event.key ==pygame.K_SPACE:
                    fire.fire(active,interface.attack,player.angle,player.power)
                    if endgame.endGame():
                        game=False
                    else:
                        player.nextPlayer()
                  
        
            
        draw.drawImage(init.bg,0,0,True)
        mapDraw.gameFrame()
        mapDraw.drawMap()
        for team in tanks.tanks:
            for tank in team:
                if tank==active:
                    tanks.drawTank(tank,player.angle)
                else:
                    if not tank['dead']:
                        tanks.drawTank(tank)
                
        interface.drawInterface()
        interface.drawStats(player.power,player.angle,player.active)
        pygame.transform.scale(init.surface, (init.res["width"],init.res["height"])) 
        init.gameDisplay.blit(init.surface, (0, 0))
        pygame.display.update()
        
        init.clock.tick(60)

def gameCycle():
    mainMenu.menu()
    global game
    if mainMenu.game == 'new':
        game = True
        status = newGame.playersInput()
        if status=="quit":
            mainMenu.game = "menu"
            gameCycle()
            return
        rules = houseRules.rulesMenu()
        if rules == "quit":
            mainMenu.game = "menu"
            gameCycle()
            return
        init.gameMap = mapGen.mapGen()
        tanks.genTanks()
        player.turn = 0
        player.nextPlayer()
        gameLoop()
        mainMenu.game = "menu"
        gameCycle()
    elif mainMenu.game == 'load':
        saveLoad.allLoad()
        game = True
        gameLoop()
        mainMenu.game = "menu"
        gameCycle()
    elif mainMenu.game == 'leader':
        leaderboard.leaderboard()
        game = False
        mainMenu.game = "menu"
        gameCycle()
        
gameCycle()
pygame.quit()