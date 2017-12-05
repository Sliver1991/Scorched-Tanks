import pygame

pygame.init()
width, height = pygame.display.list_modes()[0]

colors = {"white":(255,255,255),"black":(0,0,0)}


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
    pygame.display.update()
    
    clock.tick(60)

pygame.quit()