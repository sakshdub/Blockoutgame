from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 7)

        self.penup()
        self.speed("fastest")
        self.goto(x=0, y=-280)
    def move_right(self):
        new_x = self.xcor() + 20  # Move right by 20 units
        if new_x < 340:  # Keep paddle within bounds
            self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20  # Move left by 20 units
        if new_x > -340:  # Keep paddle within bounds
            self.goto(new_x, self.ycor())