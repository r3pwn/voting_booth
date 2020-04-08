#!/usr/bin/env python3
# importing the requests library 
import requests 
  
# defining the api-endpoint  
API_HOST = "http://localhost:8080"
API_ENDPOINT = "/user/login"

API_PATH = API_HOST + API_ENDPOINT
  
# data to be sent to api 
data = {'username':'dummy', 
        'password':'hunter2'}
print("POST data:", data)

# sending post request and saving response as response object 
r = requests.post(url = API_PATH, data = data) 
  
# extracting response text  
response = r.text 

print("API_HOST:", API_HOST)
print("API_ENDPOINT:", API_ENDPOINT)
print("API response:", r.text)

if (response != "ERR"):
    print("TEST PASS!")
else:
    print("TEST FAIL!")
    switcher = {
        400: "Bad request",
        403: "User account doesn't exist or password incorrect",
        500: "Server broke :("
    }
    print(switcher.get(r.status_code, "Unknown error code"))


