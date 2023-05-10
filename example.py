from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
import time

service = FirefoxService(
    executable_path='Z:\alryum\python_projects\kaspi_bot\drivers\geckodriver.exe')

browser = webdriver.Firefox(service=service)

browser.get('https://www.chunkbase.com/')


try:
    header = browser.find_element(By.CSS_SELECTOR, "#navwrap")
    print('load header')
    button = header.find_element(By.XPATH, '//*[@id="navapps"]')
    print('load button')
    button.click()
    print('clicked')
    time.sleep(3)
finally:
    browser.quit()
