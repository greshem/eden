#!/usr/bin/env python
import turtle
import random
aj=turtle.Pen()
y=0
aj.speed(5)
turtle.screensize(600,800)
turtle.bgcolor("black")
aj.shape("turtle")

x=aj.xcor()
for each in range(1,100,1):
    
    aj.color(random.random(),random.random(),random.random())

    aj.penup()
    aj.goto(random.randint(0,600)-300, random.randint(0,800) - 400 )
    aj.pendown()



    aj.begin_fill()

    aj.circle(random.randint(0,200),360) #随机画一个 半径在0-200的圆
	
    aj.end_fill()
		
