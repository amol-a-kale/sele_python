from time import time


class TakeScreenshot1():
    def __init__(self, driver):
        self.driver = driver

    def take_screenshot1(self, filename):
        screenshot_folder_path = "C:\\Users\\Sanket\\Desktop\\sele_python\\screenshot_save\\"
        self.driver.save_screenshot(screenshot_folder_path + filename + ".png")

    def take_screenshot_dynamic(self):
        screenshot_folder_path = "C:\\Users\\Sanket\\Desktop\\sele_python\\screenshot_save\\"
        self.driver.save_screenshot(screenshot_folder_path + str(round(time() * 1000)) + ".png")
