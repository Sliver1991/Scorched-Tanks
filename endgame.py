import tanks, text,colors, init,pygame, draw, leader

def testEndGame():
    living = list()
    for team in tanks.tanks:
        living.append(False)
        for tank in team:
            if tank['health']>0:
                living[-1]=True
    return living

def endGame():
    living = testEndGame()
    if living.count(True)<=1:
        status = True
        report = {}
        report['players'] = []
        messages = []
        if True in living:
            living = living.index(True)
        else:
            living = None
        for team in tanks.tanks:
            for tank in team:
                temp = tankReport(tank,living)
                messages.append(temp[0])
                report['players'].append({
                        'name':temp[1],
                        'kills':temp[2],
                        'death':temp[3],
                        'victor':temp[4]})
        leader.updateLeaders(report)                
        while status:
            draw.drawSquare(200,150,init.screen[0]-400,init.screen[1]-300,colors.BLACK)
            text.message_display("GAME OVER",40,colors.RED2,(init.gameSize["x"]+init.gameSize["width"])/2,200)
            if living is not None:
                text.message_display("Team {} Won!".format(living+1),40,colors.RED2,init.gameSize["width"]//2,300)
            else:
                text.message_display("As in war, there are no winners",40,colors.RED2,init.gameSize["width"]//2,300)
            
            for i in range(len(messages)):
                text.message_display(messages[i],30,colors.WHITE,init.gameSize["width"]//2,400+i*50)
            
            pygame.transform.scale(init.surface, (init.res["width"],init.res["height"])) 
            init.gameDisplay.blit(init.surface, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        status = False
            
            pygame.transform.scale(init.surface, (init.res["width"],init.res["height"])) 
            init.gameDisplay.blit(init.surface, (0, 0))
            pygame.display.update()
            
            init.clock.tick(60)
        return True
    return False

def tankReport(tank,victor):
    if victor is not None:
        if tank in tanks.tanks[victor]:
            victor=True
        else:
            victor=False
    return "Player: {}. Kills: {}   {} and {}".format(tank['player'],tank['kills'],"died" if tank['dead'] else "lived","won" if victor else "lost"),tank['player'],tank['kills'],tank['dead'],victor 

#def updateLeaderboards():
    