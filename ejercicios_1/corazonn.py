import turtle as t

t.bgcolor("black")
t.speed("fastest")
t.pensize(5)

def curve():
    for i in range (200):
        t.right(1)
        t.fd(1)

def texts(text,x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.pencolor("white")
    t.write(text,font=('Roboto',50,'bold'))
    t.up()
    t.goto(-50,-50)
    t.down()

def head():
    t.color('red2','red1')
    t.begin_fill()
    t.left(140)
    t.fd(120)
    curve()
    t.left(125)
    curve()
    t.fd(120)
    t.end_fill() 
    t.hideturtle()

texts("Te Amo...",-220,180)
head()
texts("JA 22",-120,30)
texts("Mi jefecita",-120,-150)
texts("Hermosa",-50,-230)

t.exitonclick()
