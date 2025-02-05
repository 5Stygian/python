from turtle import *

# variables
backgroundColor = input("Background color: ")

turtleColor = input("Turtle color: ")
turtleSize = input("Turtle size: ")
turtleShape = input("Turtle shape: ")

# turtle and window
s = Screen()
t = Turtle()

s.setup(width=600, height=600)
s.bgcolor(backgroundColor)

t.speed(0)
t.shape(turtleShape)
t.color(turtleColor)
t.shapesize(turtleSize)

# shape inputs


s.mainloop()
