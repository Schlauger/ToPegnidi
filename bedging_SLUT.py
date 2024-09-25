# bedging_SLUT
# Supporting Level Utility Tools
import random
import pygame as pyg

def cntr_text(txt,line_width=80):
    txtLength=len(txt)
    spaces=(line_width - txtLength)//2
    print(spaces*' '+txt)

def roll_dice():
    
    mnumber =random.randint(1,6)
    cntr_text("A dice was rolled...",45)
    given = int(input("Guess a number from 1 to 6 :\n\t\t"))

    while (mnumber != given):
        cntr_text("Miss...",45)
        given = int(input("Guess a number from 1 to 6 :"))

## Get Color tuple 
def color_tuple():
    b=random.randint(0,255)
    r = int(b*(144/255))
    g = r-10 if r>=10 else 0
    return (r,g,b)

def color_tuple(b=255//2):
    n_b=b+random.randint(-5,5)
    n_b = n_b if n_b>=0 and n_b<=255 else 0
    r = int(n_b*(144/255))
    g = random.randint(0,r)
    return (r,g,n_b)

# Show 2D array as a simple map
def prnt2D(table):
    for lin in table:
        for room in lin:
            print(str(room)+'\t',end='')
        print()

# Function for filter on pairs
def filter_IsValid(pair):
    key,val=pair
    if val == -1:
       return False
    else:
        return True
    
def get_routes(Options_dic):
    posibleRoutes = list(filter( filter_IsValid,Options_dic.items()))
    return random.sample(posibleRoutes,len(posibleRoutes))

#
def center_Align(windoSize,surface):
    return (windoSize[0] - surface.get_width())/2

ma_fonts=["AnAlphaBetIsm-Medium.ttf", "AnAlphaBetIsm.ttf", "Apalu.ttf", "Asghia-Regular.otf", "Asghia-Regular.ttf", "Canterbury.ttf", "Christmas Gift.ttf", "HomemadeApple.ttf", "Olde English Regular.ttf", "POSEA___.TTF", "Prestige Signature Script - Demo.ttf", "Reman.ttf", "ROCHESTE.TTF", "Rossana-Regular.otf", "southpaw.otf", "SpontanoCondenso.ttf", "StrokeyHand.ttf", "TangoMacabre.ttf", "Tremolo-DemiBold.ttf", "Tremolo.ttf", "Viking Runes and Icons.otf"]
# Get label surface from text
def text_label(txt,font_idx=0,font_size=5,color=pyg.Color('#9000ff')):
    pyg.font.init()
    fonts = pyg.font.get_fonts()
    di_fond = pyg.font.SysFont(fonts[font_idx],font_size)
    text_surface = di_fond.render(txt,True,color)
    return text_surface

def text_label_tf(txt,font_name,font_size=5,color=pyg.Color('#9000ff')):
    pyg.font.init()
    di_fond = pyg.font.Font(font_name,font_size)
    text_surface = di_fond.render(txt,True,color)
    return text_surface


# Get a tile piece from a surface 
def get_image(sheet, x_i, y_i, width, height,scale=1,color=(0,0,0)):
    ''' Get image from sprite sheet
     start at indexes **x_i** and **y_i** <u>NOT PIXELS</u>
     with **height** and **width**
    '''
    img = pyg.Surface((width, height)).convert_alpha()
    img.blit(sheet,(0,0),((x_i),(y_i),width,height))
    img = pyg.transform.scale(img, (width * scale, height *scale))
    img.set_colorkey(color)
    return img


if __name__ == "__main__":
    print("\n\nHello from...")
    cntr_text("Hello from Supporting Level Utility Tools",45)