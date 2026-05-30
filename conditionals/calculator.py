num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
operation = input("Enter operation(+,-,*,/,%): ")
match operation:
  case "+":
    sum_result = num1 + num2
    print(f"Sum Result: {sum_result}")
  case "-":
    sub_result = num1 - num2
    print(f"Subtraction Result: {sub_result}")
  case "*":
    mul_result = num1 * num2
    print(f"MultiplicationResult: {mul_result}")
  case "/":
    if num2 == 0:
      print("Division by zero is not allowed")
    else:
      div_result = num1 / num2
      print(f"Division Result: {div_result}")
  case "%":
    if num2 == 0:
      print("Modulo by zero is not allowed")
    else:
        mod_result = num1 % num2
        print(f"Mod Result: {mod_result}")      
  case _:
    print("Invalid operation")