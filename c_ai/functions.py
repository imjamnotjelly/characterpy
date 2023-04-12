# selenium is syntactically goofy
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from c_ai.exeptions import *

class Character():

    MESSAGE_BOX_ID = 'user-input'
    TRY_AGAIN_ID = ""
    
    def __init__(self, id, headless=False):
        self.id = id
        self.options = webdriver.FirefoxOptions()

        if headless:
            self.options.add_argument('--headless')
            self.options.add_argument('--disable-gpu')

    def back(self):
        self.driver.get(f"https://beta.character.ai/chat?char={self.id})")

    def start(self, newchat=False):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=self.options)
        self.back()
        if newchat:
            self.reset()
    
    def wait_for_element(self, by, content, visible=True):
        while True:
            try:
                element = self.driver.find_element(by, content)
                if visible and not element.is_displayed():
                    continue
            except NoSuchElementException:
                continue
            else:
                return element
    def element_exists(self, by, content):
        try:
            element = self.driver.find_element(by, content)
        except NoSuchElementException:
            return False
        return element
    
    def prompt(self, message, attempts=5):
        attempts = int("9"*50) if attempts == 'inf' else attempts
        self.wait_for_element(By.ID, self.MESSAGE_BOX_ID).send_keys(message)
        for i in range(attempts):
            if (element:=self.element_exists(By.ID, self.TRY_AGAIN_ID)):
                element.click()
                continue
            
    def retry():
    
    def delete():
    
    def view():

    def reset():

    def end():


