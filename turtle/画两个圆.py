#!/usr/bin/env python
import turtle
import random
aj=turtle.Pen()
y=0
aj.speed(1)
turtle.screensize(600,800)
turtle.bgcolor("blue")
aj.shape("turtle")
aj.hideturtle()
aj.pensize(3)

for each in range(1,3,1):
    
    aj.color("white")
    aj.goto(random.randint(0,600)-300, random.randint(0,800) - 400 )
	
    aj.color("red")
    aj.circle(100,360)
	
    
		
