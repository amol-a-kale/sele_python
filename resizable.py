from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver=webdriver.Chrome (executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
driver.get("https://jqueryui.com/")
driver.maximize_window()
Resizable_link=driver.find_element_by_xpath("//a[text()='Resizable']")
Resizable_link.click()
sleep(3)
driver.switch_to.frame(0)
Resizable_corner=driver.find_elements_by_xpath("//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
#Resizable_corner.click()
actions=ActionChains(driver)
actions.move_to_element_with_offset(Resizable_corner,-100,100).perform()
driver.quit()