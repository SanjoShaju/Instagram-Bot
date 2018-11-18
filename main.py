from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

import time
import random
import re


def init_driver():
    options  = Options()
    # Add path to your User profile 
    # Create a seperate user profile for this bot with instagram logged in that user profile.
    # Otherwise use your default. But when using default you wont be able to use chrome for anything else.
    options.add_argument("--user-data-dir=C:/path to the user profile/User Data")
    # Add path to your chrome driver
    driver = webdriver.Chrome(executable_path='C:/path to the chromedriver/chromedriver.exe', options=options)
    return driver


def get_post_links(driver, tag):
    driver.get('https://www.instagram.com/explore/tags/'+ tag +'/')
    time.sleep(2)

    # Scrolling 3 times to get more post links
    for i in range(1, 3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print('scroll '+ str(i) + ' time')
        time.sleep(2)
    print('scroll done')

    pic_hrefs = []
    hrefs_in_view = driver.find_elements_by_tag_name('a')
    post_url_start = "https://www.instagram.com/p/" # this is the starting part of most post url
    # finding post hrefs
    pic_hrefs = [elem.get_attribute('href') for elem in hrefs_in_view if post_url_start in elem.get_attribute('href')]
    print("=======================================")
    for pic_href in pic_hrefs:
        print(pic_href) # printing the link
        print('---------------------------')

        driver.get(pic_href) # the link is opened
        time.sleep(2)

        # function that does the commenting
        comment(driver)

        # function that does the like and follow function
        like_follow_automater(driver)

def like_follow_automater(driver):
    try:
        username = driver.find_element_by_xpath("//a[@class='FPmhX notranslate nJAzx']").get_attribute('text')
        driver.get('https://www.instagram.com/'+ username +'/')
        
        print("Opened "+ username + "'s profile")
        print('---------------------------')
        
        time.sleep(2)

        if (driver.find_element_by_css_selector('._5f5mN.jIbKX._6VtSN.yZn4P')): # finding if this person is already followed
            driver.find_element_by_css_selector('._9AhH0').click()
            print('DIV clicked')
            time.sleep(2)
            driver.find_element_by_css_selector('.glyphsSpriteHeart__outline__24__grey_9.u-__7').click()
            print("Pic 1 Like clicked")
            driver.find_element_by_css_selector('.HBoOv.coreSpriteRightPaginationArrow').click()
            print("Right Arrow clicked")
            time.sleep(2)
            driver.find_element_by_css_selector('.glyphsSpriteHeart__outline__24__grey_9.u-__7').click()
            print("Pic 2 Like clicked")
            driver.find_element_by_css_selector('.HBoOv.coreSpriteRightPaginationArrow').click()
            print("Right Arrow clicked")
            time.sleep(2)
            driver.find_element_by_css_selector('.glyphsSpriteHeart__outline__24__grey_9.u-__7').click()
            print("Pic 3 Like clicked")
            driver.find_element_by_css_selector('.oW_lN._0mzm-.sqdOP.yWX7d').click()
            print("Followed the profile")
            time.sleep(2)
        else:
            print("Already Followed")
        print('closed next----------------')
        print('.')
        print('---------------------------')
    except Exception as e:
        print(e)


def comment(driver):
    try:
        comments_block = driver.find_element_by_class_name('k59kT')
        comments_in_block = comments_block.find_elements_by_class_name('gElp9')
        user_comment = re.sub(r'#.\w*', '', comments_in_block[0].find_element_by_tag_name('span').text)
    except Exception as e:
        print(e)
        user_comment = ''

    # Before using this first train your bot with trainer.py
    # it would have created a trained set which is stored as a sqlite file
    bot = ChatBot('instabot')
    bot.set_trainer(ListTrainer)

    # user's comment and bot's response
    response = bot.get_response(user_comment).__str__()
    print("User's Comment :- \n", user_comment)
    print('---------------------------')
    print("Bot's Response :- \n", response)
    print('---------------------------')

    try:
        driver.find_element_by_css_selector('.Ypffh').send_keys(response)
        driver.find_element_by_css_selector('.Ypffh').send_keys(Keys.ENTER)
        time.sleep(2)
        print("Commented on the post")
        print('---------------------------')
    except Exception as e:
        print(e)
        print('---------------------------')
    

def main():
    driver = init_driver() # intializing the driver

    # Hastag list to iterate
    hashtags = ['comic', 'cartoon', 'manga', 'meme', 'pokemon','dc', 
            'marvel', 'ironman', 'avengers', 'anime', 'fun', 'happy']
    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            get_post_links(driver, tag)
        except Exception:
            driver.close()
    driver.close()
    
if __name__ == '__main__':
    main()




