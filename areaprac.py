#Area of rectangle

l=int(input("Enter the length of the rectangle: "))
b=int(input("Enter the breadth of the rectangle: "))
formula=l*b
print(f"The area of rectangle is {formula}.")

#Area of square

a=int(input("Enter the side of square: "))
area=a*a
print(f"The area of square is {area}.")

#area of triangle

height=int(input("Enter the height of the triangle: "))
base=int(input("Enter the base of the traingle: "))
area=1/2*(base*height)
print(f"The area of triangle is {area}.")

#area of circle

radius=int(input("Enter the radius of the circle : "))
area=3.14*radius**2
print(f"The area of circle is {area}.")
