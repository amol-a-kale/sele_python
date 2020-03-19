from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep


from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")

driver.get("https://aiims.edu/en.html")

driver.maximize_window()

sleep(10)
tenders = driver.find_element(By.XPATH, "//a[@title='Tenders']")
actions = ActionChains(driver)
actions.move_to_element(tenders).perform() # when we use action class then use this  perform call operation
Aiims_tenders = driver.find_element(By.XPATH, "//span/span[text()='AIIMS Tenders']")
actions.move_to_element(Aiims_tenders).click().perform()
tender_title=driver.find_elements(By.XPATH, "//td/a")
sleep(10)
tender_title_list=[]
for title in tender_title:
    title_tender=title.text
    tender_title_list.append(title_tender)
print(tender_title_list)
p

driver.close()
driver.quit()