from turtle import Turtle  # Turtle class from turtle module

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()  # does not draw line
        self.go_start()  # turtle moves to that x,y position
        self.setheading(90)  # like heading toward north: 90

    def go_up(self):
        self.forward(MOVE_DISTANCE)

        # def go_r(self):
        # self.setheading(0)  # face right
        # self.forward(10)

        #   def go_l(self):
        #   new_x = self.xcor() - 10
        #   self.goto(new_x, self.ycor())

    def finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def go_start(self):
        self.goto(STARTING_POSITION)
