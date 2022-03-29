import random
from turtle import Turtle

class Food(Turtle): 

    def __init__(self): # object properties
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.new_food()

    def new_food(self): #new_food go to random place on the screen
        self.goto(random.randrange(-200, 200), 
                  random.randrange(-200, 200))
