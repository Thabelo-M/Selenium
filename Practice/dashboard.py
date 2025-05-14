from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver (adjust if using Firefox or a different browser)
driver = webdriver.Chrome()

try:
    # Open your dashboard (update path if needed)
    driver.get("file:///C:/Users/ThabeloMuthuvhukuma/OneDrive - Praesignis/Desktop/Selenium_Practice/Selenium/Practice/Dashboard.html")

    time.sleep(1)  # Give time for page to load

# Test 1: Welcome message is displayed
    # header = driver.find_element(By.TAG_NAME, "h1")
    # assert "Welcome, Thabelo!" in header.text
    # print("✅ Welcome message found.")


# Test 3: Logout button exists and is clickable
    logout_btn = driver.find_element(By.CLASS_NAME, "logout-btn")
    # assert logout_btn.is_displayed() and logout_btn.is_enabled()
    # print("✅ Logout button is present.")

# Test 4: Navigation links
    # nav_links = driver.find_elements(By.TAG_NAME, "a")
    # nav_texts = [link.text for link in nav_links]
    # for expected in ["Home", "Submit Leave", "Leave History", "Profile"]:
    #     assert expected in nav_texts
    # print("✅ Navigation links verified.")

# # Test 5: Search box presence
#     search_box = driver.find_element(By.ID, "search-box")
#     assert search_box.is_displayed()
#     search_box.send_keys("go")
#     print("✅ Search box is functional.")

# # Test 6: Profile image
    # profile_img = driver.find_element(By.CSS_SELECTOR, ".profile-img img")
    # assert profile_img.get_attribute("src") != ""
    # print("✅ Profile image found.")

# # Test 7: Calendar input
    calendar = driver.find_element(By.ID, "calendar")
    calendar.send_keys("2025/07/17")
    print("✅ Calendar input works.")
# Test 5: Search box filters cards
    # search_box = driver.find_element(By.ID, "search-box")
    # search_box.send_keys("approved")
    # time.sleep(1) 
# # Test 8: Logout button action (simulate click)
    logout_btn.click()
    time.sleep(1)
    alert = driver.switch_to.alert
    assert "logged out" in alert.text
    alert.accept()
    print("✅ Logout alert verified.")

except AssertionError as e:
    print("Test failed:", e)
except Exception as e:
    print("Error occurred:", e)
finally:
    time.sleep(2)
    driver.quit()