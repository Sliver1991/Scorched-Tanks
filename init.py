import pygame, ctypes, os

pygame.init()
width, height = pygame.display.list_modes()[0]
clock = pygame.time.Clock()
ctypes.windll.user32.SetProcessDPIAware()
screen = (1920, 1080)
gameDisplay = pygame.display.set_mode(screen,pygame.FULLSCREEN)

res={"width":1920, "height":1080}
gameSize = {"x":96, "y":54,"width":1536, "height":918}

surface = pygame.Surface((res["width"], res["height"]))
rules = {"radius":100,"damage":100,"health":100, "gravity":-9.8, "wind":0, "map":"mixed","wind change":False,"wind low":-20,"wind high":20}
#ameDisplay = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
pygame.display.set_caption('Scorched Tanks')

sky =  pygame.image.load("."+os.sep+"assets"+os.sep+"sky"+os.sep+"sky1.jpg")
bg =  pygame.image.load("."+os.sep+"assets"+os.sep+"bg.jpg")