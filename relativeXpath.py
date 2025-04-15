import time
from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://classic.freecrm.com/"
titlePage = "Free CRM software for customer relationship management, sales, and support."

def test_abosuteXpath():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    assert driver.title == titlePage
    time.sleep(3)


    #using relative xpath
    driver.find_element(By.XPATH,"//a[@class='navbar-brand']/img[@class='img-responsive']").click()
    time.sleep(3)

    driver.find_element(By.LINK_TEXT, "Sign Up").click()
    time.sleep(3)

    assert driver.title == titlePage
    driver.quit()

