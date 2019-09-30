import turtle as t
import math
unit = 30
R = 3*unit
r = unit

t.setup(18*unit*2, 12*unit*2, 0, 0)
t.speed(5)

t.penup()
t.goto(-15*unit, -10*unit)
t.pendown()
t.color("red", "red")
t.pensize(1)
t.begin_fill()
for i in range(2):
    t.forward(15*unit*2)
    t.left(90)
    t.forward(10*unit*2)
    t.left(90)
t.end_fill()

t.color("yellow", "yellow")
t.penup()
t.goto(-10*unit, 5*unit)
t.left(180-18)
t.fd(R)
t.seth(0)
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(1.902*R)
    t.right(144)
t.end_fill()

t.penup()
t.goto(-5*unit, 8*unit)
t.rt(90+math.atan2(5, 3)*180/math.pi)
t.fd(r)
t.rt(180-18)
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(1.902*r)
    t.right(144)
t.end_fill()
t.seth(0)

t.penup()
t.goto(-3*unit, 6*unit)
t.rt(90+math.atan2(7, 1)*180/math.pi)
t.fd(r)
t.rt(180-18)
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(1.902*r)
    t.right(144)
t.end_fill()
t.seth(0)

t.penup()
t.goto(-3*unit, 3*unit)
t.lt(90+math.atan2(7, 2)*180/math.pi)
t.fd(r)
t.rt(180-18)
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(1.902*r)
    t.right(144)
t.end_fill()
t.seth(0)

t.penup()
t.goto(-5*unit, 1*unit)
t.lt(90 + math.atan2(5, 4)*180/math.pi)
t.fd(r)
t.rt(180-18)
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(1.902*r)
    t.right(144)
t.end_fill()

t.penup()
t.goto(-unit*4, 11*unit)
t.color("red", "red")
t.write("Python画国旗", font=('黑体', 20, 'normal'))
t.goto(-unit*18, 12*unit)
t.done()
