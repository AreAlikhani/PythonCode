import turtle
import time

root = turtle.Screen()
root.bgcolor('lightblue')
root.setup(width = 600, height = 700)
root.title('Clock')
root.tracer(0)


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(5)

#-------------draw clock face--------------
while True:
    h = int(time.strftime('%I'))
    m = int(time.strftime('%M'))
    s = int(time.strftime('%S'))

    pen.pensize(5)
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color('yellow')
    pen.pendown()
    pen.circle(210)
#======================draw the lines for hours============
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for i in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
        pen.pensize(5)

    #===========draw the hour hand================
    pen.penup()
    pen.goto(0,0)
    pen.color('black')
    pen.setheading(90)
    angle = (h/12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)
    pen.pensize(5)
    #===========draw the minute hand==============
    pen.penup()
    pen.goto(0,0)
    pen.color('blue')
    pen.setheading(90)
    angle = (m/60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)
    pen.pensize(3)
    #=============draw the second hand===========
    pen.penup()
    pen.goto(0,0)
    pen.color('red')
    pen.setheading(90)
    angle = (s/60) * 360
    pen.right(angle)
    pen.pendown()
    pen.fd(60)
    pen.pensize(1)





    root.update()
    time.sleep(1)
    pen.clear()






turtle.done()
