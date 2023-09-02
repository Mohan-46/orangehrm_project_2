from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from Test_data import credentials
from Test_locators.login_page import LoginPageLocators
import sys
sys.path.append('C:/Users/MOHANA KRISHNA R/PycharmProjects/TC_PIM_03')



class LoginPageActions:

    def __init__(self):
        self.loginlocators = LoginPageLocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def login(self):


        """
        find the webelement for username ,clear the text field and set the username passed
        :return:
        """

        username_webelement = self.driver.find_element(By.NAME, self.loginlocators.username_tag).send_keys(credentials.username)
        # username_webelement.clear()
        # username_webelement.send_keys(credentials.username)
        password_webelement = self.driver.find_element(By.NAME, self.loginlocators.password_locator_name_tag).send_keys(credentials.password)
        login_button_webelement = self.driver.find_element(By.XPATH, self.loginlocators.login_button).click()
        Admin_webelement = self.driver.find_element(By.XPATH, self.loginlocators.Admin_button).click()
        pim_webelement = self.driver.find_element(By.XPATH, self.loginlocators.pim_button).click()
        leave_webelement = self.driver.find_element(By.XPATH, self.loginlocators.leave_button).click()
        time_webelement = self.driver.find_element(By.XPATH, self.loginlocators.time_button).click()
        requirement_webelement = self.driver.find_element(By.XPATH, self.loginlocators.requirement_button).click()
        info_webelement = self.driver.find_element(By.XPATH, self.loginlocators.info_button).click()
        perform_webelement = self.driver.find_element(By.XPATH, self.loginlocators.perform_button).click()
        dash_webelement = self.driver.find_element(By.XPATH, self.loginlocators.dash_button).click()
        direct_webelement = self.driver.find_element(By.XPATH, self.loginlocators.direct_button).click()
        main_webelement = self.driver.find_element(By.XPATH,self.loginlocators.main_button).click()
        main_webelement = self.driver.find_element(By.XPATH, self.loginlocators.main_password).send_keys(credentials.password)
        main_webelement = self.driver.find_element(By.XPATH,self.loginlocators.main_confirm).click()
        claim_webelement = self.driver.find_element(By.XPATH,self.loginlocators.claim_button).click()
        buzz_webelement = self.driver.find_element(By.XPATH,self.loginlocators.buzz_button).click()
        sleep(5)


LoginPageActions().login()


