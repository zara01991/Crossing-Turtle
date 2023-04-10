from turtle import Turtle, Screen
from littleturtle import LittleTurtle
from cars import Cars
import time
import random

screen = Screen()
screen.setup(width = 600, height = 400)
screen.title("Crossing Turtle Game")
screen.tracer(0)


t = LittleTurtle()
n = random.randint(10,20)
carlist= []


for i in range(0,n):
    c = Cars()
    carlist.append(c)

game_over = False




while not game_over :
    screen.update()
    time.sleep(0.2)

    t.turtle_move()

    while level_up:
        if t.ycor() >= 280:
            




    i = 0
    while not game_over  and i < len(carlist):

        c = carlist[i]
        c1 = c.segment[0]
        c2 = c.segment[1]
    

        if t.distance(c1)<15 or t.distance(c2)<15:
        #if str(t.position())== str(c1.position()) or str(t.position()) == str(c2.position()):
            game_over = True
            print('game over')
            
        else:
            if c1.xcor()<=-340:
                n = random.randint(-180,180)
                c1.goto(300,n)
                c2.goto(320,n)

            else:
                carlist[i].car_move()
            
            i += 1
        
     


               
        
           
            


screen.exitonclick()