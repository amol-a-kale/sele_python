from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
sleep(5)
laptop_icon=driver.find_element_by_xpath("//div/a[text()='Laptops']")
laptop_icon.click()
sleep(3)
laptop_expected_list=['Sony vaio i5', 'Sony vaio i7', 'MacBook air', 'Dell i7 8gb', '2017 Dell 15.6 Inch', 'MacBook Pro']

laptop_actual_list=[]
find_product=driver.find_elements_by_xpath("//div/h4/a")


for product in find_product:
    laptop_actual_list.append(product.text)
print(laptop_actual_list)
# if laptop_expected_list==laptop_actual_list:
#     print('it is dispaly')

assert laptop_expected_list==laptop_actual_list
print('It is display')

monitors_icon = driver.find_element_by_xpath("//a[text()='Monitors']")
monitors_icon.click()
sleep(3)
find1_product = driver.find_elements_by_xpath("//div/h4/a")
# print(find1_product.text)
list=[]
for product in find1_product:
    list.append(product.text)
print(list)

sleep(5)
driver.close()
driver.quit()


