from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

SPEED = 0.6
screen = Screen()
height = 600
width = 600
screen.setup(width=width, height=height)
screen.bgcolor("black")
screen.title("My snake game")
screen.delay(0)
#instances 
snake = Snake()
food = Food()
score = Score()
screen.listen()
#interface
screen.onkey(key="Up", fun=snake.UP)
screen.onkey(key="Down", fun=snake.DOWN)
screen.onkey(key="Left", fun=snake.LEFT)
screen.onkey(key="Right", fun=snake.RIGHT)

finish = False
while not finish:
    snake.walk()
    time.sleep(0.1 * SPEED)
    #eating the food 
    if snake.snake_head.distance(food) < 15:
        food.new_food()
        score.increase_score()
        snake.extend()
        SPEED = 0.9
    #hitting the wall
    if snake.snake_head.xcor() > 250 or snake.snake_head.xcor() < -250 or snake.snake_head.ycor() > 250 or snake.snake_head.ycor() < -250:
        score.reset()
        snake.reset()
    #hitting the snake's tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()