from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POSITIONS:
            self.add_seg(pos)

    def add_seg(self, position):
        snake_part = Turtle()
        snake_part.penup()
        snake_part.shape("square")
        snake_part.color("white")
        snake_part.setpos(position)
        self.segments.append(snake_part)

    def extent(self):
        self.add_seg(self.segments[-1].pos())

    def move(self):
        for snake_seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_seg - 1].xcor()
            new_y = self.segments[snake_seg - 1].ycor()
            self.segments[snake_seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
