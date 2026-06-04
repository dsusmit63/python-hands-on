import requests
api_url ="https://jsonplaceholder.typicode.com/comments"
response = requests.get(url=api_url)
comments = response.json()
for comment in comments:
  if comment["postId"] == 2 and comment["id"] == 10:
    print(f"Name: {comment['name']} Email: {comment['email']}")
    break