from turtle import Turtle
MOVE_FORWARD = 20
x = 0
y = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_turtle()
        self.head = self.segments[0]

    def create_turtle(self):
        for pos in range(3):
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(x, y)
            self.segments.append(new_turtle)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
            print(i)
        self.head.forward(MOVE_FORWARD)

    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)
