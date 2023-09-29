from selenium import webdriver
from selenium.webdriver.common.by import By  #Set of supported locator strategies
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/") #OPEN GIVEN PAGE
#driver.find_element(By.ID, "kc-login").click()
driver.find_element(By.NAME, "enter-name").send_keys("Sanjana")
driver.find_element(By.ID, "checkBoxOption2").click()
title = driver.title  #Returns the title of the current page
assert "Practice Page" in title
print(title)
#driver.quit() CLOSE THE OPEN WINDOW (WEB DRIVER METHOD)