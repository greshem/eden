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


    
goto(-600,300)
color("white")
write('你好',font=("微软雅黑", 18))
#up()

goto(-600,250)
write('Author:Mifen',font=("微软雅黑", 18))

goto(-600,200)
write('E-mail :2952277346@qq.com',font=("微软雅黑", 18))

goto(-600, 150)
write('Code :https://github.com/Amd794/Python123', font=("微软雅黑", 18))


#time.sleep(60)
hideturtle()
text=textinput("DDDDDDD", "FFFFF")
