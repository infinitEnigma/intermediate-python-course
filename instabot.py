from selenium import webdriver
from time import sleep
from random import randint

# instagram variables
loginButton = '#loginForm > div > div:nth-child(3)'
dontRememberPass = '//*[@id="react-root"]/section/main/div/div/div/div/button'
noNotifications = '/html/body/div[4]/div/div/div/div[3]/button[2]'
firstPost = '//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]/div/a/div/div[2]'
followButton = '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button'
likeButton = '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span'
commentButton = '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button/div'
commentTextArea = '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea'
submitButton = '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div//form/button'

# your posts (comments) - should be replaced with some ai logic
commentList = ['Awesome post `(super post - testiranje bota u toku, sorry :tada:)`', 'Great post `(super post - testiranje bota u toku, sorry :tada:)`', 'I really like your post `(super post - testiranje bota u toku, sorry :tada:)`', 'The best post today `(super post - testiranje bota u toku, sorry :tada:)`']


# open chrome
chromewebdriver = webdriver.Chrome()
chromewebdriver.get('https://instagram.com')
sleep(randint(5,10)) # sleep while the page loads - change according to your internet speed !!!

# login is ready - input username and password
username = chromewebdriver.find_element_by_name('username')
password = chromewebdriver.find_element_by_name('password')

user = input('input Instagram username: ')
passw = input('input Instagram password: ')
username.send_keys(user)
sleep(1)
password.send_keys(passw)
sleep(0.5)

# pass through without save credentials and 
lbutton = chromewebdriver.find_element_by_css_selector(loginButton)
lbutton.click()
sleep(3)
notnow = chromewebdriver.find_element_by_xpath(dontRememberPass)
notnow.click()
sleep(3)
notnow = chromewebdriver.find_element_by_xpath(noNotifications)
notnow.click()
sleep(randint(5,10))

# logged in, go to instagram's explore page
chromewebdriver.get('https://instagram.com/explore/')
sleep(randint(5,10))

# take first post
post = chromewebdriver.find_element_by_xpath(firstPost)
post.click()
sleep(randint(1,3))

# start the loop for following, liking and posting - change to fit your needs
while True:
    for item in range(1,10):
        sleep(randint(3,7))
        if chromewebdriver.find_element_by_xpath(followButton).text == 'Follow':
            chromewebdriver.find_element_by_xpath(followButton).click()
            sleep(randint(1,4))
            chromewebdriver.find_element_by_xpath(likeButton).click()
            sleep(randint(2,5))
            chromewebdriver.find_element_by_xpath(commentButton).click()
            sleep(randint(1,3))
            commentbox = chromewebdriver.find_element_by_xpath(commentTextArea)
            commentbox.click()
            commentbox.send_keys(commentList[randint(0,3)])
            sleep(randint(1,3))
            chromewebdriver.find_element_by_xpath(submitButton).click()
            sleep(randint(1,3))
        # go to the next post
        chromewebdriver.find_element_by_link_text('Next').click()
    sleep(10000)

