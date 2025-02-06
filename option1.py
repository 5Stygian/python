from turtle import *

# variables
backgroundColor = input("Background color: ")

turtleColor = input("Turtle color: ")
turtleSize = int(input("Turtle size: "))
turtleShape = input("Turtle shape: ")

screenWidth = int(input("Screen width: "))
screenHeight = int(input("Screen height: "))

# turtle and window
s = Screen()
t = Turtle()

s.setup(width=screenWidth, height=screenHeight)
s.bgcolor(backgroundColor)

t.speed(0)
t.shape(turtleShape)
t.color(turtleColor)
t.shapesize(turtleSize)

# shape inputs
def squareSpiral(amountSS):
    for i in range(amountSS):
        t.goto(0, screenHeight)
        t.right(7)
        t.goto(0, t.ycor * int(amountSS))
        for i in range(4):
            t.forward(100)
            t.left(90)

# actions
print("===============================")
print("||What shape should be drawn?||")
print("||    Spiral                 ||")
print("||    Plus                   ||")
print("||    Octagon                ||")
print("===============================")
shapeAsk = input("Input: ")

if shapeAsk == "spiral" or shapeAsk == "Spiral":
    amountSS = int(input("Spiral amount: "))
    squareSpiral(int(amountSS))
else:
    print("Please input a valid value")

s.mainloop()