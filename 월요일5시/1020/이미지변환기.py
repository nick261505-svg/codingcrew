from PIL import Image

# PNG를 GIF로 변환
img = Image.open("1020/recycle.png")
img.save("1020/recycle.gif")
print("파일변환 완료!")