env = input("Enter deployment environment(dev/stg/prd): ")
if env == "dev" or env == "stg" or env == "prd":
  number_of_instances = int(input(f"Enter number of ec2 instances you want to deploy in {env}: "))
  print(f"You have successfully deployed {number_of_instances} instances in {env}")
else:
  print("Enter valid environment (dev/stg/prd)")