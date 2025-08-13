import basic

print(basic.variable)

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red", "green")
timmy.forward(100)
timmy.dot(50)

my_screen = Screen()
print(
    my_screen.canvheight
)  # canvheight  tells us the hight of the canvas that is created
my_screen.exitonclick()  # exitonclick() will make make the canvas stay in the screen
