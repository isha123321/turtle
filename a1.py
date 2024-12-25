import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(600,700)
turtle.Screen().title("turtle")
my_pen=turtle.Turtle()
size=0
while True:
    for i in range(360):
        my_pen.forward(1)
        my_pen.right(1)
    

turtle.done()
