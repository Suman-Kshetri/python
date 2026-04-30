# REST = Representational State Transfer.
# Uses HTTP methods: GET, POST, PUT, DELETE.
# Data is usually in JSON format.

import requests # type: ignore
from pprint import pprint

url = "https://jsonplaceholder.typicode.com/posts/1"

#GET request to fetch data from the API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pprint(data)
else:
    print(f"Error: {response.status_code}")

# POST request to send data to the API
new_post = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)

if response.status_code == 201:
    data = response.json()
    pprint(data)
else:
    print(f"Error: {response.status_code}")