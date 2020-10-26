 from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver=webdriver.Chrome (executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
driver.get("https://jqueryui.com")
sleep(3)
driver.maximize_window()
draggable_click=driver.find_element_by_xpath("//a[text()='Draggable']")
draggable_click.click()
iframe_list = driver.find_elements_by_tag_name("iframe") # it is used to find iframe, iframe, new window means new html
#document.we have to siwtch ifrmae for  operation on that  iframe

print(len(iframe_list)) # used this to find index
driver.switch_to.frame(0)
#Drag
draggable_element = driver.find_element_by_id("draggable")
actions= ActionChains(driver)
actions.drag_and_drop_by_offset(draggable_element, 300, 100).perform();
sleep(3)
driver.switch_to.default_content()
#Drag_Drop
droppable_click=driver.find_element_by_xpath("//a[text()='Droppable']")
droppable_click.click()
sleep(3)
driver.switch_to.frame(0)
draggable_element = driver.find_element_by_id("draggable")
droppable_element = driver.find_element_by_id("droppable")
actions=ActionChains(driver)
actions.drag_and_drop(draggable_element, droppable_element).perform()
driver.switch_to.default_content()
#slider
slider_link = driver.find_element_by_xpath("//a[text()='Slider']")
slider_link.click()
driver.switch_to.frame(0)
sleep(5)
slider =driver.find_element_by_xpath("//div/span[@class='ui-slider-handle ui-corner-all ui-state-default']")
actions=ActionChains(driver)
actions.drag_and_drop_by_offset(slider, 100, 0).perform()
sleep(5)
driver.close()
driver.quit()
