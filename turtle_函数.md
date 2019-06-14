
# 行动  Move and draw

    | forward | fd   |往前 
    | backward | bk | back |后退
    | right | rt  |右转
    | left | lt   |左转
    | goto | setpos | setposition |到什么地方 
    | setx |设置 x 的位置
    | sety | 设置y的位置
    | setheading | seth  |头的方向
    | home  |到中心位置
    | circle | 画圆
    | dot   |画点
    | stamp
    | clearstamp
    | clearstamps
    | undo
    | speed  |调整速度

# 行动  Tell Turtle state

    | position | pos  |获取当前位置
    | towards       |获取当前方向
    | xcor
    | ycor
    | heading   |获取头部方向
    | distance  |获取距离

# 行动  Setting and measurement

    | degrees  |角度
    | radians


# 画笔   Drawing state

    | pendown | pd | down   |画笔按下去
    | penup | pu | up       |画笔收起爱
    | pensize | width       |画笔的粗细
    | pen
    | isdown                |画笔按下去了吗

# 画笔   Color control

    | color     |设置颜色
    | pencolor
    | fillcolor |用颜色填充

# 画笔   Filling

    | filling
    | begin_fill
    | end_fill

# 画笔   More drawing control

    | reset |重置
    | clear |清空
    | write |写字



# 乌龟状态   Visibility

    | showturtle | st  |显示乌龟
    | hideturtle | ht  |隐藏乌龟
    | isvisible

# 乌龟状态  Appearance

    | shape     |乌龟的形状
    | resizemode
    | shapesize | turtlesize
    | shearfactor
    | settiltangle
    | tiltangle
    | tilt
    | shapetransform
    | get_shapepoly

# 乌龟Using events

    | onclick   |点击乌龟
    | onrelease |释放乌龟
    | ondrag    |拖拽乌龟

# 乌龟Special Turtle methods

    | begin_poly    |开始多边形
    | end_poly
    | get_poly
    | clone
    | getturtle | getpen
    | getscreen
    | setundobuffer
    | undobufferentries


Methods of TurtleScreen/Screen
------------------------------

# Window control

    | bgcolor   |背景颜色
    | bgpic     |背景图片
    | clear | clearscreen |清空背景
    | reset | resetscreen |重置背景
    | screensize          |背景大小
    | setworldcoordinates

# Animation control

    | delay     |延迟
    | tracer   
    | update

# Using screen events

    | listen
    | onkey | onkeyrelease
    | onkeypress        |键盘按下去
    | onclick | onscreenclick
    | ontimer           |时间触发器
    | mainloop | done

# Settings and special methods

    | mode
    | colormode         |颜色模式
    | getcanvas
    | getshapes
    | register_shape | addshape  |添加形状
    | turtles
    | window_height
    | window_width

# Input methods

    | textinput |文字输入
    | numinput  |数值输入

# Methods specific to Screen

    | bye       |再见
    | exitonclick
    | setup
    | title     |标题

