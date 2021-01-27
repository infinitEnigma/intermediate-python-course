from time import sleep
from random import randint
import insta_vars, sys

# define the loop for following, liking and posting - change to fit your needs
def FollowLikePost(who, chromewebdriver):
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
            followbutton = chromewebdriver.find_element_by_xpath(insta_vars.followButton)
            if followbutton.text == 'Follow':
                followbutton.click()
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
                print("no more posts by these criteria for: ", who)
                action = input("enter 'r' for random or specific name that you want to search for, or 'q' to quit: ")
                if action == 'q': sys.exit("goodbye")
                else: FollowLikePost(action, chromewebdriver)
        sleep(randint(100,10000))
