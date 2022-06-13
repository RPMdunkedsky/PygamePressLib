import pygame
pygame.init()
def get_key_pressed():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            return "QUIT"
        elif event.type==pygame.K_0:
            return "0"
        elif event.type==pygame.K_1:
            return "1"
        elif event.type==pygame.K_2:
            return "2"
        elif event.type==pygame.K_3:
            return "3"
        elif event.type==pygame.K_4:
            return "4"
        elif event.type==pygame.K_5:
            return "5"
        elif event.type==pygame.K_6:
            return "6"
        elif event.type==pygame.K_7:
            return "7"
        elif event.type==pygame.K_8:
            return "8"
        elif event.type==pygame.K_9:
            return "9"
        elif event.type==pygame.K_BACKSPACE:
            return "BACKSPACE"
        elif event.type==pygame.K_TAB:
            return "TAB"
        elif event.type==pygame.K_CLEAR:
            return "CLEAR"
        elif event.type==pygame.K_RETURN:
            return "RETURN"
        
        