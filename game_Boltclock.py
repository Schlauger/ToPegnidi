from bedging_SLUT import *
import pygame as pyg
from pygame.locals import *
from sys import exit

class Artifiscielment: # ideattrezzo
    def __init__(self,name,fps) -> None:
        self.name = name
        self.clock= pyg.time.Clock()
        self.fps = fps


class Animatronic:
    def __init__(self,name):
        self.name=name
        self.actions={'test':None}
    
    def get_Action(self,action_name="walk"):
        '''
        Return the array with the actions frames
        '''
        return self.actions[action_name]
    
    def add_Action(self,file_name,action_name,num_of_frames,width_in,height_in):
        
        sprite_sheet= pyg.image.load(file_name).convert_alpha()
        print("Args=====>",sprite_sheet)
        self.actions[action_name] = [self.get_image(sprite_sheet, idx, 0, 128,128) for idx in range(num_of_frames)]
        print(self.actions)

    def get_image(self,sheet, x_i, y_i, width, height,scale=1,color=(0,0,0)):
        ''' Get image from sprite sheet
        start at indexes **x_i** and **y_i** <u>NOT PIXELS</u>
        with **height** and **width**
        '''
        print("================>",sheet, x_i, y_i, width, height,scale,color)
        img = pyg.Surface((width, height)).convert_alpha()
        img.blit(sheet,(0,0),((x_i * width),(y_i * height),width,height))
        img = pyg.transform.scale(img, (width * scale, height *scale))
        img.set_colorkey(color)
        return img
    