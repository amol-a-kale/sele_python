from selenium import webdriver
from time import sleep
driver=webdriver.Chrome(executable_path="C:\\Users\\Sanket\\amol2\\webdriver\\chromedriver.exe")
driver.get("https://freecrm.co.in/")
login_btn=driver.find_element_by_xpath("//span[text()='Log In']")
login_btn.click()
username=driver.find_element_by_name("email")
username.send_keys("sharma.rajeshwar9@gmail.com")
user_password=driver.find_element_by_name("password")
user_password.send_keys("letscode")
sleep(2)
login_button=driver.find_element_by_xpath("//div[text()='Login']")
login_button.click()
sleep(3)
left_pane_items_list = driver.find_elements_by_xpath("//div[@id='main-nav']//span")

expected_items_list = ['Home', 'Calendar', 'Contacts', 'Companies', 'Deals', 'Tasks', 'Cases', 'Calls', 'Documents', 'Email', 'Campaigns', 'Forms']
for i in range(0,len(expected_items_list)):
    print(left_pane_items_list[i].text)
    item_actual_text = left_pane_items_list[i].text
    if (item_actual_text == expected_items_list[i]):
        print(item_actual_text + "is matching with " + expected_items_list[i])
    else:
        print(item_actual_text + "is not matching with " + expected_items_list[i])

    sleep(10)
driver.close()
driver.quit()