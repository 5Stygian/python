from turtle import *
import time as time

restart = "yes"
total = 0

turtle = Turtle()
screen = Screen()

while restart == "yes":
    turtle.clear()
    colorLoop   = True
    shapeLoop   = True
    bgColorLoop = True
    validShape  = ""
    while colorLoop:
        total += 1
        try:
            turtlecolor = screen.textinput("Turtle Color", "What color do you want your turtle to be?".lower().strip())
            turtle.color(turtlecolor)
            colorLoop = False
        except:
            turtle.write("Invalid Color! Please enter a valid color", font=("Arial", 20), align="center")
            time.sleep(2)
            turtle.clear()
            shapeLoop = True
    while shapeLoop:
        turtleshape = screen.textinput("Turtle Shape", "What shape do you want your turtle to be?".lower().strip())
        try:
            turtle.shape(turtleshape)
            shapeLoop = False
        except:
            turtle.write("Invalid Shape! Please enter a valid shape", font=("Arial", 20), align="center")
            time.sleep(2)
            turtle.clear()
            bgColorLoop = True
    while bgColorLoop:
        bg_color = screen.textinput("BGColor", "What color do you want the background to be?".lower().strip())
        try:
            screen.bgcolor(bg_color)
            bgColorLoop = False
            validShape = "no"
        except:
            turtle.write("Invalid Color! Please enter a valid color", font=("Arial", 20), align="center")
            time.sleep(2)
            turtle.clear()
            bgColorLoop = True
    while validShape != "yes":
        shape = textinput("Let's Draw!", "What shape should turtle draw?".lower().strip())
        if shape == "square":
            for i in range(4):
                turtle.forward(50)
                turtle.right(90)
            validShape = "yes"
        elif shape == "octagon":
            for i in range(8):
                turtle.forward(40)
                turtle.right(45)
            validShape = "yes"
        elif shape == "circle":
            turtle.circle(50)
            validShape = "yes"
        else:
            validShape = "no"
            turtle.write("That is not a valid shape!", font=("Arial", 20), align="center")
            time.sleep(2)
            turtle.clear()
    restart = ""
    while restart != "yes" or restart != "no":
        restart = screen.textinput("Play Again?", "Would you like to restart?".lower().strip())
        if restart == "no":
            turtle.bye()
            break
        if restart == "yes":
            turtle.reset()
            turtle.write(f"Thanks for playing! You ran the program {total} times", font=("Arial", 20), align="center")
            restart = "yes"
            break

screen.mainloop()
