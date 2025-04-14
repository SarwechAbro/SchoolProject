import requests
import json

url = "http://127.0.0.1:8000/studentapi/"


headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY2Mzk4MjMyLCJpYXQiOjE3MzUyOTQyMzIsImp0aSI6ImU4ZDcxMjU4NWUyZjQzYTVhZmVjOGQzZmFmODEyNjFkIiwidXNlcl9pZCI6MX0.7Yyz-Wpuk7_f01SF96fScN6vnedzAZ1E2JALTCesKxI',
 
}

response = requests.request("GET", url, headers=headers)
data = json.loads(response.text)
print(data)