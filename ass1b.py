# question

# Python program to take radius of a circle from the user. Calculate the area and
# perimeter of the circle and show the values up to 3 decimal points. E.g.
# Area = xx.xxx and Perimeter = yy.yyy.

radius = int(input("Enter the radius of the circle: "))
area = round(22/7 * radius * radius , 2)
perimeter = round(2 * 22/7 * radius, 2)
print("Area of the circle is: " + str(area))
print("Perimeter of the circle is: " + str(perimeter))


# Thing to learn : 
# alternative to print statements could be 
# print(f"Area of the circle is: {area}") --> in python newer versions
# round to restrict the decimal to 2 