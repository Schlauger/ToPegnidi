from bedging_SLUT import *
import pygame
from pygame.locals import *
from sys import exit

### Game Data
rooms=["Garden",
       "Bathroom",
       "Haul",
       "Storage",
       "Livingroom",
       "Saloon"
       "Lounge",
       "Corridor",
       "Kitchen",
       "Upper Coridor",
       "Brother's room",
       "Parent's room",
       "Your room"]

plotSize = (5,5)
rooms2D=[ [-1 for j in range(plotSize[0])]  for i in range(plotSize[1]) ]
y= 0
x= 2
# check around
options={
"above" : [y-1, x] if y-1>=0 else -1, 
"below" : [y+1, x] if y+1<plotSize[1] else -1,
"left" : [y, x-1] if x-1>=0 else -1,
"right" : [y, x-1] if x+1<plotSize[0] else -1,
}


pos=[y, x]
y,x= pos
windoSize = (640,640)

def getQuit():
    for event in pygame.event.get():
        if event.type == QUIT:
            return True

def center_Align(surface):
    return (windoSize[0] - surface.get_width())/2

def main():
    pygame.init()
    surfaceColor = (144, 0, 255)
    screen = pygame.display.set_mode(windoSize, DOUBLEBUF, 32)
    pygame.display.set_caption("Playing in Pygame!")
    textfont = pygame.font.SysFont("Arial",48)
    thetext = textfont.render("Hello world!", True,(255,0,0),(255,255,0))

    textx = center_Align(thetext)
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
    main()
