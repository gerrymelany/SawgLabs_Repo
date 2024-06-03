import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

if os.getenv("CI"):
    driver = webdriver.Chrome()
else:
    chrome_options.binary_location = 'executable_path=/home/mgerry/path/chromedriver'
    driver = webdriver.Chrome(options=chrome_options)

def before_all(context):
    global driver
    context.driver = driver
    context.driver.implicitly_wait(10)
    context.base_url = "https://www.saucedemo.com/"

def after_all(context):
    context.driver.quit()