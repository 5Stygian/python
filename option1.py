from turtle import *
from time import sleep

Turtle().hideturtle()

# variables
s = Screen()
t = Turtle()

repeat = True
amount = 0

backgroundColor, turtleColor = 'Black', 'White'

invisibleFString = "Invisible (recommended)"

# functions
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

while repeat:
    '''
    backgroundColor = str(input("Background color: ").lower().strip())
    while not backgroundColor:
        print("Please input a valid value")
        backgroundColor = str(input("Background color: ").lower().strip())

    turtleColor = input("Turtle color: ").lower().strip()
    while not turtleColor:
        print("Please input a valid value")
        turtleColor = input("Turtle color: ").lower().strip()
    '''

    while True:
        try:
            if not backgroundColor == '':
                 backgroundColor = str(input("Background color: ").lower().strip())
            break
        except ValueError or TypeError or IndexError or backgroundColor == False:
            print("Please input a valid value")

    while True:
        try:
            if not turtleColor == '':
                turtleColor = str(input("Turtle color: ").lower().strip())
            break
        except ValueError:
            print("Please input a valid value")

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

    def reset():
        t.reset()
        global backgroundColor, turtleColor, shapeAsk, screenWidth, screenHeight, turtleSize, amount
        backgroundColor, turtleColor, shapeAsk = "", "", ""
        screenWidth, screenHeight, turtleSize, amount = 0, 0, 0, 0
        print("\n" * 100)


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
    elif shapeAsk == "plus":
        plus()
    elif shapeAsk == "tiled hexagons":
        tiledHexagons()
    elif shapeAsk != "spiral" or shapeAsk != "plus" or shapeAsk != "tiled hexagons":
        print("Please input a valid value")
        shapeAsk = input("Shape: ").lower().strip()

    print("=================================")
    print("|| Stats:                      ||")
    print("||    Shape:                   ||")
    print(f"||    {shapeAsk:<24} ||")
    print("||                             ||")
    if shapeAsk == "spiral":
        print("||    Amount:                ||")
        print(f"||    {amount:<24} ||")
        print("||                           ||")
    print("||    Color:                   ||")
    print(f"||    {turtleColor:<24} ||")
    print("||                             ||")
    print("||    Window dimensions:       ||")
    print(f"||    {screenWidth} x {screenHeight:<18} ||")
    print("||                             ||")
    print("||    Background color:        ||")
    print(f"||    {backgroundColor:<24} ||")
    print("||                             ||")
    print("||    Turtle shape:            ||")
    print(f"||    {turtleShape:<24} ||")
    print("||                             ||")
    if turtleShape != "invisible":
        print("||    Turtle size:             ||")
        print(f"||    {turtleSize:<24} ||")
        print("||                             ||")
    print("||    Turtle color:            ||")
    print(f"||    {turtleColor:<24} ||")
    print("=================================")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1.1)
    print("===============================")
    print("||    Yes                    ||")
    print("||    No                     ||")
    print("===============================")
    repeatIn = input("Repeat: ").lower().strip()
    if repeatIn == "no":
        reset()
        repeat = False
        break
    if repeatIn == "yes":
        reset()
        repeat = True
        print("===============================")
    else:
        print("Please input a valid value")
        repeatIn = input("Repeat: ").lower().strip()

s.mainloop()
