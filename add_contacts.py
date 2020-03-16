from selenium import webdriver
from time import sleep


def add_contacts_wo_parameter():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\amol2\\webdriver\\chromedriver.exe")
    driver.get("https://freecrm.co.in/")
    sleep(2)
    driver.maximize_window()
    login_btn = driver.find_element_by_xpath("//ul[@class='rd-navbar-nav']/a")
    login_btn.click()

    username = driver.find_element_by_name("email")
    username.send_keys("sharma.rajeshwar9@gmail.com")

    password = driver.find_element_by_name("password")
    password.send_keys("letscode")

    sleep(3)

    login_button = driver.find_element_by_xpath("//div[text()='Login']")
    login_button.click()
    sleep(3)

    left_panel_contact = driver.find_element_by_xpath("//span[text()='Contacts']")
    left_panel_contact.click()

    sleep(3)

    new_btn = driver.find_element_by_xpath("//button[@class='ui linkedin button']/i[@class='edit icon']")
    new_btn.click()

    sleep(3)

    first_name = driver.find_element_by_name("first_name")
    first_name.send_keys("amol")

    last_name = driver.find_element_by_name("last_name")
    last_name.send_keys("patil")

    email = driver.find_element_by_xpath("//input[@placeholder='Email address']")
    email.send_keys("jennysmith@gmale.com")

    sleep(6)
    save_btn = driver.find_element_by_xpath("//button[@class='ui linkedin button']/i[@class='save icon']")
    save_btn.click()
    sleep(5)


add_contacts_wo_parameter()
