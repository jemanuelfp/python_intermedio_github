from urllib import request
import requests
import os

os.system('cls')


json_resquest = requests.get("https://jsonplaceholder.typicode.com/posts/1")

#print(json_resquest)
#print(type(json_resquest))

print("=" * 50)
print(json_resquest.text)
print(type(json_resquest.text))
print("=" * 50)
print(json_resquest.json())
print(type(json_resquest.json()))


