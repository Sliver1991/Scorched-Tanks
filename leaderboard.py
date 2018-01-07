import pygame, leader, init,text,colors
    
def leaderboard():
    data = leader.readLeaders()
    if data is None:
        return "quit"
    data = data['players']
    sortKey = 'wins'
    flag = True
    def sortLeaders():
        data.sort(key=lambda player:player[sortKey],reverse=flag)
        
    sortLeaders()
    
    def sortByWins():
        nonlocal sortKey,flag
        if sortKey=='wins':
            flag = not flag
        else:
            sortKey='wins'
            flag = True
        sortLeaders()
        
    def sortByKills():
        nonlocal sortKey,flag
        if sortKey=='kills':
            flag = not flag
        else:
            sortKey='kills'
            flag = True
        sortLeaders()
        
    def sortByDeaths():
        nonlocal sortKey,flag
        if sortKey=='deaths':
            flag = not flag
        else:
            sortKey='deaths'
            flag = True
        sortLeaders()
        
    def sortByLoses():
        nonlocal sortKey,flag
        if sortKey=='loses':
            flag = not flag
        else:
            sortKey='loses'
            flag = True
        sortLeaders()
        
    def clearLeaders():
        f = open('leaderboard.txt','w')
        f.close()
        done()
        
    def done():
        nonlocal status
        status = 'quit'
        
    
    status = "menu"
    while status=="menu":
        init.surface.fill(colors.BLACK)
        text.message_display("Leaderboard - Top 5",50,colors.WHITE,init.screen[0]//2,100)
        
        text.button("Name",100,200,100,50,colors.WHITE,40,colors.GRAY,colors.GRAY)
        text.button("Wins",250,200,100,50,colors.WHITE,40,colors.GRAY,colors.GREEN,sortByWins)
        text.button("Kills",400,200,100,50,colors.WHITE,40,colors.GRAY,colors.GREEN,sortByKills)
        text.button("Deaths",550,200,130,50,colors.WHITE,40,colors.GRAY,colors.GREEN,sortByDeaths)
        text.button("Loses",700,200,100,50,colors.WHITE,40,colors.GRAY,colors.GREEN,sortByLoses)
        
        i=0
        for player in data[:5]:
            text.message_display(player['name'],25,colors.WHITE,150,300+i*50)
            text.message_display(str(player['wins']),25,colors.WHITE,300,300+i*50)
            text.message_display(str(player['kills']),25,colors.WHITE,450,300+i*50)
            text.message_display(str(player['deaths']),25,colors.WHITE,600,300+i*50)
            text.message_display(str(player['loses']),25,colors.WHITE,750,300+i*50)
            i+=1
            
        text.button("CLEAR LEADERBOARD",300,800,500,50,colors.WHITE,40,colors.GRAY,colors.RED1,clearLeaders)
        text.button("Back",1020,900,200,50,colors.WHITE,40,colors.GRAY,colors.GREEN, done)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    status = "quit"
        
        pygame.transform.scale(init.surface, (init.res["width"],init.res["height"])) 
        init.gameDisplay.blit(init.surface, (0, 0))
        pygame.display.update()
        
        init.clock.tick(60)