from turtle import Turtle,Screen
from ball import Ball
from paddle import Paddle
import random
import time
screen=Screen()
screen.setup(width=800, height=600)  # Set screen size
ROW=(3,4,5)
COL=(8,9,10)
BLOCK_HEIGHT=20
BLOCK_GAP=2
LIFE=3
def create_block():
    blocks=[]
    rows = random.choice(ROW)
    cols = random.choice(COL)
    BLOCK_WIDTH = (screen.window_width() - (cols - 1) * BLOCK_GAP) / cols
    for row in range(rows):
        for col in range(cols):
            x = -screen.window_width() / 2 + col * (BLOCK_WIDTH + BLOCK_GAP) + BLOCK_WIDTH / 2
            # Calculate y position (starting from the top)
            y = 250 - row * (BLOCK_HEIGHT + BLOCK_GAP)
            block=Turtle()
            block.shape("square")
            block.color("blue")  # Make blocks visible against the background

            block.shapesize(stretch_wid=BLOCK_HEIGHT/20,stretch_len=BLOCK_WIDTH/20)
            block.penup()
            block.goto(x, y)  # Position the block
            blocks.append(block)
    return blocks
def Game_over():
    over=Turtle()
    over.goto(0,0);
    over.write("GAME OVER",align="center",font=("Arial", 24, "normal"))
screen.tracer(0)
blocks=create_block()
paddle=Paddle()
ball=Ball()
screen.listen()
screen.onkey(key="Right",fun=paddle.move_right)
screen.onkey(key="Left",fun=paddle.move_left)
game_on=True
while game_on:
    time.sleep(0.1)
    ball.move()

    if ball.ycor()>290:
        ball.bounce_y()
    elif ball.xcor()>385 or ball.xcor()<-385:
        ball.bounce_x()
    elif ball.distance(paddle) <50 and ball.ycor() < paddle.ycor() + 30:
        ball.bounce_y()
        ball.sety(paddle.ycor() + 25)
    for block in blocks:
        if ball.distance(block)<40:
            ball.bounce_y()
            block.hideturtle()
            blocks.remove(block)
            break

    if ball.ycor()<-275:
        if(LIFE!=0):
            LIFE-=1
            ball.goto(0,0)
            ball.move()

        else:
            Game_over()
            print("game over")
            break
    screen.update()  # Update the screen after all movements and checks

screen.exitonclick()