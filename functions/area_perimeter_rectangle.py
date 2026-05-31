length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))
def calculate_perimeter(length, breadth):
  perimeter = 2 * (length + breadth)
  return perimeter
def calculate_area(length, breadth):
  area = length * breadth
  return area
perimeter = calculate_perimeter(length, breadth)
area = calculate_area(length, breadth)
print(f"Perimeter of the rectangle is: {perimeter}")
print(f"Area of the rectangle is: {area}")