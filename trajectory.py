def coordinatefixer (x,y):
    x+=96
    y=972-y
    return (x,y)

def shot(equ_x,funcshot,x,y):
    x,y=coordinatefixer(x,y)
    res = funcshot(equ_x-x)
    return(equ_x,res+y)
    
def funcshot(x):
    return x

print(shot(1,1,513,100))