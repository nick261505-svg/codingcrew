import turtle
s=turtle.Screen()
s.setup(width=800,height=600)
s.title("자기이름")
s.register_shape("1113/alien.png")

c=turtle.Turtle()
c.shape("turtle")
c.shapesize(2,2)
c.penup()

speed=10
def 왼쪽이동():
    #현재x좌표
    x=c.xcor()-speed
    #x값이 -380을 넘어가면 화면밖으로 나감
    if x < -380:
        x=-380
    c.setx(x)


s.listen()
s.onkeypress(왼쪽이동,"Left")







turtle.done()