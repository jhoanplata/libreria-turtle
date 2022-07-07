import turtle 

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.hideturtle()
t.goto(0,-10)

t.pensize(5)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(180)
t.end_fill()

t.penup()
t.goto(-85,130)
t.pendown()
t.color('white')
t.write('Te Amo...',font=('Roboto',45,'bold'))

t.done()