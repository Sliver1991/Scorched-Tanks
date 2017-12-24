"""Useful PyGame functions"""

"""Text Display"""

def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text,size,color,loc_x,loc_y):
    #Text appears with loc_x and loc_y it's center
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((loc_x),(loc_y))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
"""Draw"""

def drawSquare(loc_x,loc_y, width, height, color):
    pygame.draw.rect(gameDisplay, color, [loc_x,loc_y, width, height])
    
def drawPixel(loc_x,loc_y, color):
    pixAr = pygame.PixelArray(gameDisplay)
    pixAr[loc_x][loc_y] = color

def drawLine(start_x,start_y, end_x, end_y, width, color):    
    pygame.draw.line(gameDisplay, color, (start_x,start_y), (end_x, end_y),width)
    
def drawCircle(loc_x,loc_y, radius, color):
    pygame.draw.circle(gameDisplay, color, [loc_x,loc_y],radius)
    
def drawPoly(color,locList):
    pygame.draw.polygon(gameDisplay, color,locList)
    
def button(msg,x,y,w,h,ic,ac, action=None):
    """msg: What do you want the button to say on it.

    x: The x location of the top left coordinate of the button box.
    
    y: The y location of the top left coordinate of the button box.
    
    w: Button width.
    
    h: Button height.
    
    ic: Inactive color (when a mouse is not hovering).
    
    ac: Active color (when a mouse is hovering)."""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)