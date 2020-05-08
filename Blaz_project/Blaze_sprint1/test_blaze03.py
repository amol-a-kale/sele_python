# As an end user, I should able to view the computer products after clicking on computer from home page - AK

from time import sleep
import pytest
from selenium import webdriver


@pytest.mark.usefixtures("oneTimeSetUp")
class Test_blaze_03:
    @pytest.fixture(scope="class")  # used for setup file runs  once
    def setup(self):
        self.driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_screenshot\\Blaz03\\homepage.png")

    # define function for  view the laptop product
    def test_laptops_view(self, setup):
        laptop_icon = self.driver.find_element_by_xpath("//div/a[text()='Laptops']").click()  # click on laptop category
        sleep(3)

        self.driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_screenshot\\Blaz03\\laptop.png")

        # take expected laptop product list
        laptop_expected_view_list = ['Sony vaio i5', 'Sony vaio i7', 'MacBook air', 'Dell i7 8gb',
                                     '2017 Dell 15.6 Inch', 'MacBook Pro']

        # find the actual laptop list
        laptop_actual_view_list = []
        find_product = self.driver.find_elements_by_xpath("//div/h4/a")  # find actual product on window

        for product in find_product:
            laptop_actual_view_list.append(product.text)
        assert laptop_expected_view_list == laptop_actual_view_list  # compare actual and expected product list

    # define function for  view the monitors product
    def test_monitors_view(self, setup):
        monitors_icon = self.driver.find_element_by_xpath("//a[text()='Monitors']").click()  # click on monitor category

        sleep(5)
        self.driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_screenshot\\Blaz03\\monitors.png")

        # take expected monitors product list
        monitors_expected_view_list = ['Apple monitor 24', 'ASUS Full HD']

        monitors_actual_view_list = []
        find1_product = self.driver.find_elements_by_xpath("//div/h4/a")  # find actual product on window

        for product in find1_product:
            monitors_actual_view_list.append(product.text)
        assert monitors_expected_view_list == monitors_actual_view_list
