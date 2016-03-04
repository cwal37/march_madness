# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:48:40 2015

@author: cwal3
"""

from selenium import webdriver
import time
import urllib
import lxml.html
import random as rn
import pandas as pd

driver = webdriver.Firefox()
driver.get('http://espn.go.com/mens-college-basketball/tournament/bracket')

teams = []

for team in driver.find_elements_by_tag_name('a'): # select the url in href for all a tags(links)
    team_name = str(team.get_attribute('title'))
    if len(team_name)>2:
        teams.append(team_name)
    print team_name
#print teams

driver.close()
driver.quit()
    
    

        
    
