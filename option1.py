from turtle import *

Turtle().hideturtle()

# variables
s = Screen()
t = Turtle()

invisibleFString = "Invisible (recommended)"

backgroundColor = input("Background color: ").lower().strip()
while not backgroundColor:
    print("Please input a valid value")
    backgroundColor = input("Background color: ").lower().strip()

turtleColor = input("Turtle color: ").lower().strip()
while not turtleColor:
    print("Please input a valid value")
    turtleColor = input("Turtle color: ").lower().strip()

while True:
    try:
        screenWidth = int(input("Screen width: "))
        break
    except ValueError:
        print("Please input a valid value")

while True:
    try:
        screenHeight = int(input("Screen height: "))
        break
    except ValueError:
        print("Please input a valid value")

while True:
    try:
        turtleSize = int(input("Turtle size: "))
        break
    except ValueError:
        print("Please input a valid value")

print("====================================")
print("||    Arrow                       ||")
print("||    Turtle                      ||")
print("||    Circle                      ||")
print("||    Square                      ||")
print("||    Triangle                    ||")
print("||    Classic                     ||")
print("||                                ||")
print(f"||    {invisibleFString:<27} ||")
print("====================================")

turtleShape = input("Turtle shape: ").lower().strip()
while not turtleShape:
    print("Please input a valid value")
    turtleShape = input("Turtle shape: ").lower().strip()

if turtleShape == "invisible":  # duran duran
    t.hideturtle()
else:
    t.shape(turtleShape)

# turtle and window
s.setup(width=screenWidth, height=screenHeight)
s.bgcolor(backgroundColor)

t.speed(0)
t.color(turtleColor)
t.shapesize(turtleSize)

# shape inputs
def squareSpiral(amount):
    sideLength = 20
    for i in range(amount):
        for i in range(4):
            t.down()
            t.forward(sideLength)
            t.left(90)
            t.up()
        t.right(7) 
        sideLength += 10 

def plusQuarter():
    for i in range(2):
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.forward(50)

def plus():
    for i in range(4):
        plusQuarter()
        t.right(90)

def tiledHexagons():
    for i in range(3):
        for i in range(6):
            t.forward(100)
            t.left(60)
        t.right(120)

# actions
print("===============================")
print("||    Spiral                 ||")
print("||    Plus                   ||")
print("||    Tiled Hexagons         ||")
print("===============================")
shapeAsk = input("Shape: ").lower().strip()

if shapeAsk == "spiral":
    amount = int(input("Spiral amount: "))
    squareSpiral(amount)
    if amount >= 101:
        amount = 100
if shapeAsk == "plus":
    plus()
if shapeAsk == "tiled hexagons":
    tiledHexagons()
else:
    print("Please input a valid value")

print("===============================")
print("|| Stats:                    ||")
print("||    Shape:                 ||")
print(f"||    {shapeAsk:<22} ||")
print("||                           ||")
if shapeAsk == "spiral":
    print("||    Amount:                ||")
    print(f"||    {amount:<22} ||")
    print("||                           ||")
print("||    Color:                 ||")
print(f"||    {turtleColor:<22} ||")
print("||                           ||")
print("||    Window dimensions:     ||")
print(f"||    {screenWidth} x {screenHeight:<16} ||")
print("||                           ||")
print("||    Background color:      ||")
print(f"||    {backgroundColor:<22} ||")
print("||                           ||")
print("||    Turtle shape:          ||")
print(f"||    {turtleShape:<22} ||")
print("||                           ||")
if turtleShape != "invisible":
    print("||    Turtle size:           ||")
    print(f"||    {turtleSize:<22} ||")
    print("||                           ||")
print("||    Turtle color:          ||")
print(f"||    {turtleColor:<22} ||")
print("===============================")

s.mainloop()
