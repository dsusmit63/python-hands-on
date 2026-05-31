for i in range(3):
  env = input("Enter environment (dev,stg,prd): ").lower()
  if env == "prd":
    print("Deployed to Production server")
  elif env == "stg":
    print("Deployed to Staging server")
  elif env == "dev":
    print("Deployed to Dev server")
  else:
    print("Deployed into wrong environment")
    break