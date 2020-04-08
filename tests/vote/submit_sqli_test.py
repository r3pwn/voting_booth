#!/usr/bin/env python3
# importing the requests library 
import requests 
  
# defining the api-endpoint  
API_HOST = "http://localhost:8080"
API_ENDPOINT = "/vote/submit"

API_PATH = API_HOST + API_ENDPOINT

# data to be sent to api
data = {'username': 'dummy"; DROP TABLE users;--', 
        'candidate': 'Greg Willard'}
print("POST data:", data)

# sending post request and saving response as response object 
r = requests.post(url = API_PATH, data = data) 
  
# extracting response text  
response = r.text 

print("API_HOST:", API_HOST)
print("API_ENDPOINT:", API_ENDPOINT)
print("API response:", r.text)

if (response == "OK"):
    print("TEST PASS!")
else:
    print("TEST FAIL!")
    switcher = {
        400: "Bad request",
        403: "User account doesn't exist or incorrect auth code",
        409: "User has already voted",
        500: "Server broke :("
    }
    print(switcher.get(r.status_code, "Unknown error code"))


