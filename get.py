#this program gets the data from another ai that we will call using url
import requests as rq
from pprint import pprint

params = {"userId": 1}


res = rq.get("https://jsonplaceholder.typicode.com/posts", params=params)

print(f"Code : {res.status_code}")
print(f"URL : {res.url}")
print(f"Num of posts( basically the count of all the userid with 1 as their value):{len(res.json())}")
print("Now as per the number of posts we can chose the post we want to display using indexing.")

pprint(res.json()[6])

print(f"Number of total posts : {len(res.json())}")
print(f"Title : {res.json()[9]['title']}")
print(f"ID of 3rd post : {res.json()[2]['id']}")