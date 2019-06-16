#!/usr/bin/env python
import turtle
import random
turtle2=turtle.Pen()
y=0
turtle2.speed(5)
turtle.screensize(600,800)
turtle.bgcolor("white")
turtle2.shape("turtle")

x=turtle2.xcor()
for each in range(1,1000,1):
    
    turtle2.color(random.random(),random.random(),random.random())

    turtle2.home()
    turtle2.pendown()
    turtle2.showturtle()
    turtle2.goto(random.randint(0,600)-300, random.randint(0,800) - 400 )
    turtle2.penup()
    turtle2.hideturtle()
