#pip install pytest (FIRST)
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login_with_invalid_email(driver):
    file_path = os.path.abspath("Login_Page.html")
    driver.get("file://" + file_path)

    # Fill in the form with invalid email
    driver.find_element(By.CLASS_NAME, "email").send_keys("Selenium25@gmail.com")
    driver.find_element(By.CLASS_NAME, "password").send_keys("Y0uMade1t&3&&")
    driver.find_element(By.ID, "login-btn").click()

    # Wait for popup to appear
    wait = WebDriverWait(driver, 10)
    popup = wait.until(EC.visibility_of_element_located((By.ID, "login-popup")))

    popup_message = driver.find_element(By.ID, "login-popup-message").text

    # assert popup.is_displayed(), "Popup did not appear"
    # assert "successfully" not in popup_message.lower(), "Unexpected success message shown" #If successfully is not in the message shown, it will pass

    assert popup.is_displayed(), "Popup did not appear"
    assert "successfully"  in popup_message.lower(), "Unexpected success message shown" #If successfully is in the message shown, it will pass

    time.sleep(2)
    
# pytest test_pytest.py -v
