# -*- coding: utf-8 -*-
"""
Created on Fri May  4 14:29:10 2018

@author: vijayana
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
import io
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome()
browser.get('https://www.google.com/maps/place/Embassy+Manyata+Business+Park/@13.0499862,77.6175589,17z/data=!3m1!4b1!4m10!1m2!2m1!1smanyata+tech+park+banglore!3m6!1s0x3bae176ddc662065:0x57b2874f9023bb8!8m2!3d13.049981!4d77.6197476!9m1!1b1')

actions = ActionChains(browser)

browser.maximize_window()
time.sleep(3)
content = browser.find_element_by_class_name('scrollable-show').click()
htmlstring = browser.page_source
afterstring=""
for _ in range(10000):
    afterstring = htmlstring
    actions.send_keys(Keys.PAGE_DOWN).perform()
    htmlstring = browser.page_source
    if afterstring == htmlstring:
        print ("ended scraping crack test one")
        actions.send_keys(Keys.PAGE_DOWN).perform()
        htmlstring = browser.page_source
        if afterstring == htmlstring:
           print ("--Scrapping End--")
           break
    time.sleep(3)
    

#print(htmlstring)
textdoc = io.open("gmapreview.txt", "w", encoding="utf-8")
soup = BeautifulSoup(htmlstring,"lxml")
mydivs = soup.findAll("div", {"class": "section-review-content"})
counter = 0
for a in mydivs: 
    textdoc.write(str("\nReviewer name: "+a.find("div", class_="section-review-title").text)+" \n||Reviewer Detail: " + str(a.find("div", class_="section-review-subtitle").text) +" \n||Reviewerer Profile URL:"+ str(a.find("a").get('href')))
    
    textdoc.write(" \n||" + a.find("span", class_="section-review-text").text+" \n|| " + a.find("span", class_="section-review-publish-date").text)
    textdoc.write("=========================================\n")
    counter = counter + 1
print ("Total reviews scraped:"+str(counter))
textdoc.close()
    
#actions.send_keys(Keys.PAGE_DOWN).perform()

#browser.execute_script('')