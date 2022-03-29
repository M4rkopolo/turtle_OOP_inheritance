from turtle import Turtle , Screen
from paddle import Paddle 
from ball import Ball
from score_board import Score
import time

#Create a screen
screen = Screen()
height = 600
width = 800
screen.setup(width=width, height=height)
screen.bgcolor("black")
screen.title("My snake game")
screen.delay(0)
#creating ball and two players 
player_one = Paddle(1)
player_two = Paddle(-1)
ball = Ball()
#keep score
score = Score()
screen.listen()
#control of paddles 
screen.onkeypress(key="Up", fun=player_one.up)
screen.onkeypress(key="Down", fun=player_one.down)
screen.onkeypress(key="w", fun=player_two.up)
screen.onkeypress(key="s", fun=player_two.down)
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detecting collision witch wall 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    #detecting colliaoon witch the paddle
    if ball.xcor() > 320 and ball.distance(player_one) < 50 or ball.xcor() < -320 and ball.distance(player_two) < 50:
        ball.paddle_bounce()
    #detecting collision when miss the paddle
    if ball.xcor() > 390:
        ball.goto(0, 0)
        score.l_point()
    if ball.xcor() < -390:
        ball.goto(0, 0)
        score.r_point()

screen.exitonclick()