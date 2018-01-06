import pygame,init

def drawSquare(x,y, w, h, color):
    pygame.draw.rect(init.surface, color, [x,y,w,h])

def drawPixel(loc_x,loc_y, color):
    pixAr = pygame.PixelArray(init.surface)
    pixAr[loc_x][loc_y] = color

def drawLine(start_x,start_y, end_x, end_y, width, color):    
    pygame.draw.line(init.surface, color, (start_x,start_y), (end_x, end_y),width)
    
def drawCircle(loc_x,loc_y, radius, color):
    pygame.draw.circle(init.surface, color, [loc_x,loc_y],radius)
    
def drawPoly(color,locList):
    pygame.draw.polygon(init.surface, color,locList)
    
def drawLeftArrow(color, x,y):
    poly = [(x,y),(x-10,y-15),(x,y-30),(x-10,y-30),(x-20,y-15),(x-10,y)]
    drawPoly(color,poly)
    
def drawRightArrow(color, x,y):
    poly = [(x,y),(x+10,y-15),(x,y-30),(x+10,y-30),(x+20,y-15),(x+10,y)]
    drawPoly(color,poly)