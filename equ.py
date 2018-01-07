import math, init

dt = 1/15

def linear(angle,power,time):
    power = 100 if power==-1 else 500
    angle = math.radians(angle)
    time*=dt
    x = power*time*math.cos(angle)
    y = power*time*math.sin(angle)
    return int(x),int(y)

def ballistic(angle,power,time):
    angle = math.radians(angle)
    time*=dt
    x = init.rules['wind']*time**2/2+power*time*math.cos(angle)
    y = init.rules['gravity']*time**2/2+power*time*math.sin(angle)
    return int(x),int(y)

def guided(angle,power,time):
    
    reverse = False
    x=time*10
    if angle<90:
        angle = 90-angle
        if angle==0:angle=2
    elif angle==90:
        return(linear,angle,power,time)
    else:
        angle-=90
        reverse = True
    y=power*math.log(x,angle)
    if reverse:
        x*=-1
    if angle>90:
        y*=-1
    return int(x),int(y)

def crazy(angle,power,time):
    if power==0: power=100
    angle = math.radians(angle)
    time*=dt
    x = power*time
    y = power*math.sin(angle*x)
    return int(x),int(y)

def distance(x1,y1,x2,y2):
    return int(math.sqrt((x1-x2)**2+(y1-y2)**2))