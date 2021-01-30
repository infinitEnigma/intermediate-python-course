""" connect to instagram and start actions """
import sys
from time import sleep
from random import randint
from selenium import webdriver
import insta_vars
from insta_actions import FollowLikePost

# open chrome
chromewebdriver = webdriver.Chrome()
chromewebdriver.get('https://instagram.com')
# sleep while the page loads - change according to your internet speed !!!
sleep(randint(5,10))

username = chromewebdriver.find_element_by_name('username')
password = chromewebdriver.find_element_by_name('password')

# login is ready - input username and password
user = input('input Instagram username: ')
passw = input('input Instagram password: ')
username.send_keys(user)
sleep(1)
password.send_keys(passw)
sleep(0.5)

# pass through without saving credentials and don't allow notifications
lbutton = chromewebdriver.find_element_by_css_selector(insta_vars.loginButton)
lbutton.click()
sleep(3)
notnow = chromewebdriver.find_element_by_xpath(insta_vars.dontRememberPass)
notnow.click()
sleep(3)
notnow = chromewebdriver.find_element_by_xpath(insta_vars.noNotifications)
notnow.click()
sleep(randint(5,10))

# logged in, define your actions
print("do you want random search or specific person?")
print("enter 'r' for random or specific name that you want to search for, ")
action = input("or 'q' to quit: ")
if action == 'q':
    sys.exit("goodbye")

# start the loop
followLikePost(action, chromewebdriver)
