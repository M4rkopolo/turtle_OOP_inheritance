from turtle import Turtle
import random
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slow")
        self.penup()
        self.direction = 1
        self.x_move = 10 
        self.y_move = 10 
        self.move_speed = 0.1

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def bounce(self):
        self.y_move *= -1
        
    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

