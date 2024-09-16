from bedging_SLUT import *


### Game Data
idx=0
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

idx+=1
rooms2explore=[]
plotSize = (5,5)

rooms2D=[ [-1 for j in range(plotSize[0])]  for i in range(plotSize[1]) ]
start_pos=list([0,i] if i<plotSize[0] else [i-plotSize[0],0] for i in range(1,10)  )
# print("start potions:",random.sample(start_pos,1))
y, x = random.sample(start_pos,1)[0]
# y=0
# x=2
rooms2D[y][x] = rooms[idx]

# check around

new_options= lambda y,x : {
"above" : [y-1, x] if y-1>=0 else -1, 
"below" : [y+1, x] if y+1<plotSize[1] else -1,
"left" : [y, x-1] if x-1>=0 else -1,
"right" : [y, x+1] if x+1<plotSize[0] else -1,
}

def get_routes(Options_dic):
    posibleRoutes = list(filter( filter_IsValid,new_options(y,x).items()))
    return random.sample(posibleRoutes,random.randint(1,len(posibleRoutes)))


prnt2D(rooms2D)
# option to add rooms around
print("Rooms around:",new_options(y,x))
# choose randomly positions
routes=get_routes(new_options(y,x))
print("Choosed:",routes)

# Add room to each route
for r in routes:
    y,x= r[1]
    rooms2explore.append(r[1])
    rooms2D[y][x] = rooms[idx]
    idx+=1



prnt2D(rooms2D)
print(rooms2explore)