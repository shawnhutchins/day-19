from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

# w key to go forwards
# s key to go backwards
# a key to go counter-clockwise
# d key to go clockwise
# c key to clear the screen and put the turtle back in the center

move_distance = 10
turn_degrees = 10

def move_forwards():
    timmy.forward(move_distance)

def move_backwards():
    timmy.backward(move_distance)

def turn_right():
    timmy.right(turn_degrees)

def turn_left():
    timmy.left(turn_degrees)

def clear_and_reset():
    timmy.home()
    timmy.setheading(0)
    timmy.clear()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_and_reset)
screen.exitonclick()