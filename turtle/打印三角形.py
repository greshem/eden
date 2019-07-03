

# colormixer

from turtle import Screen, Turtle, mainloop



def setbgcolor():
    #screen.bgcolor(100,100,100)
    screen.bgcolor("grey")
def main():
    global screen, red, green, blue
    screen = Screen()
    screen.delay(0)
    screen.setworldcoordinates(-1, -0.3, 3, 1.3)

    #red = ColorTurtle(0, .5)
    #green = ColorTurtle(1, .5)
    #blue = ColorTurtle(2, .5)
    setbgcolor()

    writer = Turtle()
    writer.ht()
    writer.pu()
    writer.goto(1,0.3)

    #writer.write("DRAG!",align="center",font=("Arial",30,("bold","italic")))
	
    #writer.write("我们毕业了！", align="center", font=("微软雅黑", 40, "bold"))
    writer.write("我们毕业了！", align="center", font=("宋体", 40, "bold"))
	
    writer.goto(1,0.5)
    writer.write("我们毕业了！", align="center", font=("微软雅黑", 40, "bold"))
    
    writer.goto(1,0.7)
    writer.write("我们毕业了！", align="center", font=("楷体", 40, "bold"))

    writer.pendown()
    writer.goto(0,0)
    writer.color("red")
    writer.circle(2,360)
    return "EVENTLOOP"
	
	
	


if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()

