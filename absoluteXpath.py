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
    driver.find_element(By.LINK_TEXT, "Sign Up").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/ul/li[2]/a").click()
    time.sleep(3)
    assert driver.title == titlePage
    driver.quit()

