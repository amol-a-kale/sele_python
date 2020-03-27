from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.implicitly_wait(5)
driver.maximize_window()
radio_btn=driver.find_element_by_id("u_0_8")
radio_btn.click()
custom_dropdown=driver.find_element_by_name("preferred_pronoun")
#custom_dropdown.click()
select_class=Select(custom_dropdown)
sleep(3)
select_class.select_by_value("6")
sleep(5)
driver.close()
driver.quit()

