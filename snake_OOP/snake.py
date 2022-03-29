#GLOBAL VARIABLES
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
N = 0
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

from turtle import Turtle
from food import Food

class Snake(Turtle):    #inheritance parent is a Turtle

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def walk(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.snake_head.forward(20)

    def hit_the_tail(self):
        if self.segments[0].pos() in STARTING_POSITION:
            self.reset()

    def reset(self):
        for _ in self.segments:
            _.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]

    def UP(self):
        self.snake_head.setheading(UP)
    def DOWN(self):
        self.snake_head.setheading(DOWN)
    def LEFT(self):
        self.snake_head.setheading(LEFT)
    def RIGHT(self):
        self.snake_head.setheading(RIGHT)
