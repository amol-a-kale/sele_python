from time import sleep
from selenium import webdriver
import pytest


@pytest.fixture(scope='class')
def one_Time_SetUp(request):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\amol2\\webdriver\\chromedriver.exe")
    driver.get("https://www.yatra.com/hotels")
    sleep(4)
    driver.maximize_window()
    sleep(2)
    request.cls.driver = driver
    yield driver

    driver.close()

    driver.quit()



