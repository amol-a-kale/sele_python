from selenium import webdriver
from time import sleep
from utility.screenshot_by_me import TakeScreenshot1 # when we call function from utility package


driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)

# driver.save_screenshot("homepage.png") #This will save the screenshot in the same folder where your script is
#  To save at particular folder, we need to specify path
#screenshot_folder_path = "C:\\Users\\Sanket\\Desktop\\sele_python\\screenshot_save\\" #syntax for folder location
#driver.save_screenshot(screenshot_folder_path + "fb2.png") # syntax for save image on specific floder path
# take screenshot by using object
take_sshot = TakeScreenshot1(driver)
#take_sshot.take_screenshot('fb')
#take dyanamic screen shot
take_sshot.take_screenshot_dynamic()


sleep(3)

driver.close()
driver.quit()



ctions = ActionChains(driver)
source = driver.find_element_by_xpath("(//input[@placeholder='From'])[1]")
source.clear()

actions.move_to_element(source).send_keys("Mumbai").send_keys(Keys.ENTER).perform()

# driver.save_screenshot(screenshot_folder_path + "cityenter.png")
take_ss.take_screenshot_with_dynamic_name()

destination = driver.find_element_by_xpath("(//input[@placeholder='To'])[1]")
destination.clear()
actions.move_to_element(destination).send_keys("Pune").send_keys(Keys.ENTER).perform()

#driver.save_screenshot("loading.png")
take_ss.take_screenshot_with_dynamic_name()

# To define folder path

# driver.save_screenshot(screenshot_folder_path + "loading.png")

sleep(5)
driver.close()
driver.quit()

# # To take screenshot
# driver.save_screenshot("loadingone.png") # This will save the screenshot in the same folder where your script is
# # To save at particular folder, we need to specify path
# sleep(3)
# screenshot_folder_path = "../screenshots"
# driver.save_screenshot(screenshot_folder_path + "anotherloading.png")

