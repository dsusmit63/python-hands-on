import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url=api_url)
todos = response.json()
completed = []
for todo in todos:
  if todo["userId"] == 1 and todo["completed"] == True:
    completed.append(todo["title"])
print(completed)