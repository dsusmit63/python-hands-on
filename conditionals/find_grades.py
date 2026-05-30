percentage_marks = float(input("Enter obtained percentage: "))
if percentage_marks >= 90 and percentage_marks <= 100:
  print("Grade AA")
elif percentage_marks >=80 and percentage_marks < 90:
  print("Grade A+")
elif percentage_marks >=60 and percentage_marks < 80:
  print("Grade A")
elif percentage_marks >= 50 and percentage_marks < 60:
  print("Grade B+")
elif percentage_marks >= 40 and percentage_marks < 50:
  print("Grade B")
elif percentage_marks >= 30 and percentage_marks < 40:
  print("Grade C")
elif percentage_marks < 30 and percentage_marks >= 0:
  print("Grade D: Failed")
else:
  print("Invalid")