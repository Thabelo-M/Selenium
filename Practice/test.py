from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def test_login_popup(driver):
    file_path = os.path.abspath("Login_Page.html")
    print("Opening file:", file_path)
    driver.get("file://" + file_path)

#Test Case 1: Correct credentials
    # driver.find_element(By.CLASS_NAME, "email").send_keys("Selenium25@gmail.com")
    # driver.find_element(By.CLASS_NAME, "password").send_keys("Y0uMade1t&3&&")
#Test Case 2: Incorrect email
    # driver.find_element(By.CLASS_NAME, "email").send_keys("Selenium@gmail.com")
    # driver.find_element(By.CLASS_NAME, "password").send_keys("Y0uMade1t&3&&")
#Test Case 3: 
    driver.find_element(By.CLASS_NAME, "email").send_keys("Sekenium@gmail")
    driver.find_element(By.CLASS_NAME, "password").send_keys("Yahoo#21678")
    # Click login
    driver.find_element(By.ID, "login-btn").click()

    # Wait for popup
    wait = WebDriverWait(driver, 1)
    popup = wait.until(EC.visibility_of_element_located((By.ID, "login-popup")))
    popup_message = driver.find_element(By.ID, "login-popup-message").text

    # Assertions
    assert popup.is_displayed(), "Login popup did not display"
    assert "successfully" in popup_message.lower(), f"Unexpected message: {popup_message}"

    print("Login popup test passed on", driver.name)

    # Wait 3 seconds to observe popup before closing
    time.sleep(10)

# Run
chrome_driver = webdriver.Chrome()
test_login_popup(chrome_driver)
chrome_driver.quit()