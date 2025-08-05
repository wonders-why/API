import requests as rq
from pprint import pprint

data = {
    "title": "Daniel",
    "body": "lorem ipsion 100",
    "userId": 6
}

# POST request
res = rq.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(f"Status code : {res.status_code}")
print(f"Url: {res.url}")
pprint(res.json())

# GET request (won’t retrieve post because mock API doesn’t store it)
res = rq.get("https://jsonplaceholder.typicode.com/posts", params={"userId": 6})
print(f"GET Status code : {res.status_code}")
pprint(res.json()[0]["title"])
