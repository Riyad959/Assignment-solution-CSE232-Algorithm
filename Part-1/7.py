def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = area(length, width)
perimeter = perimeter(length, width)

print(f"The area is: {area}")
print(f"The perimeter is: {perimeter}")