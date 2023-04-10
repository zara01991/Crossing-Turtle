from turtle import Turtle

class Score(Turtle):
    def __init__(self,score):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-270,180)
        self.write("LEVEL: ",False, align="center", font = ('Arial', 15, 'normal'))
        self.s = score
        self.goto(-245, 180)
        self.write(self.s,False, align ="center", font = ('Arial', 15, 'normal') )

    def add_score(self):
        #self.undo()
        self.goto(-235, 180)
        self.s +=1
        self.write(self.s, False, align="center", font=('Arial', 15, 'normal'))

    def game_over(self):
        self.write("GAME OVER", False, align="center", font=('Arial', 25, 'bold'))