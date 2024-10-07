import turtle

rocket = turtle.Turtle()
space= turtle.Screen()

space.bgpic("backround.gif")

spaceman= turtle.Turtle()
spaceman.penup()
spaceman.goto(-103,255)
space.addshape("spaceman.gif")
spaceman.shape("spaceman.gif")


space.addshape("rocket.gif")
rocket.shape("rocket.gif")
rocket.penup()
rocket.goto(180, -250)
rocket.speed(1000)


def up():
    rocket.setheading(90)
    rocket.forward(10)
    rocket.setheading(0)

def down():
    rocket.setheading(270)
    rocket.forward(10)
    rocket.setheading(0)

def left():
    rocket.setheading(180)
    rocket.forward(10)
    rocket.setheading(0)

def right():
    
    rocket.forward(10)

turtle.listen()


turtle.onkeypress(up, "Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
while True:
    space.update()
    if rocket.distance(spaceman)<10:
        space.bgpic("thank.gif")

turtle.done()