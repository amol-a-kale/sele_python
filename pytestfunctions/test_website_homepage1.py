from selenium import webdriver
from time import sleep

import pytest


# from pytestfunctions import conftest
# from conftest import OneTimeSetUp


# def SetUp():
#     print('setting driver path')
#     print('launching Browser')
#     yield
#     print('driver close')
# driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
@pytest.fixture(scope="module")
def OneTimeSetUp():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
    driver.get("https://www.google.com/")
    sleep(4)
    driver.maximize_window()
    yield driver
    print("driver close")
    driver.close()
    print("driver quite")
    driver.quit()


def test_browser_launch(self, OneTimeSetUp):
    print('Getting homepage title')
    page_title = self.driver.title
    print('Comparing title')
    assert page_title == 'google.com'
    # page_title = self.driver.title
    # print(page_title)
    # assert True

# def test_homepage_title(OneTimeSetUp):
#     print('getting homepage title')
#     print('comparing title')
#     assert True
#
# def test_homepage_link(OneTimeSetUp):
#     print('getting all links')
#     print('validating links from homepage')
#     assert False
# from selenium import webdriver


# @pytest.fixture
# def OneTimeSetUp(request):
#     driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
#     driver.get("https://www.google.com/")
#     sleep(4)
#     driver.maximize_window()
#     request.cls.driver = driver  # check this one
#     yield driver
#     print("driver close")
#     driver.close()
#     print("driver quite")
#     driver.quit()
# def test_browser_launch(OneTimeSetUp):
#     page_title = driver.title
#     print(page_title)
#     assert True
