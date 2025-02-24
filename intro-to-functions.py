
'''
from turtle import *
import time

# Creating the screen and the turtle
screen = Screen()
crush = Turtle()
crush.color("black")



# The program loop variable
again = "yes"
while again == "yes":
   # Resetting the turtle for a restart
   crush.reset()
   crush.pensize(5)
   crush.speed(0)

   # Making screen color unbreakable
   while True:
       screenColor = textinput("Screen Color", "What color would you like the screen to be? ")
       try:
           screen.bgcolor(screenColor.lower())
           break
       except:
           crush.write("That's not a valid color. Try again.", font=("Arial", 20))
           time.sleep(2)
           crush.clear()
   # Making turtle color unbreakable
   while True:
       tColor = textinput("Turtle Color", "What color would you like the turtle to be? ")
       try:
           crush.color(tColor.lower())
           break
       except:
           crush.write("That's not a valid color. Try again.", font=("Arial", 20))
           time.sleep(2)
           crush.clear()

   # Making the shape size unbreakable
   while True:
       length = textinput("Shape Size", "How big would you like the shape to be? ")
       try:
           length = int(length)
           break
       except:
           crush.write("Please only enter a number. Try again.", font=("Arial", 20))
           time.sleep(2)
           crush.clear()

   # Making the repeat number unbreakable
   while True:
       repeat = textinput("Repeat", "How many times do you want to repeat the drawing? ")
       try:
           repeat = int(repeat)
           break
       except:
           crush.write("Please only enter numbers. Try again.", font=("Arial", 20))
           time.sleep(2)
           crush.clear()

   crush.up()
   crush.goto(-100, 0)
   crush.down()
   # Drawing the shape with the user input
   for i in range(repeat):
       for i in range(4):
           crush.forward(length)
           crush.right(90)
           crush.right(45)

   # Making the restart option unbreakable
   while True:
       startOver = textinput("Restart", "Do you want to try again? ")
       if startOver.lower() == "yes":
           break
       elif startOver.lower() == "no":
           again = "no"
           break
       else:
           crush.write("Please only answer with yes or no. Try again.", font=("Arial", 20))
           time.sleep(2)
           crush.clear()



# Clearing the screen for the turtle's goodbye
crush.clear()
crush.up()
crush.goto(-100,0)
crush.down()
crush.write("Goodbye", font = ("Arial", 60))
time.sleep(4)
exit()

screen.mainloop()
'''
