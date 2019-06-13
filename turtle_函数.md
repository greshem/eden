
行动  Move and draw
      | forward | fd  
      | backward | bk | back
      | right | rt
      | left | lt
      | goto | setpos | setposition
      | setx
      | sety
      | setheading | seth
      | home
      | circle
      | dot
      | stamp
      | clearstamp
      | clearstamps
      | undo
      | speed

行动  Tell Turtle state
      | position | pos
      | towards
      | xcor
      | ycor
      | heading
      | distance

行动  Setting and measurement
      | degrees
      | radians


画笔   Drawing state
      | pendown | pd | down
      | penup | pu | up
      | pensize | width
      | pen
      | isdown

画笔   Color control
      | color
      | pencolor
      | fillcolor

画笔   Filling
      | filling
      | begin_fill
      | end_fill

画笔   More drawing control
      | reset
      | clear
      | write



乌龟状态   Visibility
      | showturtle | st
      | hideturtle | ht
      | isvisible

乌龟状态  Appearance
      | shape
      | resizemode
      | shapesize | turtlesize
      | shearfactor
      | settiltangle
      | tiltangle
      | tilt
      | shapetransform
      | get_shapepoly

乌龟Using events
   | onclick
   | onrelease
   | ondrag

乌龟Special Turtle methods
   | begin_poly
   | end_poly
   | get_poly
   | clone
   | getturtle | getpen
   | getscreen
   | setundobuffer
   | undobufferentries


Methods of TurtleScreen/Screen
------------------------------

Window control
   | bgcolor
   | bgpic
   | clear | clearscreen
   | reset | resetscreen
   | screensize
   | setworldcoordinates

Animation control
   | delay
   | tracer
   | update

Using screen events
   | listen
   | onkey | onkeyrelease
   | onkeypress
   | onclick | onscreenclick
   | ontimer
   | mainloop | done

Settings and special methods
   | mode
   | colormode
   | getcanvas
   | getshapes
   | register_shape | addshape
   | turtles
   | window_height
   | window_width

Input methods
   | textinput
   | numinput

Methods specific to Screen
   | bye
   | exitonclick
   | setup
   | title

