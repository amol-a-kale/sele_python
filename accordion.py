from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from time import sleep
driver=webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
driver.get('https://jqueryui.com/accordion/')
print(driver.title)
driver.maximize_window()
sleep(4)
driver.switch_to.frame(0)
section_list=driver.find_elements_by_css_selector("#accordion > h3")
#section_list=driver.find_elements_by_xpath('//div[@id="accordion"]/h3')
print("length_of_list:",len(section_list))
action=ActionChains(driver)
i=1
for section in section_list:
    action.move_to_element(section).click().perform()
    driver.execute_script("arguments[0].scrollIntoView();",section)
    sleep(8)
    section_text=driver.find_element_by_css_selector("div[aria-labelledby='ui-id-"+str(i)+"']")
    sleep(4)
    print(":",section_text.text)
    sleep(4)
    i=i+2
sleep(4)
driver.close()
driver.quit()


