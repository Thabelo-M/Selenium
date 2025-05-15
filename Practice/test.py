import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='login_test.log',
    filemode='w'
)

def test_login_popup(driver):
    file_path = os.path.abspath("Login_Page.html")
    logging.info("Opening file: %s", file_path)
    driver.get("file://" + file_path)

    try:
        # Test Case 1: Correct credentials
        # logging.info("Entering email and password")
        # driver.find_element(By.CLASS_NAME, "email").send_keys("Selenium25@gmail.com")
        # driver.find_element(By.CLASS_NAME, "password").send_keys("Y0uMade1t&3&&")
        # driver.find_element(By.ID, "login-btn").click()

        # Test Case 2
        logging.warning("Testing incorrect email")
        driver.find_element(By.CLASS_NAME, "email").send_keys("Selenium@gmail.com")
        driver.find_element(By.CLASS_NAME, "password").send_keys("Y0uMade1t&3&&")
        driver.find_element(By.ID, "login-btn").click()
        #Test Case 3
        # logging.error("Testing badly formatted email")
        # driver.find_element(By.CLASS_NAME, "email").send_keys("Sekenium@gmail")
        # driver.find_element(By.CLASS_NAME, "password").send_keys("Yahoo#21678")
        # driver.find_element(By.ID, "login-btn").click()

        driver.save_screenshot("screenshot_before_popup.png")
        logging.info("Screenshot saved before popup appears")

        wait = WebDriverWait(driver, 10)
        popup = wait.until(EC.visibility_of_element_located((By.ID, "login-popup")))
        popup_message = driver.find_element(By.ID, "login-popup-message").text
        logging.info("Popup message: %s", popup_message)

        assert popup.is_displayed(), "Login popup did not display"
        assert "successfully" in popup_message.lower(), f"Unexpected message: {popup_message}"

        logging.info("Login popup test passed on %s", driver.name)
        time.sleep(3)

    except Exception as e:
        logging.error("An error occurred during the test: %s", e)
        driver.save_screenshot("error_screenshot.png")
        raise

# Run
chrome_driver = webdriver.Chrome()
test_login_popup(chrome_driver)
chrome_driver.quit()