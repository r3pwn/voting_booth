#!/usr/bin/env python3
# importing the requests library 
import requests 
import sys
  
# defining the api-endpoint  
API_HOST = "http://localhost:8080"
API_ENDPOINT = "/results/view"

API_PATH = API_HOST + API_ENDPOINT

# sending post request and saving response as response object 
r = requests.get(url = API_PATH) 
  
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
        500: "Server broke :("
    }
    print(switcher.get(r.status_code, "Unknown error code"))


