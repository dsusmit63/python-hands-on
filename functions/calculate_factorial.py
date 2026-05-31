number = int(input("Enter the number: "))
def calculate_factorial(number):
  factorial_result = 1
  for num in range(number, 0, -1):
    factorial_result = factorial_result * num
  return factorial_result
if number < 0:
  print("Factorial is not defined for negative numbers")
else:
  print(f"Factorial Result: {calculate_factorial(number)}")



