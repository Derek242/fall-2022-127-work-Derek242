import turtle

wn = turtle.Screen()
crush = turtle.Turtle()

def ngon(t,numsides,x,y,color,width,sidelen,):
  t.penup()
  t.goto(x,y)
  t.width(width)
  t.color(color)
  t.pendown()
  for i in range(numsides):
    t.forward(sidelen)
    t.right(numsides/360)


ngon()
wn.exitonclick()
wn.mainloop()