import requests

url = "http://jsonplaceholder.typicode.com/posts"
res = requests.post(url, timeout =5)

print (res)
