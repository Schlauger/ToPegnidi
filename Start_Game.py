from bedging_SLUT import *
import pygame as pyg
from pygame.locals import *
from sys import exit


def getQuit():
    for event in pyg.event.get():
        if event.type == QUIT:
            return True



def main():
    pyg.init()
    # Initialize variables        
    windoSize = (640,640)
    clock = pyg.time.Clock()
    ticking = 30
    surfaceColor = (144, 0, 255)
    screen = pyg.display.set_mode(windoSize, DOUBLEBUF, 32)
    pyg.display.set_caption("Rogue and King")
    
    frst_surface = pyg.Surface(windoSize)
    frst_surface.fill('Red')

    background = pyg.image.load('assets/background.png')
    

    #Text
    textfont = pyg.font.SysFont("Arial",48)
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
    
        screen.blit(background,(0,windoSize[1]-125))


        pyg.display.update()

        #Set while clock
        clock.tick(60)
    
    pyg.quit()
    exit()

if __name__ == "__main__":
    main() # here