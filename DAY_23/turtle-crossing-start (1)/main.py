import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # turned off the tracer

player = Player()  # object is created here
car_manager = CarManager()
score = Scoreboard()

screen.listen()  # listens for keyboard events
screen.onkey(player.go_up, "Up")  # when users press Up call the func player.go_up()


game = True
while game:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()  # object.file_name()
    car_manager.move_car()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game = False
            score.over()

        if player.finish_line():
            player.go_start()
            car_manager.level()
            score.increase()

screen.exitonclick()
