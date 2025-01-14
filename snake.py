from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments=[]

        self.create_snake()


    def create_snake(self):
        x = -20
        for i in range(3):

            y=0
            segment=Turtle('square')
            segment.color('green')
            segment.penup()
            segment.goto(x,y)
            self.segments.append(segment)
            x-=20


    def move_snake(self):
        for num in range(len(self.segments)-1,0,-1):
            x=self.segments[num-1].xcor()
            y = self.segments[num-1].ycor()
            self.segments[num].goto(x,y)

        self.segments[0].forward(20)

    def grow(self):
        x=self.segments[len(self.segments)-1].xcor()
        y = self.segments[len(self.segments)-1].ycor()
        segment = Turtle('square')
        segment.color('green')
        segment.penup()
        segment.goto(x, y)
        self.segments.append(segment)


    def hit_wall(self):
        if self.segments[0].xcor()>=300 or self.segments[0].xcor()<=-300 or self.segments[0].ycor()>=300 or self.segments[0].ycor()<=-300:
            return True


    def up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def hit_body(self):
        for segment in self.segments:

            if self.segments[0].distance(segment)<15:
                if segment==self.segments[0]:
                    continue
                return True


    def respawn(self):
        for segment in self.segments:
            segment.goto(10000,10000)

        self.segments.clear()


        self.create_snake()





