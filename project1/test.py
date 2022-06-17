#!/bin/python3
import time
from numpy import empty
import requests
from typing import get_type_hints
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

profile_path = r'/home/kali/.mozilla/firefox/06au6nqy.default'
options=Options()
options.set_preference('profile', profile_path)
service = Service(r'./geckodriver')
driver = Firefox(service=service, options=options)

url = "https://nbl.one"
r = requests.get(url)
if r.status_code < 400:
    try:
        driver.get(url)
        print("Python Waiting for web page to finish loading...")
        for i in range(10,0,-1):
            print("{}....".format(i))
            time.sleep(1)
        print()
        ids = driver.find_elements_by_tag_name('section')
        count = 0
        for id in ids:
            if 'quest' in id.get_attribute('id'):
                count+=1
        if count > 0:
            print("{} questions available.".format(count))
        else:
            print("No questions available.")
        print()

    except Exception as e:
        print(e)

url = "https://nbl.one/listings"
r = requests.get(url)
if r.status_code >= 400:
    exit(r.reason)
else:
    try:
        driver.get(url)
        print("Python Waiting for web page to finish loading...")
        for i in range(10,0,-1):
            print("{}....".format(i))
            time.sleep(1)
        print()
        count = 0
        classes = driver.find_elements_by_class_name('gig_cards')
        for i in classes:
            if i.text != '':
                count+=1
        for i in range(count):
            print("Course number : {}".format(i+1))
            classes = driver.find_elements_by_class_name('gig_cards')
            count2 = 0
            for c in classes:
                if c.text != '':
                    if count2 == i:
                        temp = c.text.split('\n')
                        print("Course Name : {}".format(temp[0]))
                        for i in temp:
                            if 'Starts' in i:
                                i = i.split()
                                i = i[len(i)-1].split('$')
                                print("Course Price : Starts at ${}".format(i[len(i)-1]))
                        c.click()
                        time.sleep(2)
                        print("Course URL : {}".format(driver.current_url))
                        driver.execute_script("window.history.go(-1)")
                        print ('--------------------------------------------------')
                        time.sleep(2)
                        break
                    count2+=1
        driver.quit()
    except Exception as e:
        print(e)