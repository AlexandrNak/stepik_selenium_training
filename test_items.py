import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time  

def test_to_find_a_button_on_the_page(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    browser.get(link)
    time.sleep(10)
    
    buttons = browser.find_elements(By.CLASS_NAME, 
                                    "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(buttons) > 0, "No_element"

        


