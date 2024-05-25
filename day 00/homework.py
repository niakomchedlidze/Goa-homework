from turtle import *


#we want to paint a house
speed(30)
width(5)
color("yellow")
forward(200)
left(90)


forward(200)
left(90)



forward(200)
left(90)

forward(200)
left(90)
#end for square

#drawing a door

forward(70)
color("blue")
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("pink")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)



exitonclick()