import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

URL = "https://www.facebook.com/"

def test_seleniumWaits():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    driver.implicitly_wait(5)




    # drag and Drop
    action =  ActionChains(driver)
    time.sleep()

    ele1 =driver.find_element(By.XPATH, "Put the Xpath here")#source Xpath


    ele2 =driver.find_element(By.XPATH, "Put the Xpath here") #Destination Xpath 

    action.drag_and_drop(ele1,ele2).perform()

    ele3=driver.find_element(By.XPATH, "Put the Xpath here")

    driver.quit()