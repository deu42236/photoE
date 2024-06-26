from PIL import Image
import time

def filter1():
    x = 0
    for x in range(sirka):
        y = 0
        for y in range(vyska):
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (r , b, r))
            if prumer > 100:
                obrazek.putpixel((x,y), (255, 255, 255))
            else:
                obrazek.putpixel((x,y), (0, 0, 0))
#-------------------------------------------------------------
def filter2():
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
#-------------------------------------------------------------
def filter3():
    x = 0
    for x in range(sirka):
        y = 0
        for y in range(vyska):
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (70-r , 70-g, 98-b))
#-------------------------------------------------------------



pic = "trouba.jpg"
obrazek = Image.open(pic)
sirka, vyska = obrazek.size
print("Would you like to choose your own picture?")
if  input("yes or no: ") == "yes":
    pic = input("Enter the name of the picture: ")
    obrazek = Image.open(pic)
    sirka, vyska = obrazek.size
else:
    obrazek = Image.open(pic)
    sirka, vyska = obrazek.size
    print("Ok, we chose the picture for you. It is called 'trouba.jpg' and it is in the same folder as this program.")

inp = input("Choose filter 1, 2 or 3: ")
start_time = time.time()
if inp == "1":
    filter1()
elif inp == "2":
    filter2()
elif inp == "3":
    filter3()
else:
    print("Wrong input")

print("ok")
end_time = time.time()
print(f"Runtime of the program is {end_time - start_time}")

obrazek.show()
##display(obrazek)

start_time = time.time()