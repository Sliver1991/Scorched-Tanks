import math, random
import numpy as np
from scipy.interpolate import interp1d as inter
import init

def quad(angle,power,g,shift_x,shift_y):
    t = np.array(range(100))
    x,y = ballistic(angle,power,t,g)
    f = inter(x,y,kind="quadratic", fill_value='extrapolate')
    return [[i+shift_x,int(f(i))+shift_y] for i in range(500)]

def lin(angle,shift_x,shift_y):
    t = np.array(range(1000))
    x,y = linear(angle,t)
    f = inter(x,y,kind="linear",fill_value='extrapolate')
    return [[i+shift_x,int(f(i))+shift_y] for i in range(500)]

def ballistic(angle,power,time,g):
    angle = math.radians(angle)
    x = power*time*math.cos(angle)
    y = g*time**2/2+power*time*math.sin(angle)
    return x,y

def linear(angle,time):
    angle = math.radians(angle)
    x = time*math.cos(angle)
    y = time*math.sin(angle)
    return x,y

def trim():
    global gameMap
    min_y = gameSize['y']+150
    max_y = gameSize['height']-50
    i = 2
    while i<len(gameMap) and min_y<=gameMap[i][1]<=max_y and gameMap[i][0]<=gameSize['width']:
        i+=1
    gameMap = gameMap[:i]

def clean():
    global gameMap
    cleanedMap = gameMap[:2]
    xmap = []
    for x,y in gameMap[2:]:
        if x not in xmap:
            cleanedMap.append([x,y])
            xmap.append(x)
    gameMap=cleanedMap

gameSize = {"x":96, "y":54,"width":1536, "height":918}

def mapGen():
    global gameMap
    mode = init.rules["map"]
    gameMap = [[gameSize['x'],gameSize['height']]]
    x,y = gameSize['x'], gameSize['height']-random.randint(50,750)
    while x<gameSize['width']:
        last_y = gameMap[-1][1]
        if last_y==gameSize['y']+150:
            angle = random.randint(-80,0)
        elif last_y==gameSize['height']-50:
            angle = random.randint(0,80)
        else:
            angle = random.randint(-80,80)
        if mode=="mixed":
            slope = random.choice(["quad","lin"])
        elif mode=="straight":
            slope = "lin"
        elif mode=="slope":
            slope="quad"
        slope_len = random.randint(100,500)
        if slope=="quad":
            power = random.randint(10,100)
            g = random.uniform(-20,20)
            gameMap.extend(quad(angle,power,g,x,y)[:slope_len])
        else:
            gameMap.extend(lin(angle,x,y)[:slope_len])
        trim()
        x,y = gameMap[-1][0],gameMap[-1][1]
    clean()
    gameMap.append([gameSize['width'],gameSize['height']])
    return gameMap

