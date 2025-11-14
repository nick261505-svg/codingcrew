import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(2)

line=300
t.backward(line/2)

for i in range(3):
    t.forward(line) 
    t.right(360/3)

t.forward(line/3)
t.left(60)
t.forward(line/3)

for i in range(3):
    t.right(360/3)
    t.forward(line)

turtle.done()