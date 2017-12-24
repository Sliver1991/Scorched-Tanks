import math

def coordinatefixer (x,y):
    x+=96
    y=972-y
    return (x,y)

def shot(equ_x,shot,x,y):
    x,y=coordinatefixer(x,y)
    res = shot(equ_x-x)
    return(equ_x,res+y)
    
def MakeEquationDic():
    
    def liniarShot(angle,x):
        return math.tan(math.radians(angle))*x
    
    def talulShot(angle, power, x):
        return  math.tan(math.radians(angle))*x**2+power*x
    
    def munjeShot(angle,power,x):
        return math.tan(math.radians(angle))*math.log(x,power)
    
    def crazyShot(angle,power,x):
        return math.tan(math.radians(angle))*math.sin(math.radians(power*x))

    return {"talulShot":talulShot,"liniarShot":liniarShot,"munjeShot":munjeShot,"crazyShot":crazyShot}

def distance(x1,y1,x2,y2):
    return int(math.sqrt((x1-x2)**2+(y1-y2)**2))

linear = MakeEquationDic()["liniarShot"]
ballistic  = MakeEquationDic()["talulShot"]
guided = MakeEquationDic()["munjeShot"]
crazy = MakeEquationDic()["crazyShot"]