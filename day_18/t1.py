from turtle import Turtle, Screen

timmy = Turtle("turtle")
timmy.color("red", "green")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)


screen = Screen()
screen.exitonclick()


# also we can do

# for _ in range(4):
# timmy.right(90)
# timmy.forward(100)
