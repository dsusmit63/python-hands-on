env = input("Enter environment (dev,stg,prd): ").lower()
if(env == "prd"):
  print("Deployed to Production server")
elif(env == "stg"):
  print("Deployed to Staging server")
else:
  print("Deployed to Dev server")