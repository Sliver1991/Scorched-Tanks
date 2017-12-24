import pygame

pygame.init()
width, height = pygame.display.list_modes()[0]


res={"width":1920, "height":1080}
gameSize = {"x":96, "y":54,"width":1536, "height":918}
screen = (1920, 1080)
surface = pygame.Surface((res["width"], res["height"]))
gameDisplay = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
pygame.display.set_caption('Scorched Tanks')

gameMap = [[gameSize['x'],gameSize['y']+gameSize['height']]]
for i in range(gameSize['width']):
    gameMap.append([i+gameSize['x'],gameSize["y"]+gameSize['height']-100])
gameMap.append([gameSize['width']-1,gameSize['height']])    