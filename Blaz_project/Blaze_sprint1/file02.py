from time import sleep

from selenium import webdriver
# from utility.take_screenshot import TakeScreenshot


driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
driver.save_screenshot("C:\\Users\\Sanket\\Desktop\\sele_python\\Blaz_screenshot\\homepage.png")
sleep(5)
laptop_icon = driver.find_element_by_xpath("//div/a[text()='Laptops']").click()
select_product = driver.find_element_by_xpath("//div/h4/a[text()='Sony vaio i5']").click()
sleep(3)
product_detail_title = driver.find_element_by_class_name("name").text
assert product_detail_title == 'Sony vaio i5'

# product_title = product_detail_title.text
# print(product_title)
product_prize = driver.find_element_by_class_name("price-container").text
assert product_prize == "$790 *includes tax"
# print(product_prize)
is_displayed = driver.find_element_by_xpath("//div[@class='tab-pane fade active in']/p").is_displayed()
assert True == is_displayed

# product_description = driver.find_element_by_xpath("//div[@class='tab-pane fade active in']/p").text
# assert product_description

# print(product_description)


sleep(3)
driver.close()
driver.quit()
