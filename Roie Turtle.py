import turtle

repeat = 0

wn = turtle.Screen()

turtle.position()
(0.00,0.00)
rosie = turtle.Turtle()
rosie.shape("turtle")
rosie.color("pink")

for repeat in range (0,4):
    rosie.forward(50)
    rosie.right(72)

    
wn.exitonclick()
