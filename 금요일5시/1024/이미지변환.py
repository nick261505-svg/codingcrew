from PIL import Image

# PNG를 GIF로 변환
img = Image.open("1024/ai-generated.png") # 'RGBA' 모드로 열림

# 원본 픽셀크기를 변경하기(가로,세로)
new_size=(100,100*640//588)
img_resized=img.resize(new_size) # 여전히 'RGBA' 모드

# --------------------
# RGBA 모드를 GIF가 지원하는 'P' (Palette) 모드로 변환합니다.
# palette=Image.Palette.ADAPTIVE 옵션은 원본 이미지에 최적화된
# 색상 팔레트를 생성하고, 알파 채널(투명도)을
# GIF의 단일 투명 인덱스로 자동 변환해 줍니다.
img_palette = img_resized.convert('P', palette=Image.Palette.ADAPTIVE)
# --------------------

# 'P' 모드로 변환된 이미지를 저장
img_palette.save("1024/ai-generated2.gif")
print("파일변환 완료!")