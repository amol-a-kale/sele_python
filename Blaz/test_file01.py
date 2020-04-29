from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

# driver: WebDriver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")



@pytest.fixture(scope='module')
def setup():
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()
    yield driver
    sleep(6)
    driver.close()
    driver.quit()


def test_laptops_view(setup):
    laptop_icon = driver.find_element_by_xpath("//div/a[text()='Laptops']")
    laptop_icon.click()
    laptop_expected_list = ['Samsung galaxy s6', 'Nokia lumia 1520', 'Nexus 6', 'Samsung galaxy s7',
                            'Iphone 6 32gb',
                            'Sony xperia z5', 'HTC One M9', 'Sony vaio i5', 'Sony vaio i7']
    laptop_actual_list = []
    find_product = driver.find_elements_by_xpath("//div/h4/a")
    for product in find_product:
        laptop_actual_list.append(product.text)
    assert laptop_expected_list == laptop_actual_list
    print('able to view laptop product')


def test_monitors_view(setup):
    monitors_icon = driver.find_element_by_xpath("//a[text()='Monitors']")
    monitors_icon.click()
    sleep(5)
    monitors_expected_list = ['Apple monitor 24', 'ASUS Full HD']
    monitors_actual_list = []
    find1_product = driver.find_elements_by_xpath("//div/h4/a")
    for product in find1_product:
        monitors_actual_list.append(product.text)
    assert monitors_expected_list == monitors_actual_list
    print('able to view monitors product')
