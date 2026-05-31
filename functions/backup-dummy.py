def backup_server():
  print("Backup script running ...")
  print("Backup successfull...")
day = input("Enter week day: ").lower()
if (day == "friday"):
  for i in range(1,4,1):
    backup_server()
else:
  print("Wait for friday...")