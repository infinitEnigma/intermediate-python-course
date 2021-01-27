from selenium import webdriver
from time import sleep
from random import randint
import insta_vars 
import sys



# open chrome
chromewebdriver = webdriver.Chrome()
chromewebdriver.get('https://instagram.com')
sleep(randint(5,10)) # sleep while the page loads - change according to your internet speed !!!

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
action = input("enter 'r' for random or specific name that you want to search for or 'q' for quit: ")
if action == 'q': sys.exit("goodbye")



# define the loop for following, liking and posting - change to fit your needs
def FollowLikePost(who):
    if who == 'r':
        chromewebdriver.get('https://instagram.com/explore/')
        sleep(randint(5,10))
        # take the first post
        post = chromewebdriver.find_element_by_xpath(insta_vars.firstPost)
        post.click()
        sleep(randint(1,3))
    else:
        # find instagram users and like all their posts
        searchbox = chromewebdriver.find_element_by_xpath(insta_vars.searchBox)
        searchbox.focus = True
        searchbox.send_keys(who)
        sleep(2)
        chromewebdriver.find_element_by_xpath(insta_vars.firstResult).click()
        sleep(10)
        chromewebdriver.find_element_by_css_selector(insta_vars.firstResultsPost).click()
        sleep(5)
    while True:
        for item in range(1,10):
            sleep(randint(3,7))
            
            if chromewebdriver.find_element_by_xpath(insta_vars.followButton).text == 'Follow':
                chromewebdriver.find_element_by_xpath(insta_vars.followButton).click()
                sleep(randint(1,4))
                chromewebdriver.find_element_by_xpath(insta_vars.likeButton).click()
                sleep(randint(2,5))
                chromewebdriver.find_element_by_xpath(insta_vars.commentButton).click()
                sleep(randint(1,3))
                commentbox = chromewebdriver.find_element_by_xpath(insta_vars.commentTextArea)
                commentbox.click()
                commentbox.send_keys(insta_vars.commentList[randint(0,3)])
                sleep(randint(5,8))
                chromewebdriver.find_element_by_xpath(insta_vars.submitButton).click()
                sleep(randint(1,3))
            # go to the next post
            try:
                chromewebdriver.find_element_by_link_text('Next').click()
            except:
                action = input("enter 'r' for random or specific name that you want to search for or 'q' for quit: ")
                if action == 'q': sys.exit("goodbye")
                else: FollowLikePost(action)
        sleep(10000)



#start the infinite loop
FollowLikePost(action)
    
    

