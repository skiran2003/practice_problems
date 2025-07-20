import math


def paint_cans(height,width,coverage):
    area=(height*width)/2
    no_of_cans=math.ceil(area/coverage)
    print(no_of_cans)

h=int(input("Enter height of the wall in meters:"))
w=int(input("Enter width of the wall in meters:"))
c=7
paint_cans(height=h,width=w,coverage=c)
