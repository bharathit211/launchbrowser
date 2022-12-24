import time
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://rpademo.automationanywhere.com/itbricks_enroll.php")
driver.maximize_window()
elm_rows=driver.find_elements(by=By.TAG_NAME,value="tr")
for rows in elm_rows:
    print(rows.text)
time.sleep(100)