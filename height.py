import math

def height(x,a):
    ar=math.radians(a)
    ht=x*math.tan(ar)
    return ht

x=int(input("Enter distance of user from building:"))
a=int(input("Enter degree or angle:"))

h=height(x,a)
print("Height:",h*0.30)