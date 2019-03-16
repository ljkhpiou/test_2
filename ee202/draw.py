import turtle
myPen = turtle.Turtle()
myPen.shape("arrow")

myPen.color("red")
#myPen.delay(5) #Set the speed of the turtle

#A Procedue to draw any regular polygon with 3 or more sides.
def drawPolygon(numberOfsides):
    exteriorAngle=360/numberOfsides
    length=2400/numberOfsides
    myPen.penup()
    myPen.goto(-length/2,-length/2)
    myPen.pendown()
    for i in range(0,numberOfsides):
        myPen.forward(length)
        myPen.left(exteriorAngle)


# Collect events until released
#with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener_m:
#    listener_m.join()
drawPolygon(6)
