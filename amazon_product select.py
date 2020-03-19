from selenium import webdriver
import time

from time import sleep

driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")

driver.get("https://www.amazon.in")

driver.maximize_window()

page_title = driver.title

print(page_title)

search_box = driver.find_element_by_id("twotabsearchtextbox")
search_box.send_keys("Macbook Pro 15 inch")

search_icon = driver.find_element_by_xpath("//input[@type='submit']")
search_icon.click()
sleep(3)

expected_product_list = ['Apple MacBook Pro (15-inch, Latest Model, 16GB RAM, 512GB Storage, 2.3GHz Intel Core i9) - Space Grey',
    'Apple MacBook Air (13-inch, Previous Model, 8GB RAM, 128GB Storage, 1.6GHz Intel Core i5) - Gold']

products_list = driver.find_elements_by_xpath(
    "//span[@class='a-size-medium a-color-base a-text-normal']")
for expected_product in expected_product_list:
    for product in products_list:
        #print(product.text)
        if (expected_product==product.text):
            product.click()
            sleep(2)
            parent_window = driver.current_window_handle  # parent window - String
            windows_list = driver.window_handles  # parent & child windows - Set of Strings
            for window in windows_list:
                if (window != parent_window):
                    driver.switch_to.window(window)
                    # driver.switch_to_window(window)
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
                    driver.switch_to.window(parent_window)
                    sleep(3)

# for product in products_list:
#     print(product.text)
#     if (product.text == 'New Apple MacBook Pro (13-inch, 8GB RAM, 128GB Storage, 1.4GHz Intel Core i5) - Space Grey'):
#         product.click()
#         sleep(2)
#         break

# parent_window = driver.current_window_handle
# windows_list = driver.window_handles
#
# for window in windows_list:
#     if (window != parent_window):
#         driver.switch_to.window(window)
#         # driver.switch_to_window(window)
#         product_detail_title = driver.find_element_by_id("productTitle")
#         product_title = product_detail_title.text
#         print(product_title)
#
#         product_detail_price = driver.find_element_by_id("priceblock_ourprice")
#         product_price = product_detail_price.text
#         print(product_price)
#
#         product_detail_rating = driver.find_element_by_id("acrCustomerReviewText")
#         product_rating = product_detail_rating.text
#         print(product_rating)
#
# driver.switch_to.window(parent_window)

sleep(3)

driver.close()
driver.quit()