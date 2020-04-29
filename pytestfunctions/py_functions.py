from selenium import webdriver


def url_open_chrome_test():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
    driver.get("https://www.google.com/")
    driver.maximize_window()


def url_open_firefox_test():
    browser = webdriver.Firefox(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\geckodriver.exe")
    browser.get("https://www.google.com/")
    browser.maximize_window()






url_open_chrome_test()
url_open_firefox_test()
