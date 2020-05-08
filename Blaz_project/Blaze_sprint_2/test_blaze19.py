from selenium import webdriver
import time
import pytest


@pytest.mark.usefixtures("oneTimeSetUp")
class Test_hotel_offers:
    def setup(self):
        self.driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_project\\Blaz_screenshot\\Blaz19\\homepage.png")

    def test_find_hotel_offers(self):
        select_offers_tab = self.driver.find_element_by_xpath("//li[@class='list-dropdown ytHeaderOffers']/a").click()
        self.driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_project\\Blaz_screenshot\\Blaz19\\offer.png")

        time.sleep(2)
        select_hotels_tab = self.driver.find_element_by_xpath("(//a[text()='Hotels'])[1]").click()

        time.sleep(5)
        self.driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_project\\Blaz_screenshot\\Blaz19\\hotels.png")

        expected_offers_title = ['Escapes By Yatra', 'Treebo Offer', 'Flat 10% Cashback', 'Up to Rs.800 SuperCash',
                                 'Exclusive Offer', 'Budget hotels at smart prices']
        actual_offers_title = []
        find_actual_offers = self.driver.find_elements_by_xpath("//span[@class='offerMainTitle']")
        for offer in find_actual_offers:
            actual_offers_title.append(offer.text)
        assert expected_offers_title == actual_offers_title
        print("user able to see hotels offers")