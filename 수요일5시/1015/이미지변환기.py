from PIL import Image

# PNG를 GIF로 변환
img = Image.open("1015/pokemon.png")

#원본 픽셀크기를 변경하기(가로,세로)
new_size=(50,50)
img_resized=img.resize(new_size)

img_resized.save("1015/pokemon.gif")
print("파일변환 완료!")