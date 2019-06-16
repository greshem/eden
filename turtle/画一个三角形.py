#!/usr/bin/env python
import turtle
import random
aj=turtle.Pen()
y=0
aj.speed(1)
turtle.screensize(600,800)
turtle.bgcolor("black")
aj.shape("turtle")


    
aj.color(random.random(),random.random(),random.random())

aj.penup()
aj.goto(random.randint(0,600)-300, random.randint(0,800) - 400 )      
aj.pendown()



aj.begin_fill()

width=random.randint(1,200)
for number in range(0,3,1):
    aj.left(120)
    aj.forward(width)
    
	
	
aj.end_fill()
		
