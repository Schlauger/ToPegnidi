# bedging_SLUT
# Supporting Level Utility Tools
import random
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

def prnt2D(table):
    for lin in table:
        for room in lin:
            print(str(room)+'\t\t',end='')
        print()


def filter_IsValid(pair):
    key,val=pair
    if val == -1:
       return False
    else:
        return True 

def get_routes(Options_dic):
    posibleRoutes = list(filter( filter_IsValid,Options_dic.items()))
    return random.sample(posibleRoutes,len(posibleRoutes))


if __name__ == "__main__":
    print("\n\nHello from...")
    cntr_text("Hello from Supporting Level Utility Tools",45)