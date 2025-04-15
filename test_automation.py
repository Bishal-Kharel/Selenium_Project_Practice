import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

project_path = os.getcwd()

path = os.path.join(project_path, "Selenium_Webdriver", "chromedriver")


service = Service(executable_path=path)


# delete the chrome notification like automaed by test
c_options = webdriver.ChromeOptions()
c_options.add_experimental_option("excludeSwitches", ["enable-automation"])
c_options.add_experimental_option("useAutomationExtension", False)
c_options.accept_insecure_certs = True



browser = webdriver.Chrome(service=service, options=c_options)
browser.maximize_window()



browser.get("https://www.cacert.com")


time.sleep(5)
browser.quit()
