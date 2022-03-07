from PIL import Image
img = Image.open("/Volumes/NOÉ NOTTARI/Image codée/image1.png")
r,v,b = img.getpixel((0,0))
j = (r+v+b)//3

print(r,v,b)
print(j)