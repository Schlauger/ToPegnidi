from bedging_SLUT import *
import pygame as pyg
from pygame.locals import *
from sys import exit

class Artifiscielment: # ideattrezzo
    def __init__(self,name,fps) -> None:
        self.name = name
        self.clock= pyg.time.Clock()
        self.fps = fps

class Animatronic:   # Animation object
    def __init__(self,name,pos=()):
        self.name=name
        self.actions={'test':None} # A dictionary with the actions
        self.frame = 0  # current frame
        self.rect = 0   # current frame's rectangle
    
    def get_Action(self,action_name="walk"):
        '''Return the array with the actions frames'''
        return self.actions[action_name]
    

    def add_Action(self,file_name,action_name,num_of_frames,width_in,height_in):
        ''' Adding an a couple <action_name>:[] into the actions dictionary 
         from the file file_name '''
        sprite_sheet= pyg.image.load(file_name).convert_alpha()
        self.actions[action_name] = [self.get_image(sprite_sheet, idx, 0, width_in,height_in) for idx in range(num_of_frames)]

    def get_image(self,sheet, x_i, y_i, width, height,scale=1,color=(0,0,0)):
        ''' Get image from sprite sheet
        start at indexes **x_i** and **y_i** <u>NOT PIXELS</u>
        with **height** and **width**
        '''
        img = pyg.Surface((width, height)).convert_alpha()
        img.blit(sheet,(0,0),((x_i * width),(y_i * height),width,height))
        img = pyg.transform.scale(img, (width * scale, height *scale))
        img.set_colorkey(color)
        return img
    
    def input2frame(self,key_pressed,pos):
        if not key_pressed:
            self.frame = 0 if self.frame>=len(self.actions['idle'])-1 else self.frame+1
            fram = self.actions['walk'][self.frame]
            return (fram, fram.get_rect(midbottom=pos))