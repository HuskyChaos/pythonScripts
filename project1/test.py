#!/bin/python3
import time
from typing import get_type_hints
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

profile_path = r'/home/kali/.mozilla/firefox/06au6nqy.default'
options=Options()
options.set_preference('profile', profile_path)
service = Service(r'./geckodriver')

driver = Firefox(service=service, options=options)

driver.get("https://nbl.one/listings")

print("Python Waiting for web page to finish loading...")

for i in range(10,0,-1):
    print("{}....".format(i))
    time.sleep(1)

print()
classes = driver.find_elements_by_class_name('gig_cards')

for c in classes:
    if c.text != '':
        temp = c.text.split('\n')
        print(temp[0])
        for i in temp:
            if 'Starts' in i:
                print(i)
        print ('--------------------------------------------------')

driver.quit()