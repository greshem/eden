#! /usr/bin/python3.6
"""       turtle-example-suite:

            tdemo_yinyang.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the circle
command.

"""

from turtle import *

def yin(radius, color1, color2):
    width(3)                #画笔为3
    color("black", color1)  #设置成黑色
    begin_fill()            #开始填充
    circle(radius/2., 180)  #画180度的一个半圆 半径为 radius/2
    circle(radius, 180)     #再
    left(180)
    circle(-radius/2., 180)
    end_fill()
    left(90)            #左转
    up()                #往上
    forward(radius*0.35) #往前面走
    right(90)            #右转
    down()               #往下走
    color(color1, color2) #用 color1  color2 填充 
    begin_fill()
    circle(radius*0.15)
    end_fill()
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)

def main():
    reset()
    yin(200, "black", "white")
    yin(200, "white", "black")
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()
