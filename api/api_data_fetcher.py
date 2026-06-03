import requests
api_url ="https://jsonplaceholder.typicode.com/users"
response = requests.get(url = api_url)  
print(response)
users = response.json()
for user in users:
  if user["company"]["name"] in ["Romaguera-Crona", "Romaguera-Jacobson"]:
    print(user)

