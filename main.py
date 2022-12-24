import time
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui
global driver
driver=webdriver.Chrome(executable_path="C:\\Users\\USER\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://rpademo.automationanywhere.com")
driver.find_element(by=By.XPATH,value="//*[@id='username']").send_keys("testuser")
driver.find_element("id","password").send_keys("mypassword")
driver.find_element("id","mybutton").click()
actual_url=driver.current_url
expected_url="https://rpademo.automationanywhere.com"
if actual_url!=expected_url:
    print("success")
else:
    print("fail")
time.sleep(100)