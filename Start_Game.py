from bedging_SLUT import *
from game_Boltclock import *
import pygame as pyg
from pygame.locals import *
from sys import exit





def main():
    pyg.init()
    # Initialize variables        
    windoSize = ((2**7)*5,(2**7)*5) 
    clock = pyg.time.Clock()
    fps = 15
    
    screen = pyg.display.set_mode(windoSize, DOUBLEBUF, 32)
    pyg.display.set_caption("Rogue and King")
    
    sky = pyg.Surface(windoSize)
    sky.fill((71, 149, 252))

    frst_surface = pyg.Surface(windoSize)
    frst_surface.fill('Green')
    

    spawned = pyg.image.load('assets/bedger_tool/bedging_scissor.png').convert_alpha()
    spawned = pyg.transform.scale(spawned ,(int(spawned.get_width() * 0.04),int(spawned.get_height() * 0.035 ))).convert_alpha()
    spawned_rect = spawned.get_rect(midbottom=(500,500))
   
    # sprite_sheet= pyg.image.load('assets/ninja/Fighter/Walk.png').convert_alpha()
    # fighter_walk =[get_image(sprite_sheet, i, 0, 128, 128, 1, (0,0,0)) for i in range(8)]
    fighter = Animatronic("Fighter")
    fighter.add_Action(file_name='assets/ninja/Fighter/Idle.png',action_name="idle",num_of_frames=6,width_in=128,height_in=128)
    fighter.add_Action(file_name='assets/ninja/Fighter/Walk.png',action_name="walk",num_of_frames=8,width_in=128,height_in=128)
    fighter.add_Action(file_name='assets/ninja/Fighter/Run.png',action_name="run",num_of_frames=8,width_in=128,height_in=128)
    action=fighter.get_Action("walk")
    # action=fighter.get_Action("run")
    #action=fighter.get_Action("idle")
    
    
    # Animation timer
    last_update = pyg.time.get_ticks()
    anim_timer = 5
    animFrame = 0
    test_coin=[]
    # coin test 
    sprite_sheet= pyg.image.load('assets/pocket/coin.png').convert_alpha()
    for i in range(10):
        test_coin.append(get_image(sprite_sheet, 44+i*(90+5), 29, 90, 90))
    for i in range(8):
        test_coin.append(get_image(sprite_sheet, 124+i*(90+5), 146, 90, 90))

    endprogram = False
    b=200
    move_x=0
    font_idx=len(ma_fonts)-1
    # Game Loop
    while not endprogram:

        # Event Handler
        for event in pyg.event.get():
            if event.type == QUIT:  # Exit button
                endprogram = True
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_w:
                    font_idx=len(ma_fonts)-1 if font_idx<=0 else font_idx-1
                    print(font_idx,"Font:",ma_fonts[font_idx])


        (r,g,b)=color_tuple(b)
        screen.fill((r,g,b))
        # screen.blit(thetext,(textx,texty))
        
        
    
        

        screen.blit(sky,(0,0))
        screen.blit(frst_surface,(0,windoSize[1]-150))

        
        txt_label = text_label_tf("Rogue to King",'assets/fonts/'+ma_fonts[8],font_size=69)
        txt_x = center_Align(windoSize,txt_label)
        txt_y = windoSize[1]//4
        screen.blit(txt_label,(txt_x,txt_y))

        # Update animation
        current_time = pyg.time.get_ticks()
        if current_time - last_update >=500:
            animFrame += 1
            last_update = current_time
        if animFrame>=len(action):
            animFrame = 0
        
        
        spawned_rect.x-=1
        screen.blit(spawned,spawned_rect)

        move_x+=1
        if move_x>windoSize[1]-1:
            move_x = 0
        elif move_x<0:
            move_x = windoSize[1]-1
        fr,recta = fighter.input2frame(False,(move_x,windoSize[1]-145))
        screen.blit(fr,recta)
        for i,c in enumerate(test_coin):
            screen.blit(c,(i*30,i*30))
        

        pyg.display.update()
        #Set while clock
        clock.tick(fps)
    
    pyg.quit()
    exit()

if __name__ == "__main__":
    main() # here