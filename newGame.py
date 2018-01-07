import init, text, textInput, draw, colors, pygame, time, tanks, tankSelect, os

default = pygame.image.load("."+os.sep+"assets"+os.sep+"tanks"+os.sep+"bibitank.png")

def playersInput(test=False):
    if test:
        return test
    player1 = {"name":"Player1", "enabled":True,"team":1,"tank":default}
    player2 = {"name":"Player2", "enabled":True,"team":2,"tank":default}
    player3 = {"name":"", "enabled":False,"team":3,"tank":default}
    player4 = {"name":"", "enabled":False,"team":4,"tank":default}
    
    def check3():
        if player3['enabled']: 
            player3['name']=''
            if player4['enabled']:
                player4['enabled']=False
        player3['enabled']=not player3['enabled']
        time.sleep(0.1)
    
    def check4():
        if player4['enabled']: player4['name']=''
        player4['enabled']=not player4['enabled']
        time.sleep(0.1)
        
    def input1():
        name = textInput.textBox("Enter Player 1",player1['name'])
        if name!="":
            player1['name']=name
            
    def input2():
        name = textInput.textBox("Enter Player 2",player2['name'])
        if name!="":
            player2['name']=name
    
    def input3():
        if player3['enabled']:
            name = textInput.textBox("Enter Player 3",player3['name'])
            if name!="":
                player3['name']=name
            
    def input4():
        if player4['enabled']:
            name = textInput.textBox("Enter Player 4",player4['name'])
            if name!="":
                player4['name']=name
                
    
    def updateTeams():
        players = [player1,player2,player3,player4]
        team = [i['team'] for i in players if i['enabled']]
        if 2 not in team:
            if 3 in team:
                for i in range(len(team)):
                    if players[i]['team']==3:
                        players[i]['team']=2
                        team[i]=2
            if 2 not in team:
                if 4 in team:
                    for i in range(len(team)):
                        if players[i]['team']==4:
                            players[i]['team']=2
                            team[i]=2
            if 2 not in team:
                players[len(team)-1]['team']=2
        if 4 in team:
            if 3 not in team:
                for i in range(len(team)):
                    if players[i]['team']==4:
                        players[i]['team']=3
                        team[i]=3
                        
    def selectTeam():
        team = None
        
        status = True
        
        def select1():
            nonlocal status, team
            team = 1
            status = False
            
        def select2():
            nonlocal status, team
            team = 2
            status = False
            
        def select3():
            nonlocal status, team
            team = 3
            status = False
            
        def select4():
            nonlocal status, team
            team = 4
            status = False
        
        while status:
            
            draw.drawSquare(400,300,init.screen[0]-800,init.screen[1]-600,colors.BLACK)
            text.message_display("Select Team",50,colors.WHITE,init.screen[0]//2,350)
            text.button("1",700,500,50,50,colors.WHEAT,45,colors.GRAY,colors.WHITE, select1)
            text.button("2",760,500,50,50,colors.WHEAT,45,colors.GRAY,colors.WHITE, select2)
            text.button("3",820,500,50,50,colors.WHEAT,45,colors.GRAY,colors.WHITE, select3)
            text.button("4",880,500,50,50,colors.WHEAT,45,colors.GRAY,colors.WHITE, select4)
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        status = False
            
            pygame.transform.scale(init.surface, (init.res["width"],init.res["height"])) 
            init.gameDisplay.blit(init.surface, (0, 0))
            pygame.display.update()
            
            init.clock.tick(60)
        
        return team

        
    def select2():
        if player3['enabled']:
            team=selectTeam()
            if team!=None:
                player2['team']=team
                updateTeams()
            time.sleep(0.1)
        
    def select3():
        if player3['enabled']:
            team=selectTeam()
            if team!=None:
                player3['team']=team
                updateTeams()
            time.sleep(0.1)
        
    def select4():
        if player4['enabled']:
            team=selectTeam()
            if team!=None:
                player4['team']=team
                updateTeams()
            time.sleep(0.1)
            
    def done():
        nonlocal status
        status = 'continue'
        generateTeams([player1,player2,player3,player4])
        
    status = "input"
    while status=="input":
        draw.drawImage(init.bg,0,0,True)
        text.message_display("Enter Players",50,colors.WHITE,init.screen[0]//2,100)
        
        text.message_display("En",20,colors.WHITE,370,230)
        
        text.button("",350,250,50,50,colors.WHEAT,2,colors.GRAY,colors.GRAY)
        text.button("",350,320,50,50,colors.WHEAT,2,colors.GRAY,colors.GRAY)
        text.button("",350,390,50,50,colors.WHEAT,2,colors.GRAY,colors.WHITE, check3)
        text.button("",350,460,50,50,colors.WHEAT,2,colors.GRAY,colors.WHITE, check4)
        
        text.message_display("Names",30,colors.WHITE,500,225)
        
        text.button(player1['name'],420,250,500,50,colors.BLACK,45,colors.WHITE,colors.WHITE,input1)
        text.button(player2['name'],420,320,500,50,colors.BLACK,45,colors.WHITE,colors.WHITE,input2)
        text.button(player3['name'],420,390,500,50,colors.BLACK,45,colors.WHITE,colors.WHITE,input3)
        text.button(player4['name'],420,460,500,50,colors.BLACK,45,colors.WHITE,colors.WHITE,input4)
        
        text.message_display("Teams",20,colors.WHITE,940,225)
        
        text.button(str(player1['team']),930,250,50,50,colors.BLACK,45,colors.GRAY,colors.GRAY)
        text.button(str(player2['team']),930,320,50,50,colors.BLACK,45,colors.GRAY,colors.GRAY,select2)
        text.button(str(player3['team']) if player3['enabled'] else "",930,390,50,50,colors.BLACK,45,colors.GRAY,colors.WHITE,select3)
        text.button(str(player4['team']) if player4['enabled'] else "",930,460,50,50,colors.BLACK,45,colors.GRAY,colors.WHITE,select4)
        
        text.message_display("Tanks",20,colors.WHITE,1050,225)
        tankSelect.clickableImage(pygame.transform.scale(player1['tank'],(50,50)),1000,250,lambda:tankSelect.tankSelect(player1))
        tankSelect.clickableImage(pygame.transform.scale(player2['tank'],(50,50)),1000,320,lambda:tankSelect.tankSelect(player2))
        if player3['enabled']:
            tankSelect.clickableImage(pygame.transform.scale(player3['tank'],(50,50)),1000,390,lambda:tankSelect.tankSelect(player3))
        else:
            draw.drawSquare(1000,390,50,50,colors.WHITE)
        if player4['enabled']:
            tankSelect.clickableImage(pygame.transform.scale(player4['tank'],(50,50)),1000,460,lambda:tankSelect.tankSelect(player4))
        else:
            draw.drawSquare(1000,460,50,50,colors.WHITE)
        
        text.button("Continue",init.screen[0]//2-200,900,400,70,colors.BLACK,60,colors.WHITE,colors.GREEN, done)
        
        drawV(350,250)
        drawV(350,320)        
        
        if player3['enabled']:
            drawV(350,390)
        
        if player4['enabled']:
            drawV(350,460)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    status = "quit"
        
        pygame.transform.scale(init.surface, (init.res["width"],init.res["height"])) 
        init.gameDisplay.blit(init.surface, (0, 0))
        pygame.display.update()
        
        init.clock.tick(60)
    time.sleep(0.1)
    return status
        

def drawV(x,y,test=False):
    """Draws checkmark x,y are upper corner of square"""
    if test:
        return test
    draw.drawLine(x+5,y+20,x+25,y+40,6,colors.BLUE)
    draw.drawLine(x+25,y+40,x+45,y+5,6,colors.BLUE)
    
def generateTeams(players, test=False):
    if test:
        return test
    players = [player for player in players if player['enabled']]
    team1 = [(player['name'],player['tank']) for player in players if player['team']==1]
    team2 = [(player['name'],player['tank'])  for player in players if player['team']==2]
    team3 = [(player['name'],player['tank'])  for player in players if player['team']==3]
    team4 = [(player['name'],player['tank'])  for player in players if player['team']==4]
    tanks.teams = [team for team in [team1,team2,team3,team4] if len(team)>0]
    tanks.players = len(players)