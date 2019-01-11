import requests


print(requests.__version__)

r = requests.get(r'https://raw.githubusercontent.com/shouyang/CMPUT404-LAB01/master/get.py')

print(r.text)
print(r.status_code)


