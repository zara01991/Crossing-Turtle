from turtle import * #Turtle, Screen
from littleturtle import LittleTurtle
from cars import Cars
import time
import random
from score import Score



def game (level,s):
    s += 1
    score = Score(s)
    #score.add_score()
    screen = Screen()
    screen.setup(width = 600, height = 400)
    screen.title("Crossing Turtle Game")
    screen.tracer(0)
    colormode(255)

    t = LittleTurtle()
    n = random.randint(10,20)
    carlist= []
    

    for i in range(0,n):
        c = Cars()
        carlist.append(c)

    game_over = False

    while not game_over :
        screen.update()
        time.sleep(level)
        t.turtle_move()


        if t.ycor() < 180:
            i = 0
            while not game_over  and i < len(carlist):

                c = carlist[i]
                c1 = c.segment[0]
                c2 = c.segment[1]
            

                if t.distance(c1)<15 or t.distance(c2)<15:
                    game_over = True
                    score.home()
                    score.game_over()
                    
                else:
                    if c1.xcor()<=-340:
                        n = random.randint(-180,180)
                        c1.goto(300,n)
                        c2.goto(320,n)

                    else:
                        carlist[i].car_move()
                    
                    i += 1
        
        else:
            screen.clear()
            level = level * 0.5
            #score.add_score()
            game(level,s)
   
    screen.exitonclick() 
        

game(0.5,0)       



