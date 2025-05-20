from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#Create the class definition
class KeywordLibrary:
    def __init__(self, driver):
        self.driver = driver
    #Open the browser using the url/path from the csv file
    def open_browser(self, url):
        self.driver.get(url)
        self.driver.maximize_window() #??
    #Enter the email from the csv file
    def enter_text(self, locator_type, locator_value, text):
        self.find_element(locator_type, locator_value).send_keys(text)
    #Submit the form
    def click(self,locator_type, locator_value):
        self.find_element(locator_type, locator_value).click()
    #Verify the popup output
    def verify_popup_message(self, expected_message):
        try:
            WebDriverWait(self.driver, 10).until (
                EC.visibility_of_element_located((By.ID, "login-popup"))
            )
            popup_message = self.driver.find_element(By.ID, "login-popup-message").text.strip()
            assert popup_message == expected_message, f"Expected message: '{expected_message}',got: '{popup_message}'"
            print("The popup message has been verified!")
        except Exception as e:
            print("The popup message has failed!:{e}")
    #Create the wait action
    def wait(self,seconds):
        time.sleep(int(seconds))
    #Find the elements
    def find_element(self,locator_type,locator_value):
        locator_map = {
            "id":By.ID,
            "name":By.NAME,
            "class":By.CLASS_NAME,
            "xpath":By.XPATH,
            "css":By.CSS_SELECTOR
        }
        return self.driver.find_element(locator_map[locator_type],locator_value)