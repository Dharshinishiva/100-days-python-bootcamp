from turtle import Turtle, Screen

timmy = Turtle("turtle")
timmy.color("red", "green")


def draw(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)


for game in range(3, 11):
    draw(game)

screen = Screen()
screen.exitonclick()
