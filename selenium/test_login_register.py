from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = "http://<MANAGER_PUBLIC_IP>:8000"  # replace with actual manager IP

driver = webdriver.Chrome()
try:
    # Register
    driver.get(BASE_URL + "/register/")
    driver.find_element(By.NAME, "username").send_keys("ITA700")
    driver.find_element(By.NAME, "password").send_keys("2022PE0000")
    driver.find_element(By.TAG_NAME, "form").submit()
    time.sleep(2)

    # Login
    driver.get(BASE_URL + "/login/")
    driver.find_element(By.NAME, "username").send_keys("ITA700")
    driver.find_element(By.NAME, "password").send_keys("2022PE0000")
    driver.find_element(By.TAG_NAME, "form").submit()
    time.sleep(2)

    assert "Hello ITA700 How are you" in driver.page_source
    print("Selenium test passed")
finally:
    driver.quit()
