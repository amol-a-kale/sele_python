from selenium import webdriver
from time import sleep


def test_url_open_chrome_test():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
    driver.get("https://www.goindigo.in/")
    driver.implicitly_wait(2)

    driver.maximize_window()
    page_title = driver.title
    assert page_title == 'Indigo'
    #if page_title == 'Indigo':
        #print("Its matching")
    #else:
        #print('Its not matching')


def test_url_open_firefox_test():
    browser = webdriver.Firefox(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\geckodriver.exe")
    browser.get("https://www.goindigo.in/")
    browser.implicitly_wait(2)

    browser.maximize_window()
    page_title = browser.title
    assert page_title == 'Indigo'

#url_open_chrome_test()
# url_open_firefox_test()
