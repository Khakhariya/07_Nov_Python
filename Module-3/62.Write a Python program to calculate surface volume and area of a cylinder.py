import math

def cylinder_volume (radious,height) :
    cylinder_vol = math.pi*(radious*radious)* height
    return cylinder_vol

def cylinder_area (radious,height) :
    cylinder_ar = (2*math.pi*radious*height) + (2*math.pi*(radious*radious))
    return cylinder_ar

x = cylinder_volume (10,5)
y = cylinder_area(12,25)

print (f"Volume of cylinder is : {x}")
print (f"Area of cylinder is : {y}")