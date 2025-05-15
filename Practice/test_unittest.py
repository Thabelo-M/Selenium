import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginPopup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        file_path = os.path.abspath("Login_Page.html")
        self.driver.get("file://" + file_path)

    def test_invalid_email_shows_popup(self):
        driver = self.driver
        driver.find_element(By.CLASS_NAME, "email").send_keys("Selenium25@gmail.com")
        driver.find_element(By.CLASS_NAME, "password").send_keys("Y0uMade1t&3&&")
        driver.find_element(By.ID, "login-btn").click()

        wait = WebDriverWait(driver, 10)
        popup = wait.until(EC.visibility_of_element_located((By.ID, "login-popup")))
        popup_message = driver.find_element(By.ID, "login-popup-message").text

        self.assertTrue(popup.is_displayed(), "Login popup did not display")
        self.assertIn("successfully", popup_message.lower(), f"Unexpected message: {popup_message}")

        time.sleep(3)  # For observation

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()