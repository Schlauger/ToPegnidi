from bedging_SLUT import *
from game_Boltclock import *
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
    windoSize = ((2**7)*5,(2**7)*5) 
    clock = pyg.time.Clock()
    fps = 120
    surfaceColor = (144, 0, 255)
    screen = pyg.display.set_mode(windoSize, DOUBLEBUF, 32)
    pyg.display.set_caption("Rogue and King")
    
    sky = pyg.Surface(windoSize)
    sky.fill((71, 149, 252))
    frst_surface = pyg.Surface(windoSize)
    frst_surface.fill('Green')
    

    background = pyg.image.load('assets/background.png')
    
   
    # sprite_sheet= pyg.image.load('assets/ninja/Fighter/Walk.png').convert_alpha()
    # fighter_walk =[get_image(sprite_sheet, i, 0, 128, 128, 1, (0,0,0)) for i in range(8)]
    fighter = Animatronic("Fighter")
    fighter.add_Action(file_name='assets/ninja/Fighter/Walk.png',action_name="walk",num_of_frames=8,width_in=128,height_in=128)
    action=fighter.get_Action("walk")
    
    # Animation timer
    last_update = pyg.time.get_ticks()
    anim_timer = 0
    animFrame = 0
    


    endprogram = False
    b=200
    # Game Loop
    while not endprogram:
        (r,g,b)=color_tuple(b)
        screen.fill((r,g,b))
        # screen.blit(thetext,(textx,texty))
        
        
    
        screen.blit(background,(0,windoSize[1]-125))

        screen.blit(sky,(0,0))
        screen.blit(frst_surface,(0,windoSize[1]-150))

        txt_label = text_label("Rogue to King",font_size=69)
        txt_x = center_Align(windoSize,txt_label)
        txt_y = windoSize[1]//4
        screen.blit(txt_label,(txt_x,txt_y))

        # Update animation
        current_time = pyg.time.get_ticks()
        if current_time - last_update >=500:
            animFrame +=1
            last_update = current_time
        if animFrame>=len(action):
            animFrame = 0
        screen.blit(action[animFrame],(0,0))
        


        pyg.display.update()
        endprogram = getQuit()
        #Set while clock
        # clock.tick(fps)
    
    pyg.quit()
    exit()

if __name__ == "__main__":
    main() # here