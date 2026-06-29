from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_valid_login():

    # Launch Chrome
    driver = webdriver.Chrome()

    # Maximize browser
    driver.maximize_window()

    # Open login page
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Wait for page to load
    time.sleep(2)

    # Enter username
    username = driver.find_element(By.ID, "username")
    username.send_keys("testuser")

    # Enter password
    password = driver.find_element(By.ID, "password")
    password.send_keys("Password123")

    # Click Login button
    login_button = driver.find_element(By.ID, "loginButton")
    login_button.click()

    # Wait for login
    time.sleep(3)

    # Verify successful login
    assert "Dashboard" in driver.title

    # Close browser
    driver.quit()