from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.implicitly_wait(5)
driver.maximize_window()

select_date = driver.find_element_by_id("day")

select_class = Select(select_date) # use for select location
select_class.select_by_index(2)# we can use index,value,text
select_month = driver.find_element_by_id("month")

select_class1 = Select(select_month) # use for select location
select_class1.select_by_index(2)
select_year = driver.find_element_by_id("year")

select_class2 = Select(select_year) # use for select location
select_class2.select_by_index(2)
#select_class.select_by_visible_text("Aug");


sleep(3)
driver.close()
driver.quit()