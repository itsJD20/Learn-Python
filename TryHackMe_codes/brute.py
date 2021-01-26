import requests

url ='http://10.10.42.70:8000/api/'
for i in range (1,100,2):
    r=requests.get(url+str(i))
    if 'Error' not in r.text:
        print(i)
        print(r.text)
... 

