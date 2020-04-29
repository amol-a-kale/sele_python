from selenium import webdriver
import pytest

# when we use pytest, we must save program file by start or end  test word and always start write a define function name
# from test word
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
