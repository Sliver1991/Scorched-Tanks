import pygame

pygame.init()
width, height = pygame.display.list_modes()[0]
print(width,height)
gameDisplay = pygame.display.set_mode()
pygame.display.set_caption('Scorched Tanks')
clock = pygame.time.Clock()
pygame.display.toggle_fullscreen()

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                  pygame.quit()
                  quit()  
    clock.tick(60)

