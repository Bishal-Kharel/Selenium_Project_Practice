import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


URL = "https://www.facebook.com/"

def test_seleniumWaits():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    driver.implicitly_wait(5)


    driver.find_element(By.XPATH, "//a[@role='button' and @data-testid='open-registration-form-button']").click()

    month = driver.find_element(By.ID,"month")
    dropdown = Select(month).select_by_index(5)
    time.sleep(3)

    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
    driver.get_screenshot_as_file("screenshot_"+timestamp+".png")
    time.sleep(3)
 

    driver.quit()