#!/usr/bin/env python
import turtle
import random
aj=turtle.Pen()
y=0
aj.speed(1)
turtle.screensize(600,800)
turtle.bgcolor("black")
aj.shape("turtle")
aj.pensize(10)

x=aj.xcor()
for each in range(1,2,1):
    
    aj.color(random.random(),random.random(),random.random())
    aj.goto(random.randint(0,600)-300, random.randint(0,800) - 400 )
