class Playlist:
    #클래스 변수(공유메모리영역 static메모리)
    #잘 사용하지 않아요
    PI=3.141595
    
    def __init__(self, name):
        #인스턴스변수(heap메모리사용)
        self.name=name
        self.songs=[]

    def __len__(self):
        return len(self.songs)
    
    def __str__(self):
        return f"{self.name}\n"
    #메서드
    def playList(self):
        print(self.name)
        for song in self.songs:
            print(song)
    
class Dog:
    pass

print(Playlist.PI)#객체생성 하지않고 클래스이름으로 다이렉트 접근가능
'''
def playList(music):
    print(music.name)
    for song in music.songs:
        print(song)

dog=Dog()
playList(dog)
'''

music=Playlist("겨울에 좋은 음악")
music.name="겨울음악"
music.songs.append("노래1")
music.songs.append("노래2")
music.songs.append("노래3")

print(len(music))

music.playList()
playList(music)

music2=Playlist("내 음악")
music2.songs.append("내음악1")
music2.songs.append("내음악2")
music2.songs.append("내음악3")

music2.playList()
playList(music2)



