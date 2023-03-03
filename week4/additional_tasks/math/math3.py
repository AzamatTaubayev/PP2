import math

def area_of_regular_polygon(n, l):
    
    area = (n * l**2) / (4 * math.tan(math.pi/n))
    return int(area)

n = int(input())   
l = int(input()) 
area = area_of_regular_polygon(n, l)
print(area)
