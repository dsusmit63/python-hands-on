def sum_of_two_numbers(num1,num2):
  print(f"Sum of {num1} and {num2} is {num1 + num2}")
def sub_of_two_numbers(num1,num2):
  if (num2 > num1):
    print(f"Subtraction of {num2} and {num1} is {num2 - num1}")
  else:
    print(f"Subtraction of {num1} and {num2} is {num1 - num2}")
def mul_of_two_numbers(num1, num2):
  print(f"Multiplication of {num1} and {num2} is {num1 * num2}")
def div_of_two_numbers(num1,num2):
  if(num2 > num1):
    print(f"Division of {num2} and {num1} is {int(num2 /num1)}")
  else:
    print(f"Division of {num1} and {num2} is {int(num1 / num2)}")
for i in range(3):
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  choice = input("Enter operation choice (+,-,*,/): ")
  env = input("Enter environment(dev/stg/prd): ")
  if (env == "prd"):
    if (choice == "+"):
      sum_of_two_numbers(num1, num2)
    elif (choice == "-"):
      sub_of_two_numbers(num1, num2)
    elif (choice == "*"):
      mul_of_two_numbers(num1, num2)
    elif (choice == "/"):
      div_of_two_numbers(num1, num2)
    else:
      print("Invalid operation.Try again!")
  else:
    print("You are in non-prd environment")