from bedging_SLUT import *
import pygame
from pygame.locals import *
from sys import exit


def getQuit():
    for event in pygame.event.get():
        if event.type == QUIT:
            return True
        
windoSize = (640,640)

def main():
    pygame.init()
    surfaceColor = (144, 0, 255)
    screen = pygame.display.set_mode(windoSize, DOUBLEBUF, 32)
    pygame.display.set_caption("Playing in Pygame!")
    textfont = pygame.font.SysFont("Arial",48)
    thetext = textfont.render("Hello world!", True,(255,0,0),(255,255,0))

    textx = center_Align(windoSize,thetext)
    texty = 40

    endprogram = False
    b=200
    while not endprogram:
        (r,g,b)=color_tuple(b)
        screen.fill((r,g,b))
        screen.blit(thetext,(textx,texty))
        endprogram = getQuit()
        pygame.display.update()
    
    pygame.quit()
    exit()

if __name__ == "__main__":
    main() # here