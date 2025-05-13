from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Define the function
def test_login_popup(driver):
    driver.get("https://softwaretestingv1.praesignis.com/softwaretestingv1/Login_Page.html")
    time.sleep(2)
#Test Case 01: Fill in the correct credentials
    driver.find_element(By.ID, "email").send_keys("softwaretester@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Sm@rt202$")
#Test Case 02: Invalid Email + Correct password
    # driver.find_element(By.ID, "email").send_keys("tester@gmail.com")
    # driver.find_element(By.ID, "password").send_keys("Sm@rt202$")
#Test Case 03: Use a different ID selector name
    # driver.find_element(By.ID, "name").send_keys("softwaretester@gmail.com")
    # driver.find_element(By.ID, "passwords").send_keys("Sm@rt202$")
#Test Cases to try by yourself:
    # Empty fields
    # Correct email + empty password
    # Whitespace handling
    # Invalid password
#Click the login button
    driver.find_element(By.XPATH, "//form[@id='loginForm']//button[text()='Log In']").click()
    time.sleep(2) #use different seconds
#Verify the popup
    popup = driver.find_element(By.ID,"login-popup")
    popup_message = driver.find_element(By.ID,"login-popup-message").text
    
    assert popup.is_displayed(),"Login popup did not display"
    assert "success" in popup_message.lower(),f"Unexpected message: {popup_message}"
    
    print("Login popup test passed", driver.name)
#Run on Chrome
chrome_driver = webdriver.Chrome()
test_login_popup(chrome_driver)
chrome_driver.quit()