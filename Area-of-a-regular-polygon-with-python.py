# At first I use math module
import math

# Get input for number of sides and length of sides
n = float(input("Please enter the number of sides: "))
s = float(input("Please enter the length of sides: "))

 
#Let's calculate area of a regular polygon
# Obviously I use this equal "π" = "math.pi" in formula and for tangent I use math.tan()
area = (n*s**2)/(4*math.tan(math.pi/n)) 

# output the result
print(f"The area of the polygon is: {area:.2f}")