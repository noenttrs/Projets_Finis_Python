from PIL import Image
img = Image.open("/Users/nono/Documents/image codée/image1.png")
r,v,b = img.getpixel((0,0))
k = (r+v+b)//3
r,v,b = img.getpixel((1,0))
w = (r+v+b)//3

mdp = 1234
h=[]
m=[]
"""
while True : 
    o = int(input('Rentre ton mot de passe : '))
    if o == mdp :
        break
"""
for x in range(w):
    r,v,b = img.getpixel((x*k+2,0))
    h.append((r+v+b)//3)
for y in range(len(h)):
    m.append(chr(h[y]))  

s = "".join(m) 

#test = s.replace(",","")
resul = s.replace("_"," ")

print(resul)
