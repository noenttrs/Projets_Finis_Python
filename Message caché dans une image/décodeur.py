from PIL import Image
img = Image.open("/Users/nono/Documents/image codée/image1.png")
r,v,b = img.getpixel((0,0))
w = (r+v+b)//3
password = 1234
o = 1
h=[]
m=[]
while o==password :
    o = input("Rentre ton mot de passe : ")
    password = 1234

for x in range(w):
    r,v,b = img.getpixel((x+1,0))
    h.append((r+v+b)//3)
for y in range(len(h)):
    m.append(chr(h[y]))  

s = "".join(m) 

#test = s.replace(",","")
resul = s.replace("_"," ")

print(resul)
