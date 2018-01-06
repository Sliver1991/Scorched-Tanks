import pygame,init

def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text,size,color,loc_x,loc_y):
    """Text appears with loc_x and loc_y it's center"""
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((loc_x),(loc_y))
    init.surface.blit(TextSurf, TextRect)

    pygame.display.update()
    
def button(msg,x,y,w,h,tc,ts,ic,ac, action=None, wait=200):
    """msg: What do you want the button to say on it.

    x: The x location of the top left coordinate of the button box.
    
    y: The y location of the top left coordinate of the button box.
    
    w: Button width.
    
    h: Button height.
    
    ic: Inactive color (when a mouse is not hovering).
    
    ac: Active color (when a mouse is hovering).
    
    tc = text color
    
    ts = text size"""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(init.surface, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
            pygame.time.delay(wait)
    else:
        pygame.draw.rect(init.surface, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",ts)
    textSurf, textRect = text_objects(msg, smallText,tc)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    init.surface.blit(textSurf, textRect)