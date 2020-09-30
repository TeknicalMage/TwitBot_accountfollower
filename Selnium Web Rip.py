import time 
import random
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains



import pickle
#import PasswordRead as PR

#Clicking Google Search button 
#driver.find_element_by_xpath("//input[@value='Google Search']").click()

#Keyword searched in the chrometest
searchtext =('Steve Wozniak')




def chrometest():
    driver = webdriver.Chrome()
    
        
    driver.get("https://twitter.com/search?q=%22Podcast%22&src=typed_query&f=user")
    
    time.sleep(1)
    
    x=5

    f = open('values.txt', 'a')

    time.sleep(5)

    SCROLL_PAUSE_TIME = .8

    last_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height)

    itr_count = 5
    max_writes = 100

    while x < 1000:
    # Scroll down to bottom
        try:
            while itr_count < max_writes:
                id = driver.find_elements_by_xpath('//a')[itr_count].text
                print(id)

                f.write(id +"\n")
                itr_count+=1

            max_writes+= 100
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    
            time.sleep(1)
                     
            
            print(x)
            x+=1

        # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        except:
            target = driver.find_elements_by_xpath('//a')[itr_count]
            actions = ActionChains(driver)
            actions.move_to_element(target)
            #f.close()
            





    
   
    #file_object.close()
    print('exit')
    
    time.sleep(1)

    

def runloop():

    print('Type [rip] or [none]')
    x = input()
    
    if x == ('rip'):
        print('running Rip')
        chrometest()
    elif x == ('discord'):
        print('running discordlogin')
        #discordlogin()
    else:
        runloop()

#PR.login()
runloop()




