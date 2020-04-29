from selenium import webdriver
import pytest


def test_url_open_chrome():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
    driver.get("https://www.google.com/")
    driver.maximize_window()


def test_url_open_firefox():
    browser = webdriver.Firefox(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\geckodriver.exe")
    browser.get("https://www.goindigo.in/")
    browser.maximize_window()

# url_open_chrome_test()
# url_open_firefox_test()
