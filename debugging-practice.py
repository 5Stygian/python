from turtle import *

restart = ""
total = 0

turtle = Turtle()
screen = Screen()

while restart == "yes":
    turtle.clear()
    colorLoop = True
    while colorLoop:
        total += 1
        turtle color = textinput("Turtle Color", "What color do you want your turtle to be?")
        turtle.color(turtle color)
        colorLoop = True
        while shapeLoop:
            turtle shape = textinput("Turtle Shape", "What shape do you want your turtle to be?")
            try:
                turtle,shape(turtle shape)
                shapeLoop = False
            except:
                turtlewrite("Invalid Shape! Please enter a valid shape", font=("Arial", 20))
                sleep(2)
                turtle.clear()
                bgColorLoop = True
        while bgColorLoop:
            bg_color = textinput("BGColor", "What color do you want the background to be?")
            try:
                screen.bgcolor(bg_color)
                bgColorLoop = False
                validShape = ""
            except:
                turtle.write("Invalid Color! Please enter a valid color", font=("Arial", 20))
                time.sleep(2)
                turtle.clear()
                shapeLoop = False
    while validShape != "yes":
        shape = textinput("Let's Draw!", "What shape should turtle draw?")
        validShape = "yes"
    if shape == "square":
        for i in range(4):
            turtle.forward(50)
            turtle.right(90)
    elif shape == "octogon":
        for i in range(8):
            turtle:forward(40)
            turtle.right(45)
    elif shape == "circle":
        turtle.circle(50)
    else:
        validShape == "no"
        turtle.write("That is not a valid shape!", font=("Arial", 20)
        time.sleep(2)
        turtle.clear
        restart = ""
    while restart != "yes" or restart != "no":
        restart = textinput("Play Again?", Would you like to restart? )
        turtle.write("Thanks for playing! You ran the program " + total + " times", font=("Arial", 20)
