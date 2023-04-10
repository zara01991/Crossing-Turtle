from turtle import * #Turtle, Screen
import random

colormode(255)

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        segments = []
        #screen = Screen()
        self.hideturtle()
        #self.penup()
        y = random.randint(-150,180)
        x = random.randint(-300,300)

        cr = random.randint(0,254)
        cg = random.randint(0,254)
        cb = random.randint(0,254)

        c = (cr,cg,cb)

        for i in range(0,2):
            
            t = Turtle(shape = "square")
           
            t.hideturtle()
            t.penup()
            #t.speed(10)
            t.goto (x + i * 20, y)
            #t.goto (250, -150)
            t.left(180)
            t.color(c)
            t.showturtle()
            #self.left(180)
           # self.showturtle()
            
            segments.append(t)
        
        #screen.update()
        self.segment = segments
   


    def car_move (self):
        for s in self.segment:
            s.forward(10)

                     
        


    # def car_keep_moving (self):
    #     self.segment.showturtle()
    #     self.segment.speed(1)

    #     while 1!=0:
    #         self.segment.car_move_step()