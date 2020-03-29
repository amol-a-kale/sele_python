from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver=webdriver.Chrome (executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(3)
search_box=driver.find_element_by_name("q")
#search_box.send_keys("hi")
action = ActionChains(driver) #object
action.key_down(Keys.SHIFT).send_keys("Python").key_up(Keys.SHIFT).perform()
search_box.clear()
#action.key_down(Keys.SHIFT, search_box).send_keys("selenium").key_up(Keys.SHIFT, search_box).perform()

action.key_down(Keys.SHIFT,search_box).send_keys("selenium").key_up(Keys.SHIFT,search_box).perform()
search_box.clear()
sleep(2)
action.key_down("\ue008",search_box).send_keys("selenium").key_up("\ue008",search_box).perform()

sleep(3)
driver.close()
driver.quit()