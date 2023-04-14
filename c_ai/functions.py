# selenium is syntactically goofy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



class Character():

    MESSAGE_BOX_ID = 'user-input'
    LOADING_XPATH = "//button[.//div[@role='status']]"
    STOP_BUTTON_XPATH = '//button[@aria-label="Stop Message Generation"]'
    TRY_AGAIN_XPATH = '//button[normalize-space()="Try Again"]'
    
    def __init__(self, id, userdata, headless=False):
        self.id = id
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument(f'user-data-dir={userdata}')

        if headless:
            self.options.add_argument('--headless')
            self.options.add_argument('--disable-gpu')

    def back(self):
        self.driver.get(rf"https://beta.character.ai/chat?char={self.id}")

    def start(self, newchat=False):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.options)
        self.wait = WebDriverWait(self.driver, 30)
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
    
    def prompt(self, message, attempts=3):
        attempts = int("9"*10) if attempts == "inf" else attempts
        self.wait_for_element(By.ID, self.MESSAGE_BOX_ID).send_keys(message)
        for _ in range(attempts):
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.LOADING_XPATH)))
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.STOP_BUTTON_XPATH)))
            if (element:=self.element_exists(By.ID, self.TRY_AGAIN_XPATH)):
                element.click()
                continue
            return self.driver.find_elements(By.XPATH, '//p[@node="[object Object]"]')[-1]
            
            
            
    def retry():
        pass

    def delete():
        pass

    def view():
        pass

    def reset():
        pass

    def __delete__():
        pass

if __name__ == "__main__":
    print("https://i.imgur.com/KCSQ0jb.jpeg")