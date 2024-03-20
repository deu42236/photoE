from PIL import Image
import time
start_time = time.time()

obrazek = Image.open("trouba.jpg")
sirka, vyska = obrazek.size
x = 0
for x in range(sirka):
    y = 0
    for y in range(vyska):
        r, g, b = obrazek.getpixel((x,y))
        prumer = int((r+g+b)/3)
        obrazek.putpixel((x,y), (r , b, r))
        if prumer > 100:
            obrazek.putpixel((x,y), (100, 255, 255))
        else:
            obrazek.putpixel((x,y), (0, 0, 0))
        y += 1
    x += 1
print("ok")
##display(obrazek)
end_time = time.time()
print(f"Runtime of the program is {end_time - start_time}")

obrazek.show()