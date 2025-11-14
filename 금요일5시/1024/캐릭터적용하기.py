import turtle

s=turtle.Screen()
s.setup(width=800, height=800)
s.register_shape("1024/ai-generated.gif")

사자=turtle.Turtle()
사자.penup()
사자.shape("1024/ai-generated.gif")

speed=20
def move_down():
    y=사자.ycor()-speed
    if y<-400+54: #-346
        y=-400+54
    사자.sety(y)

def move_up():
    y=사자.ycor()+speed
    if y > 400-54: #346
        y= 400-54
    사자.sety(y)

def move_right():
    x=사자.xcor()+speed
    if x > 346: #346
        x= 345
    사자.setx(x)

def move_left():
    x=사자.xcor()-speed
    if x < -346: #346
        x= -346
    사자.setx(x)

s.listen()
s.onkeypress(move_down,"Down")
s.onkeypress(move_up,"Up")
s.onkeypress(move_right,"Right")
s.onkeypress(move_left,"Left")

turtle.done()