import turtle
import random

my_turtle=turtle.Turtle()

num_sildes=3;
color_slides=["green","red","yellow","orange","purple","pink","blue","brown","MediumVioletRed"]
my_turtle.position()
while num_sildes<=9:
    my_turtle.pencolor(random.choice(color_slides))
    for i in range(num_sildes):
        my_turtle.forward(100)
        my_turtle.right(360 / num_sildes)
    num_sildes+=1


turtle.mainloop()
