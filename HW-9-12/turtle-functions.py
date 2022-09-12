#hexagon() -- this should have the same parameters as square and triangle but should draw a hexagon.
#(t,numsides,x,y,color,width,sidelen) - this will draw a regular ngon with numsides sides.

import turtle

wn = turtle.Screen()
crush = turtle.Turtle()

def hexagon(t,numsides,x,y,color,width,sidelen):
  t.penup()
  t.goto(x,y)
  t.color(color)
  t.width(width)
  t.pendown()
  for i in range(6):
    t.forward(sidelen)
    t.right(60)
    

hexagon(crush,6,100,100,"blue",10,69)

wn.exitonclick()
wn.mainloop()

  