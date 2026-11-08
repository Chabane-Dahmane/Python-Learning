import geometry 
shape = input("Enter the shape (square, rectangle, circle): ").lower()

if shape == "square":
    side = float(input("Enter the side: "))
    area = geometry.square_area(side)
elif shape == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = geometry.rectangle_area(length, width)
elif shape == "circle":
    radius = float(input("Enter the radius: "))
    area = geometry.circle_area(radius) 
else:
    print("Invalid shape")
    exit()

print("The area of the", shape, "is:", area)



