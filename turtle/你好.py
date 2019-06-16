# -*- coding: utf-8 -*-
# Time    : 2019/4/5 22:44
# Author  : Mifen
# Email   : 2952277346@qq.com
# Github  : https://github.com/Amd794


from turtle import *
import random
import time

str_ = """
钱睿森在育秀实验小雪
钱睿森在育秀实验小雪
钱睿森在育秀实验小雪
钱睿森在育秀实验小雪
钱睿森在育秀实验小雪
""".split("。")
#setup(1280,720)  # 设置窗口大小
setup(1280,720)  # 设置窗口大小
colormode(255)  # 使用的颜色模式, 整数还是小数
up()
a, b = -500, 280
goto(a,b)
bgcolor("black")


down()
def write_chinese(str_,b):
    bgcolor( random.randint(0,255),random.randint(0,255),random.randint(0,255))  # 随机生成RGB值, 每次调用函数改变背景颜色
    up()
    #goto(200,b)
    down()
    size =  random.randint(12,24)  # 随机字体大小
    color( random.randint(0,255),random.randint(0,255),random.randint(0,255))  # 随机字体颜色
    write(str_, align="center",font=("楷体",size))
    up()
        

    
goto(-600,300)
write_chinese("你好",18)
#up()
color("#262626;")
goto(-600,250)
write('Author:Mifen',font=("微软雅黑", 18))
goto(-600,200)
write('E-mail :2952277346@qq.com',font=("微软雅黑", 18))
goto(-600, 150)
write('Code :https://github.com/Amd794/Python123', font=("微软雅黑", 18))
goto(-600,-350)
down()
time.sleep(60)
ht()
