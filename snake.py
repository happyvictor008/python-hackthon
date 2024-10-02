from turtle import  Turtle, Screen
import time

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.initial_snake()
        self.head = self.segments[0]


    def initial_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[num - 1].xcor()
            new_y = self.segments[num - 1].ycor()
            self.segments[num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)


    def extend(self):
        self.add_segment(self.segments[-1].position())




    def up(self):
        if self.head.heading != UP:
            self.head.setheading(90)
    def down(self):
        if self.head.heading != DOWN:
            self.head.setheading(270)
    def left(self):
        if self.head.heading != LEFT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading != RIGHT:
            self.head.setheading(0)