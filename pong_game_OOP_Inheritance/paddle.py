from turtle import Turtle
import time

class Paddle(Turtle): #Inheritance

    def __init__(self, pl): #object properties
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.turtlesize(stretch_len=5)
        self.goto(350*pl, 0)

    def up(self):   # methods responsible for changing the position of the paddle,using inherited methods from Turtle
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)