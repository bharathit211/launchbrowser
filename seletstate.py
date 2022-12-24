import time
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://www.collegesearch.in/college-registration.php")
driver.maximize_window()
drp_state=driver.find_element(by=By.ID,value="state")
select=Select(drp_state)
select.select_by_visible_text("Kerala")

time.sleep(100)
