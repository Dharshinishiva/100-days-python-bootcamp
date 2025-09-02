import turtle as t
import random
from turtle import Screen


timmy = t.Turtle("turtle")  # module.class()
timmy.color("red", "green")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)  # this is called tuple. A tuple can never be changed
    return color


timmy.speed("fastest")


def draw_spirial(sizes_of_gap):
    for _ in range(int(360 / sizes_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + sizes_of_gap)


draw_spirial(5)

screen = Screen()
screen.exitonclick()
