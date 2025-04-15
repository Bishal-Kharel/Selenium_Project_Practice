import time
from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://www.facebook.com/"


def test_abosuteXpath():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    time.sleep(3)


    #using relative xpath
    driver.find_element(By.XPATH,"//html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a").click()
    time.sleep(3)

    # using text()
    driver.find_element(By.XPATH,"//input[@type='text' and @name='firstname']" ).send_keys("Bishal")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@type='text' and @name='lastname']" ).send_keys("Kharel")
    time.sleep(3)

    # using contain()
    driver.find_element(By.XPATH,"//input[contains(@aria-label, 'Mobile')]").send_keys("bishalkharel9842@gmail.com")

    time.sleep(3)



    driver.quit()

