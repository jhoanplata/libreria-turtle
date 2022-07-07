from random import random
from turtle import*
import random

title("400 trazos")

speed(0)
x = 1
while x < 400:
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colormode(255)
    pencolor(r,g,b)
    forward(5+x)
    right(120)
    x+=1
    
mainloop()