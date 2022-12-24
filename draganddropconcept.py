import time
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.switch_to.frame(0)
source_element=driver.find_element(by=By.ID,value="draggable");
destination_element=driver.find_element(by=By.ID,value="droppable");
action=ActionChains(driver)
action.drag_and_drop(source_element,destination_element).perform()
time.sleep(100)