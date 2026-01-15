import time
from tkinter import PhotoImage
import turtle as tm

screen = tm.Screen()
screen.setup(width=600, height=600)
screen.title("poop dodge by jh")
screen.bgcolor("skyblue")
screen.tracer(0)


shape_names={"down":[],"left":[],"up":[],"right":[]}
#총 16장의 이미지 등록 하는 반복문
#i가 0~3까지 변하는 반복문(4회전)
for i,shape_item in enumerate(shape_names.items()) :
    direction,names =shape_item
    #4장의 이미지생성:j가 1부터 4까지 변하는 반복문(4회전)
    for j in range(1,5):#1,2,3,4
        path=f"player{i}{j}.png"
        photo=PhotoImage(file=path).subsample(2,2)
        img=tm.Shape("image",photo)
        shape_name=f"player{i}{j}"
        screen.addshape(shape_name, img)
        names.append(shape_name)

#print(shape_names)
#플레이어
player = tm.Turtle()
player.shape(shape_names['down'][0])
player.penup()
player.sety(-250)

#상태 변수
current_dir="down"
frame_index=0
move_speed=10

#함수
def update_character(dir):
    global frame_index, current_dir

    current_dir=dir
    frame_index = (frame_index+1)%4

    #등록된 이름으로 이미지 변경
    player.shape(shape_names[current_dir][frame_index])

    #이동
    x=player.xcor()
    y=player.ycor()
    pos=280
    if dir=="up": 
        y += move_speed
        if y>pos:y=pos     
    elif dir=="down": 
        y -= move_speed
        if y<-pos+10:y=-pos+10
    elif dir=="left": 
        x -= move_speed
        if x<-pos:x=-pos
    elif dir=="right": 
        x += move_speed
        if x>pos-5:x=pos-5
    
    player.goto(x,y)

    screen.update()

#키보드 이벤트 바인딩
screen.listen()
screen.onkeypress(lambda: update_character("up"), "Up")
screen.onkeypress(lambda: update_character("down"), "Down")
screen.onkeypress(lambda: update_character("left"), "Left")
screen.onkeypress(lambda: update_character("right"), "Right")

screen.update()
screen.mainloop()#코드 마지막 --이 코드 아래에 코드마세요