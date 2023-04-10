from turtle import Turtle, Screen

screen = Screen()
class LittleTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.penup()
        self.goto(0,-180)
        self.left(90)
        self.showturtle()


    def move_forward(self):
        self.forward(10)

    def turtle_move (self):
        screen.listen()
        screen.onkey(key = "Up", fun = self.move_forward)
