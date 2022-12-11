# Bài 4

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(executable_path='/chromedriver', chrome_options=chrome_options)
driver.get('https://www.facebook.com/')


driver.find_element(By.XPATH, "//*[text()='Create New Account']").click()
driver.find_element(By.NAME, "firstname").send_keys("Thang")
driver.find_element(By.NAME, "lastname").send_keys("Ho Huu")
driver.find_element(By.NAME, "reg_email__").send_keys("thangismegmail.com")

d = Select(driver.find_element(By.ID, "day"))
d.select_by_visible_text("5")
m = Select(driver.find_element(By.ID, "month"))
m.select_by_visible_text("5")
y = Select(driver.find_element(By.ID, "year"))
y.select_by_visible_text("2002")

driver.find_element(By.XPATH, "//lable[text() = 'Male']").click()
driver.find_element(By.NAME,"websumit").click()

driver.close()