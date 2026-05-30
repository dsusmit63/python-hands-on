age = int(input("Enter your age: "))
isVoterCardHolder = input("Do you have voter card? (True/False)").lower()
if(age >= 18) and (isVoterCardHolder == "true"):
  print("You are eligible to vote")
else:
  print("You are not eligible to vote")
