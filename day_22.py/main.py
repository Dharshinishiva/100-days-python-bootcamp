from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(5, 1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor, new_y)


def go_down():
    new_y = paddle.ycor() - 0
    paddle.goto(paddle.xcor, new_y)


screen.listen()
screen.onkey(go_up, "up")
screen.onkey(go_down, "down")


game = True
while game:
    screen.updatea()

screen.exitonclick()
