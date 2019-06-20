"""turtledemo.two_canvases

Use TurtleScreen and RawTurtle to draw on two
distinct canvases in a separate windows. The
new window must be separately closed in
addition to pressing the STOP button.
"""
# 对称的两个乌龟 

from turtle import TurtleScreen, RawTurtle, TK

def main():
    root = TK.Tk()
    cv1 = TK.Canvas(root, width=300, height=200, bg="#ddffff")
    cv2 = TK.Canvas(root, width=300, height=200, bg="#ffeeee")
    cv1.pack()
    cv2.pack()

    s1 = TurtleScreen(cv1)
    s1.bgcolor(0.85, 0.85, 1)
    s2 = TurtleScreen(cv2)
    s2.bgcolor(1, 0.85, 0.85)

    p = RawTurtle(s1) #上面的乌龟
    q = RawTurtle(s2) #下面的乌龟

    p.color("red", (1, 0.85, 0.85))
    p.width(3)
    q.color("blue", (0.85, 0.85, 1))
    q.width(3)

    for t in p,q:
        t.shape("turtle")
        t.left(36)

    q.left(180)

    for t in p, q:
        t.begin_fill()

    for i in range(5): #画五边形
        for t in p, q:
            t.forward(50)
            t.left(72)

    for t in p,q:
        t.end_fill()
        t.left(54)
        t.penup()
        t.back(50)

    return "EVENTLOOP"


if __name__ == '__main__':
    main()
    TK.mainloop()  # keep window open until user closes it
