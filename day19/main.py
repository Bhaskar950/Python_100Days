from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(1)

screen.listen()
screen.onkey(key='space' ,fun=move_forward)
screen.exitonclick()