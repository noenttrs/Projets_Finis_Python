from PIL import Image
print ("L'image utilisée devra etre nomée 'image.png' dans le dossier du programme")

img = Image.open("/Users/nono/Documents/image codée/image.png")

l = input('Rentre ta phrase à cacher, max:255 caractères : ')

z = l.replace(" ","_")

r = list(z)

w = len(r)

img.putpixel((0,0), (w,w,w))
for x in range(w):
    v = ord(r[x])
    img.putpixel((x+1,0), (v,v,v))






img.save("/Users/nono/Documents/image codée/image1.png")
