from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.x_move = random.choice([-10, 10])  # Randomly start left or right
        self.y_move = random.choice([-10, 10])
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_move *=-1

    def bounce_x(self):
        self.x_move *= -1


