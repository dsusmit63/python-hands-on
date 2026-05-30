number = int(input("Enter the number: "))
if number == 0:
  print("You have entered 0, please enter a non-zero value")
elif number % 3 == 0 and number % 5 == 0:
    print("Number is divisible by both 3 and 5")
else:
    print("Number is not divisible")