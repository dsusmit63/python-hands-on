num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
num3 = float(input("Enter num3: "))

if num1 == num2 == num3:
  print("All numbers are same")
elif num1 >= num2 and num1 >= num3:
  print("num1 is largest")
elif num2 >= num1 and num2 >=num3:
  print("num2 is largest")
else:
  print("num3 is largest")
  