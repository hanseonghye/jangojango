import requests

# url = "http://jsonplaceholder.typicode.com/posts"

url = "https://kauth.kakao.com/oauth/authorize"
res = requests.post(url, timeout =5)

print (res)
