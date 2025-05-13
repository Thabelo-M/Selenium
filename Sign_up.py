from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Define the function
def test_signup_popup(driver):
    driver.get("https://softwaretestingv1.praesignis.com/softwaretestingv1/Sign_Up_Page.html")
    time.sleep(1)
#Test Case 001: Fill in the name, email and password
    #driver.find_element(By.ID, "name").send_keys("Thabelo M")
    #driver.find_element(By.ID, "email").send_keys("thabelo34@gmail.com")
    #driver.find_element(By.ID, "password").send_keys("Thabelo$26edf")
#Test Case 002: Invalid email address
    # driver.find_element(By.ID, "name").send_keys("Thabelo M")
    # driver.find_element(By.ID, "email").send_keys("thabelo3gmail.com")
    # driver.find_element(By.ID, "password").send_keys("Thabelo$26edf")
#Test Case 003: Username has a number or symbol
    # driver.find_element(By.ID, "name").send_keys("Thabelo23")
    # driver.find_element(By.ID, "email").send_keys("thabelo3@gmail.com")
    # driver.find_element(By.ID, "password").send_keys("Thabelo$26edf")
#Test Case 004: Empty fileds
    # driver.find_element(By.ID, "name").send_keys(" ")
    # driver.find_element(By.ID, "email").send_keys(" ")
    # driver.find_element(By.ID, "password").send_keys(" ")
#Test Case 005: Weak password
    driver.find_element(By.ID, "name").send_keys("Thabelo")
    driver.find_element(By.ID, "email").send_keys("thabelo@gmail.com")
    driver.find_element(By.ID, "password").send_keys("thabe")
#Submit the form by clicking the Sign Up button
    driver.find_element(By.XPATH, "//form[@id='signupForm']//button[text()='Sign Up']").click()
    time.sleep(2)
#Verify the popup
    popup = driver.find_element(By.ID, "promo-popup")
    popup_message = driver.find_element(By.ID, "promo-popup-message").text

    assert popup.is_displayed(), "Sign-UP popup did not display."
    assert "success" in popup_message.lower(), f"Unexpected message: {popup_message}"

    print("Sign-Up popup test passed on", driver.name)

#Run the test
chrome_driver = webdriver.Chrome()
test_signup_popup(chrome_driver)
chrome_driver.quit()