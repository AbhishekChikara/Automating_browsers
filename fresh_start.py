# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 14:52:30 2018

@author: abhishek.chikara
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 19:10:39 2018

@author: Abhishek
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
#from bs4 import BeautifulSoup
#import pandas as pd
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException







browser = webdriver.Chrome("C:/Users/abhishek.chikara/Chromedriver.exe")
browser.get('website') #Website contain dyanamic elements

wait = WebDriverWait(browser,120)
def find_wait(selector=''):
    
    if selector.startswith('/'):
            by = By.XPATH
    else:
            by = By.ID
    
    try:
        
        
            
        elements=wait.until(EC.element_to_be_clickable((by, selector))) 
        return elements
    
    
        
    except StaleElementReferenceException:
        print ('attempting to recover \
                   from StaleElementReferenceException ...')
        time.sleep(5)
        elements=wait.until(EC.element_to_be_clickable((by, selector)))
        return elements
    

def select_commodities(selector=''):
    
    if selector.startswith('/'):
            by = browser.find_element_by_xpath
    else:
            by = browser.find_element_by_id
    
    try:
        commbox = by(selector)
        Select(commbox).select_by_value(p)
        
        return None
    except NoSuchElementException:
        print('trying to find the element')
        time.sleep(6)
        commbox = by(selector)
        Select(commbox).select_by_value(p)
        return None
    except StaleElementReferenceException:
        print('trying to find the element')
        time.sleep(6)
        commbox = by(selector)
        Select(commbox).select_by_value(p)
        return None
    
def select_year(selector=''):
    
    if selector.startswith('/'):
            by = browser.find_element_by_xpath
    else:
            by = browser.find_element_by_id
    
    try:
        yearbox = by(selector)
        Select(yearbox).select_by_value(q)
        
        return None
    except NoSuchElementException:
        print('trying to find the element')
        time.sleep(6)
        yearbox = by(selector)
        
        Select(yearbox).select_by_value(q)
        return None        
    
    except StaleElementReferenceException:
        print('trying to find the element')
        time.sleep(6)
        yearbox = by(selector)
        
        Select(yearbox).select_by_value(q)
        return None
    
def select_month(selector=''):
    
    if selector.startswith('/'):
            by = browser.find_element_by_xpath
    else:
            by = browser.find_element_by_id
    
    try:
        monthbox = by(selector)
        Select(monthbox).select_by_value(r)
        
        return None
    except NoSuchElementException:
        print('trying to find the element')
        time.sleep(6)
        monthbox = by(selector)
        
        Select(monthbox).select_by_value(r)
        return None 
    
    except StaleElementReferenceException:
        print('trying to find the element')
        time.sleep(6)
        monthbox = by(selector)
        Select(monthbox).select_by_value(r)
        return None       
    
def select_week(selector=''):
    
    if selector.startswith('/'):
            by = browser.find_element_by_xpath
    else:
            by = browser.find_element_by_id
    
    try:
        weekbox = by(selector)
        Select(weekbox).select_by_value(s)
        
        return None
    except NoSuchElementException:
        print('trying to find the element')
        time.sleep(6)
        weekbox = by(selector)
        
        Select(weekbox).select_by_value(s)
        return None           
    
    except StaleElementReferenceException:
        print('trying to find the element')
        time.sleep(6)
        weekbox = by(selector)
        
        Select(weekbox).select_by_value(s)
        return None 
        
#iterating through drop down options
commodities=['369','48','150','285','44','141','78','372','49','260','28','29','266','112','45','367','366','10','312','367','4','20','23','2','24','3','11','13']
#years=['2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
#months=['1','2','3','4','5','6','7','8','9','10','11','12']
#weeks=['1','2','3','4']


for p in commodities:

    select_commodities(selector='//select[@name="ctl00$cphBody$Commod1_List"]')
    element = find_wait(selector='//*[@id="cphBody_Year3_List"]')
#    yearbox=lambda : browser.find_element_by_xpath('//*[@id="cphBody_Year3_List"]')
#    years = [x.get_attribute("value") for x in yearbox().find_elements_by_tag_name("option")]
#    years=years[1:]
    years=['2017']
#    print(years)
    for q in years:

        select_commodities(selector='//select[@name="ctl00$cphBody$Commod1_List"]')
        element= find_wait(selector='//*[@id="cphBody_Year3_List"]')

        time.sleep(1)

        select_year(selector='//*[@id="cphBody_Year3_List"]')

        element =find_wait(selector='//*[@id="cphBody_Month3_List"]')
        monthbox=lambda : browser.find_element_by_xpath('//*[@id="cphBody_Month3_List"]')
        months = [x.get_attribute("value") for x in monthbox().find_elements_by_tag_name("option")]
        months=months[1:]
#        print(months)
        for r in months:
#            Select(commbox()).select_by_value(p)
            select_commodities(selector='//select[@name="ctl00$cphBody$Commod1_List"]')    

            element =find_wait(selector='//*[@id="cphBody_Year3_List"]')
            time.sleep(1)

            select_year(selector='//*[@id="cphBody_Year3_List"]')

            element= find_wait(selector='//*[@id="cphBody_Month3_List"]')
            time.sleep(1)

            select_month(selector='//*[@id="cphBody_Month3_List"]')
            element = find_wait(selector='//*[@id="cphBody_Week2_List"]')
            time.sleep(9)

            
            weekbox=lambda : (browser.find_element_by_xpath('//*[@id="cphBody_Week2_List"]'))
            weeks = [x.get_attribute("value") for x in weekbox().find_elements_by_tag_name("option")]
            weeks=weeks[1:]
            print(weeks)
            for s in weeks:

                select_commodities(selector='//select[@name="ctl00$cphBody$Commod1_List"]')  

                element =find_wait(selector='//*[@id="cphBody_Year3_List"]')
                time.sleep(1)

                select_year(selector='//*[@id="cphBody_Year3_List"]')

                element =find_wait(selector='//*[@id="cphBody_Month3_List"]')
                time.sleep(1)

                select_month(selector='//*[@id="cphBody_Month3_List"]')
                

                element = find_wait(selector='//*[@id="cphBody_Week2_List"]')
                time.sleep(12)

                select_week(selector='//*[@id="cphBody_Week2_List"]')
                browser.find_element_by_xpath('//*[@id="cphBody_Button_Subm"]').click()
                
                wait.until(EC.element_to_be_clickable((By.ID, 'cphBody_Button1')))
                
                browser.find_element_by_name('ctl00$cphBody$Button1').click()
               

                time.sleep(2)
                browser.find_element_by_id('cphBody_btnBack').click()
                wait.until(EC.element_to_be_clickable((By.ID, 'cphBody_Commod1_List')))
                
