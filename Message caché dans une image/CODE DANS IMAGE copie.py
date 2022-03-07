from PIL import Image
print ("L'image utilisée devra etre nomée 'image.png' dans le dossier du programme")

img = Image.open("/Users/nono/Documents/image codée/image.png")
img = img.convert("L")


l = input('Rentre ta phrase à cacher, max:255 caractères : ')

z = l.replace(" ","_")

r = list(z)

w = len(r)

k = int(input('rentre un niveau de protection entre 1 et 30 : '))

img.putpixel((0,0),(k,k,k))

img.putpixel((1,0), (w,w,w))
for x in range(w):
    v = ord(r[x])
    img.putpixel((x*k+2,0), (v,v,v))






img.save("/Users/nono/Documents/image codée/image1.png")
