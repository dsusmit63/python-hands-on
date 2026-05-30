num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 == num2 == num3:
  print("All numbers are same")
elif num1 == num2 and num1 < num3:
  print("num1 and num2 is smallest")
elif num2 == num3 and num2 < num1:
  print("num2 and num3 is smallest")
elif num1 == num3 and num1 < num2:
  print("num1 and num3 is smallest ")
elif num1 <= num2 and num1 <= num3:
  print("num1 is smallest")
elif num2 <= num1 and num2 <= num3:
  print("num2 is samllest")
else:
  print("num3 is smallest")