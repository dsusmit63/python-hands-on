a = int(input("Enter first side of your triangle: "))
b = int(input("Enter second side of your triangle: "))
c = int(input("Enter third side of your triangle: "))

if (a + b > c) and (b + c > a) and (a + c > b):
  print("Your triangle is valid")
else:
  print("Your triangle is not valid")