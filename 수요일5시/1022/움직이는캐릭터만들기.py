import turtle

sc=turtle.Screen()
sc.title("화살표 키로 터틀 이동하기")
sc.setup(width=800,height=600)

#터틀설정
t=turtle.Turtle()
t.shape("turtle")
t.color("green")
t.shapesize(2,2)
t.speed(0)

speed=3
moving={
    "up":False,
    "down":False,
    "left":False,
    "right":False
}
#######################
#키를 누른상태 일때
def press_up():
    moving["up"]=True

def press_down():
    moving["down"]=True

def press_left():
    moving["left"]=True

def press_right():
    moving["right"]=True
########################
#키를 눌렀다가 올라올때
def release_up():
    moving["up"]=False

def release_down():
    moving["down"]=False

def release_left():
    moving["left"]=False

def release_right():
    moving["right"]=False


sc.listen()
sc.onkeypress(press_up,"Up")
sc.onkeypress(press_down,"Down")
sc.onkeypress(press_left,"Left")
sc.onkeypress(press_right,"Right")
sc.onkeyrelease(release_up,"Up")
sc.onkeyrelease(release_down,"Down")
sc.onkeyrelease(release_left,"Left")
sc.onkeyrelease(release_right,"Right")

def game_loop():
    #현재 이동상태에 따라 터틀이동
    if moving["up"]:
        t.sety(t.ycor()+speed)
    if moving["down"]:
        t.sety(t.ycor()-speed)

    if moving["left"]:
        t.setx(t.xcor()-speed)
    if moving["right"]:
        t.setx(t.xcor()+speed)
    
    sc.update()
    sc.ontimer(game_loop, 20)

sc.tracer(0)
#게임루프 실작
game_loop()

#화면 유지
sc.mainloop()