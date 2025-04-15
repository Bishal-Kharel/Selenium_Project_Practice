import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.rediff.com/"
pageTitle = "Rediff.com: News | Rediffmail | Stock Quotes | Rediff Gurus"

def test_login():
    #login rediff.com
    driver = webdriver.Chrome()
    driver.maximize_window()

    #user will open rediff.com
    driver.get(URL)


    #verify the page title
    actualTitle = driver.title
    assert actualTitle == pageTitle

    #click Signin link
    signLink = driver.find_element(By.CLASS_NAME, "signin")
    signLink.click()

    #Enter username and password
    userName = driver.find_element(By.ID, "login1")
    userName.send_keys("abc@gmail.com")

    password = driver.find_element(By.ID,"password")
    password.send_keys("Test123")
    time.sleep(5)

    #click Signin button
    signIn = driver.find_element(By.CLASS_NAME, "signin-btn")
    signIn.click()
    time.sleep(5)
    driver.quit()