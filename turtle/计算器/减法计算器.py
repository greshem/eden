# -*- coding: utf-8 -*-
# Time    : 2019/4/5 22:44
# Author  : Mifen
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794


from turtle import *
import random
import time


#setup(1280,720)  # 设置窗口大小
setup(1280,720)  # 设置窗口大小
colormode(255)  # 使用的颜色模式, 整数还是小数
up()
a, b = -500, 280
goto(a,b)
bgcolor("black")


down()


    


#time.sleep(60)
hideturtle()
a=textinput("减法计算器", "被减数")
b=textinput("减法计算器", "减数")
c=int(a)-int(b)
textinput("减法计算器", "结果是%s"%c)
