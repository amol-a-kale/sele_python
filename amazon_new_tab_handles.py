from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

driver=webdriver.Chrome(executable_path="C:\\Users\\Sanket\\amol2\\webdriver\\chromedriver.exe")
driver.get("https://www.amazon.in")
driver.maximize_window()
text_box=driver.find_element_by_id("twotabsearchtextbox")
text_box.send_keys("Macbook Pro 15 inch")
search_icon = driver.find_element_by_xpath("//input[@type='submit']")
search_icon.click()
sleep(3)
expected_product=driver.find_element_by_xpath(
    "(//div[@class='s-include-content-margin s-border-bottom']//a[@class='a-link-normal a-text-normal'])[3]")
expected_product_text=expected_product.text
print(expected_product_text)
sleep(2)
products_list = driver.find_elements_by_xpath(
    "//div[@class='s-include-content-margin s-border-bottom']//a[@class='a-link-normal a-text-normal']")
for product in products_list:
    #print(product.text)


    if product.text == expected_product_text:
        product.click()
        sleep(2)
        parent_window = driver.current_window_handle
        windows_list = driver.window_handles
        for window in windows_list:
            if window != parent_window:
                sleep(2)
                driver.switch_to.window(window)
                driver.title
                sleep(3)
                product_detail_title = driver.find_element_by_id("productTitle")
                product_title = product_detail_title.text
                print(product_title)
                product_detail_price = driver.find_element_by_id("priceblock_ourprice")
                product_price = product_detail_price.text
                print(product_price)

                product_detail_rating = driver.find_element_by_id("acrCustomerReviewText")
                product_rating = product_detail_rating.text
                print(product_rating)
                sleep(3)
                driver.close()
                driver.quit()










