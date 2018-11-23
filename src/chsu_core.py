# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime 
import selenium 
import time 
import re
import os

#l
def split_date(msg,index):
    date = re.split('/',msg)
    return date[index]

def open_page(driver,group):
       
    driver.implicitly_wait(10)
    driver.get('https://www.chsu.ru/raspisanie')    
    try:
        cookie_button = driver.find_element_by_css_selector('.cookies-button')
        cookie_button.click()
    except NoSuchElementException:
        pass       
# Group  
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_id('select2-groups-container').click()
    except NoSuchElementException:   
        print('There is not such group') 
        return False

    driver.implicitly_wait(3)
    enter = driver.find_element_by_css_selector('.select2-search__field')
    enter.send_keys(group)
    enter.send_keys(Keys.ENTER)

# Day-range 
    fist_day = datetime.now().day
    driver.find_element_by_link_text(str(fist_day)).click()
    try:
        driver.find_element_by_link_text('30').click()
    except AttributeError: 
        driver.find_element_by_link_text('31').click()
    except AttributeError:
        driver.find_element_by_link_text('28').click()
    driver.find_element_by_id('btTime').click()
    
    return True


def fill_list(self,lq):
    j =0
    for cur_day in self.find_elements_by_class_name('head-day'):
        sub_list=[]
        sub_list.append(split_date(cur_day.text,1))

        for i in range(2,8):
            try:
                time=self.find_element_by_css_selector('#table'+str(j)+' > tr:nth-child('+str(i)+') > td.col-time').text
                disc=self.find_element_by_css_selector('#table'+str(j)+' > tr:nth-child('+str(i)+') > td.col-discipline').text
                aud=self.find_element_by_css_selector('#table'+str(j)+' > tr:nth-child('+str(i)+') > td:nth-child(5)').text
            except:
                break
            else:
                lecture = [time,disc,aud]
            sub_list.append(lecture)

        lq.put(sub_list)
        j=j+1
    lq.put('last')
    


def init():


    options = Options()
    chrome_options = Options()                              #
    chrome_options.add_argument("--headless")               #
    chrome_options.add_argument("--disable-gpu")            #
    chrome_options.add_argument("--window-size=1920x1080")  #
    chrome_driver = os.getcwd() + "\\chromedriver.exe"      #

    driver = selenium.webdriver.Chrome(chrome_options=chrome_options,executable_path=chrome_driver)
    return driver 


