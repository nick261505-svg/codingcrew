from PIL import Image

# PNG를 GIF로 변환
img = Image.open("1014/turtle.png")
img.save("1014/turtle.gif")
print("파일변환 완료!")