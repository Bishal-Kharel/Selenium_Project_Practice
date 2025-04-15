import time
from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://www.google.com/"
# titlePage = "Free CRM software for customer relationship management, sales, and support."

def test_seleniumWaits():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    # assert driver.title == titlePage

    searchBox= driver.find_element(By.XPATH,"//textarea[@id='APjFqb' and contains(@class, 'gLFyf')]").send_keys("selenium-webdriver")

    time.sleep(4)
    searchBox= driver.find_element(By.XPATH,"//div[@role='option' and @aria-label='selenium-webdriver github']").click()
    time.sleep(5)

    driver.quit()