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
            
    def prompt(self):
        self.wait_for_element(By.ID, self.MESSAGE_BOX_ID)
    def retry():
    
    def delete():
    
    def view():

    def reset():

    def end():


