from turtle import Turtle, Screen  # class is imported from a module
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()  # object is created
screen.setup(600, 600)  # its the size of the screen
screen.bgcolor("black")  # its the background color
screen.title("WELCOME TO THE SNAKE GAME ! ! !")
screen.tracer(0)

s = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)

    s.move()

    if s.head.distance(food) <= 15:
        food.refreash()
        s.extend()
        scoreboard.increase_score()

    if (
        s.head.xcor() > 290
        or s.head.xcor() < -290
        or s.head.ycor() > 290
        or s.head.ycor() < -290
    ):
        game = False
        scoreboard.game_over()

    for segment in s.segments[1:]:
        if segment == s.head:
            pass
        elif s.head.distance(segment) < 10:
            game = False
            scoreboard.game_over()


screen.exitonclick()
