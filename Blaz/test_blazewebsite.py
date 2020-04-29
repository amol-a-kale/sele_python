from time import sleep
import pytest
from selenium import webdriver


@pytest.mark.usefixtures("oneTimeSetUp")
class Test_blazewebsite:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_screenshot\\homepage.png")

    def test_laptops_view(self, setup):
        laptop_icon = self.driver.find_element_by_xpath("//div/a[text()='Laptops']").click()
        sleep(3)
        self.driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_screenshot\\laptop.png")

        laptop_expected_view_list = ['Sony vaio i5', 'Sony vaio i7', 'MacBook air', 'Dell i7 8gb',
                                     '2017 Dell 15.6 Inch', 'MacBook Pro']

        laptop_actual_view_list = []
        find_product = self.driver.find_elements_by_xpath("//div/h4/a")
        for product in find_product:
            laptop_actual_view_list.append(product.text)
        assert laptop_expected_view_list == laptop_actual_view_list

    def test_monitors_view(self, setup):
        monitors_icon = self.driver.find_element_by_xpath("//a[text()='Monitors']").click()
        sleep(5)
        self.driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_screenshot\\monitors.png")

        monitors_expected_view_list = ['Apple monitor 24', 'ASUS Full HD']
        monitors_actual_view_list = []
        find1_product = self.driver.find_elements_by_xpath("//div/h4/a")
        for product in find1_product:
            monitors_actual_view_list.append(product.text)
        assert monitors_expected_view_list == monitors_actual_view_list


@pytest.mark.usefixtures("oneTimeSetUp")

class Test_blazewebsite1:
    @pytest.fixture(scope="class")
    def setup(self):
        laptop_icon = self.driver.find_element_by_xpath("//div/a[text()='Laptops']").click()
        self.driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_screenshot\\homepage.png")
        select_product = self.driver.find_element_by_xpath("//div/h4/a[text()='Sony vaio i5']").click()

        sleep(3)

        # self.driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_screenshot\\homepage.png")

    def test_View_product_title(self, setup):
        product_detail_title = self.driver.find_element_by_class_name("name").text
        self.driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_screenshot\\select_product.png")

        assert product_detail_title == 'Sony vaio i5'

    def test_view_product_price(self, setup):
        product_prize = self.driver.find_element_by_class_name("price-container").text
        assert product_prize == "$790 *includes tax"

    def test_view_product_description(self, setup):
        is_displayed = self.driver.find_element_by_xpath("//div[@class='tab-pane fade active in']/p").is_displayed()
        assert True == is_displayed
