import requests as rq

data = {
    # userId omitted because we're directly targeting the post by ID
    "title" : "Daniel",
    "body" : "dee nail is the river in egypt your husbendo is gay"
}

res = rq.put("https://jsonplaceholder.typicode.com/posts/101", json=data)
print(f"Status : {res.status_code}")
print(f"URL : {res.url}")
print(f"Json data : {res.json()}")

#the ones below wont work as they are part of get funtion not put i made a mistake so u don't
#print(f"Post number : {len(res.json())}")
#print(f"Title : {res.json()[1]['title']}")