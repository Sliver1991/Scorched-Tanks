import pygame, text, colors, init, draw

keys = {pygame.K_0:'0', pygame.K_1:'1', pygame.K_2:'2', pygame.K_3:'3', pygame.K_4:'4', 
        pygame.K_5:'5', pygame.K_6:'6', pygame.K_7:'7', pygame.K_8:'8', pygame.K_9:'9', 
        pygame.K_a:'a', pygame.K_b:'b', pygame.K_c:'c', pygame.K_d:'d', pygame.K_e:'e', 
        pygame.K_f:'f', pygame.K_g:'g', pygame.K_h:'h', pygame.K_i:'i', pygame.K_j:'j', 
        pygame.K_k:'k', pygame.K_l:'l', pygame.K_m:'m', pygame.K_n:'n', pygame.K_o:'o', 
        pygame.K_p:'p', pygame.K_q:'q', pygame.K_r:'r', pygame.K_s:'s', pygame.K_t:'t', 
        pygame.K_u:'u', pygame.K_v:'v', pygame.K_w:'w', pygame.K_x:'x', pygame.K_y:'y', 
        pygame.K_z:'z'}

numUpper = ['!','@','#','$','%','^','&','*','(',')']

def textBox(msg,string = ""):
    """Displays a text box with msg, returns input string. Empty string if hit esc"""
    while True:
        
        draw.drawSquare(350,350,init.screen[0]-700,500,colors.BLACK)
        
        text.message_display(msg,40,colors.WHITE,init.screen[0]//2,400)
        
        draw.drawSquare(400,600,init.screen[0]-800,50,colors.WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return ""
                
                if event.key == pygame.K_RETURN:
                    return string
                if len(string)<15:
                    if event.key in keys:
                        key = keys[event.key]
                        if key.isalpha():
                            if pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]:
                                string+=key.upper()
                            else:
                                string+=key
                        else:
                            if pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]:
                                string+=numUpper[int(key)-1]
                            else:
                                string+=key
                                
                    if event.key  == pygame.K_SPACE:
                        string+=' '
                    
                    if event.key  == pygame.K_MINUS:
                        string+='-'
                        
                    if event.key  == pygame.K_PERIOD:
                        string+='.'
                    
                if event.key == pygame.K_BACKSPACE:
                    string = string[:-1]
          
        text.message_display(string,40,colors.BLACK,init.screen[0]//2,620)          
        pygame.transform.scale(init.surface, (init.res["width"],init.res["height"])) 
        init.gameDisplay.blit(init.surface, (0, 0))
        pygame.display.update()
        
        init.clock.tick(60)