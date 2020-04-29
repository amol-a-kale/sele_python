# As an end-user, I should able to view the details of selected laptop product - AK

from time import sleep
import pytest
from selenium import webdriver


@pytest.mark.usefixtures("oneTimeSetUp")
class Test_blaz_07:  # this class define for  view the details of selected laptop product
    @pytest.fixture(scope="class")
    def setup(self):
        laptop_icon = self.driver.find_element_by_xpath("//div/a[text()='Laptops']").click()  # click on laptop category

        self.driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_screenshot\\Blaz07\\homepage.png")

        select_product = self.driver.find_element_by_xpath(
            "//div/h4/a[text()='Sony vaio i5']").click()  # select product

        sleep(3)

    # define function for  check title

    def test_View_product_title(self, setup):
        product_detail_title = self.driver.find_element_by_class_name("name").text # find product title

        self.driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_screenshot\\Blaz07\\select_product.png")

        assert product_detail_title == 'Sony vaio i5'

    # define function for  check price

    def test_view_product_price(self, setup):
        product_prize = self.driver.find_element_by_class_name("price-container").text # find product price
        assert product_prize == "$790 *includes tax"

    # define function for  check description

    def test_view_product_description(self, setup):
        is_displayed = self.driver.find_element_by_xpath("//div[@class='tab-pane fade active in']/p").is_displayed()
        assert True == is_displayed
