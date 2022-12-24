import time
from selenium.webdriver.chromium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\Users\\USER\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://www.collegesearch.in/college-registration.php")
driver.maximize_window()
ischbox_selected=driver.find_element(by=By.ID,value="agree").is_selected()
print(ischbox_selected)
ischbox_selected=driver.find_element(by=By.ID,value="agree").click()
ischbox_selected=driver.find_element(by=By.ID,value="agree").is_selected()
print(ischbox_selected)

time.sleep(100)
