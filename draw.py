import pygame,init

def drawSquare(x,y, w, h, color,test=False):
    if test:
        return test
    pygame.draw.rect(init.surface, color, [x,y,w,h])

def drawPixel(loc_x,loc_y, color, test=False):
    if test:
        return test
    pixAr = pygame.PixelArray(init.surface)
    pixAr[loc_x][loc_y] = color

def drawLine(start_x,start_y, end_x, end_y, width, color, test=False):
    if test:
        return test    
    pygame.draw.line(init.surface, color, (start_x,start_y), (end_x, end_y),width)
    
def drawCircle(loc_x,loc_y, radius, color, test=False):
    if test:
        return test
    pygame.draw.circle(init.surface, color, [loc_x,loc_y],radius)
    
def drawPoly(color,locList, test=False):
    if test:
        return test
    pygame.draw.polygon(init.surface, color,locList)
    
def drawLeftArrow(color, x,y,test=False):
    if test:
        return test
    poly = [(x,y),(x-10,y-15),(x,y-30),(x-10,y-30),(x-20,y-15),(x-10,y)]
    drawPoly(color,poly)
    
def drawRightArrow(color, x,y, test=False):
    if test:
        return test
    poly = [(x,y),(x+10,y-15),(x,y-30),(x+10,y-30),(x+20,y-15),(x+10,y)]
    drawPoly(color,poly)
    
def drawImage(image,x=0,y=0, transform=False, w=0,h=0,test=False):
    if test:
        return test
    if w==0: w=init.screen[0]
    if h==0: h=init.screen[1]
    if transform: image = pygame.transform.scale(image,(w,h))
    init.surface.blit(image, (x,y))