import turtle

i = 0
j=0

wn = turtle.Screen()

turtle.position()
(0.00,0.00)

rosie = turtle.Turtle()
rosie.shape("turtle")
rosie.color("black")
rosie.speed(100)

for i in range (0,71):
	for j in range (0,5):
	    rosie.forward(100)
	    rosie.right(72)
	rosie.right(5)
    
wn.exitonclick()
