from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Test_data import credentials
from Test_locators.login_page import LoginPageLocators
import sys
sys.path.append('C:/Users/MOHANA KRISHNA R/PycharmProjects/TC_PIM_01')

class LoginPageActions:

    def __init__(self):
        self.loginlocators = LoginPageLocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def login(self):


        """
        find the webelement for forgot password ,enter the user name in the textbox ,click the resetpassword
        :return:
        """

        forgotpassword_webelement = self.driver.find_element(By.XPATH, self.loginlocators.forgotpassword_button).click()
        sleep(3)
        username_webelement = self.driver.find_element(By.NAME, self.loginlocators.username_tag).send_keys(credentials.username)
        sleep(2)
        resetpassword_webelement = self.driver.find_element(By.XPATH, self.loginlocators.resetpassword_button).click()
        sleep(10)


    def title_of_page(self):

        return self.driver.title





LoginPageActions().login()