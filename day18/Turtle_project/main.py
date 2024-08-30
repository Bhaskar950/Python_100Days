from turtle import Turtle , Screen
import turtle as t
import random


tim = Turtle()
tim.shape("turtle")
t.colormode(255)


# for _ in range(15):
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)
#     tim.color("black")
#
# screen = Screen()
# screen.exitonclick()
#
colors = ["DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
"wheat", "SlateGray"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.left(angle)
#
# for shape_side_n in range(2,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    clr = (r,g,b)
    return clr

directions = [0,90,180,270]
tim.pensize(20)
tim.speed("slow")



for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))




