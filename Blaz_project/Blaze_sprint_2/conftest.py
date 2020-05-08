from selenium import webdriver
import pytest
from time import sleep


@pytest.fixture(scope='class')
def oneTimeSetUp(request):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
    driver.get("https://www.yatra.com/")
    sleep(4)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
    print('driver quit')
    driver.quit()
