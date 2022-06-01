from urllib import request
import requests
import os

os.system('cls')


json_resquest = requests.get("https://jsonplaceholder.typicode.com/users")

#print(json_resquest)
#print(type(json_resquest))

response_dic = json_resquest.json()

for data in response_dic:
    print(data)



