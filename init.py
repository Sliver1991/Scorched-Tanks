import pygame

pygame.init()
width, height = pygame.display.list_modes()[0]

colors = {"white":(255,255,255),"black":(0,0,0),"brown":(165,42,42)}
#gameMap = [[colors["white"] if y<height*0.6 else colors["brown"] for x in range(int(width*0.8))] for y in range(int(height*0.8))]

"""
    read into surfarray for a potential method of using matrix to draw the map
"""

#width -= 20
#height -= 100
#gameDisplay = pygame.display.set_mode((width, height))
gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption('Scorched Tanks')
clock = pygame.time.Clock()

def drawSquare(color, x, y, w, h):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def gameFrame():
    frameX = width*0.05
    frameY = height*0.05
    frameW = width*0.8
    frameH = height*0.8
    drawSquare(colors["white"],frameX,frameY,frameW,frameH)
    
def gameMap():
    x = width*0.05
    y = height*0.6
    w = width*0.8
    h = height*0.25
    drawSquare(colors["brown"],x,y,w,h)
    
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                  game = False
                  
    gameDisplay.fill(colors["black"])
    gameFrame()
    gameMap()
    pygame.display.update()
    
    clock.tick(60)

pygame.quit()