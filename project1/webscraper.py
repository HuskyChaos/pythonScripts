#!/bin/python3
import time
import requests
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

profile_path = r'/home/kali/.mozilla/firefox/06au6nqy.default'
options=Options()

url = "https://nbl.one"
print("URL for question search: {}".format(url))
r = requests.get(url)
if r.status_code < 400:
    try:
        options.set_preference('profile', profile_path)
        service = Service(r'./geckodriver')
        driver = Firefox(service=service, options=options)
        driver.get(url)
        print("Python Waiting for web page to finish loading...")
        print("Wait for 5 seconds...")
        time.sleep(5)
        print()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
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
        driver.quit()

    except Exception as e:
        driver.quit()
        print(e)

url = "https://nbl.one/listings"
print("URL for course search: {}".format(url))
r = requests.get(url)
if r.status_code >= 400:
    exit(r.reason)
else:
    try:
        options.set_preference('profile', profile_path)
        service = Service(r'./geckodriver')
        driver = Firefox(service=service, options=options)
        driver.get(url)
        print("Python Waiting for web page to finish loading...")
        print("Wait for 5 seconds...")
        time.sleep(5)
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
        driver.quit()
        print(e)

url = "https://nby.la/rdJuXp"
print("URL for course booking: {}".format(url))
print()
print("Enter email ID: ", end='')
emailId = input()
print("Enter password: ",end='')
passwd = input()
r = requests.get(url)
if r.status_code >= 400:
    exit(r.reason)
else:
    try:
        options.set_preference('profile', profile_path)
        service = Service(r'./geckodriver')
        driver = Firefox(service=service, options=options)
        driver.get("https://nby.la/rdJuXp")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="skylift-book-seat"]').click()
        driver.implicitly_wait(5)
        driver.find_element_by_css_selector('''.nsm7Bb-HzV7m-LgbsSe-BPrWId''').click()
        driver.implicitly_wait(2)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        driver.find_element_by_tag_name('input').send_keys(emailId)
        driver.find_element_by_xpath('//span[text()="Next"]').click()
        time.sleep(8)
        driver.find_element_by_xpath('//input[@type="password"]').send_keys(passwd)
        driver.find_element_by_xpath('//span[text()="Next"]').click()
        time.sleep(4)
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_xpath('//span[text()="Proceed"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//p[text()="Choose Billing Country"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//input[@placeholder="Search Billing Country"]').send_keys('India')
        time.sleep(2)
        driver.find_element_by_xpath('//button[text()="India"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//p[text()="Choose Billing State"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//input[@placeholder="Search Billing State"]').send_keys('Bihar')
        time.sleep(2)
        driver.find_element_by_xpath('//button[text()="Bihar"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//span[text()="Confirm FREE Booking"]').click()
        time.sleep(8)
        driver.quit()
    except Exception as e:
        driver.quit()
        print(e)
        