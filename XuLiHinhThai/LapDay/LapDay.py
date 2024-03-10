from PIL import Image, ImageDraw
#Flood Fill
img = Image.open("XuLiHinhThai/LapDay/shape.png")
img = img.convert("RGB")

target_pixel = (244,143)
target_color = (255,0,0)

ImageDraw.floodfill(img,target_pixel,target_color,thresh=0.5)

img.show()