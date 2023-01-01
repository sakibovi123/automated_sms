import os
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class SMSBot(webdriver.Chrome):
    def __init__(self, driver=webdriver.Chrome, teardown=False):
        self.driver = driver
        self.teardown = teardown
        # self.wait = WebDriverWait(self.driver, 25)
        super(SMSBot, self).__init__()
        self.maximize_window()
        self.implicitly_wait(10)
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.teardown:
            self.quit()
            

    def go_to_dashboard(self, url):
        self.get(url)
        

    def login_to_dashboard(self, username, password):
        wait = WebDriverWait(self, 25)
        name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Username']")))
        name.click()
        name.send_keys(username)
        passw = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "input[placeholder='Password']"
        )))
        passw.click()
        passw.send_keys(password)
        
        login = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button[type='submit']"
        ))).click()


    def find_campaign_section(self):
        wait = WebDriverWait(self, 25)
        select_campaign = wait.until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, "body > aside:nth-child(1) > nav:nth-child(2) > a:nth-child(6)"
        )))
        select_campaign.click()


    def find_campaign_id(self, camp_id):
        pass

    
