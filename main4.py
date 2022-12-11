# Bài 4


import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(executable_path='/chromedriver', chrome_options=chrome_options)

driver.get('https://lms.ou.edu.vn/')
driver.find_element(By.CLASS_NAME, 'main-btn').click()
driver.find_element(By.CLASS_NAME, 'login100-form-btn').click()

userType = Select(driver.find_element(By.NAME, 'form-usertype'))

# with open('Test.csv', 'w', newline='') as f:
#     fieldName = ['user', 'password']
#     writer = csv.DictWriter(f, fieldnames = fieldName)
#     writer.writeheader()
#     writer.writerow ({'user':'2054050210', 'password':'285821804'})

with open('Test.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        user = row['user']
        password = row['password']

print(user)
print(password)


driver.find_element(By.ID, "form-username").send_keys(user)
driver.find_element(By.ID, "form-password").send_keys(password)
driver.find_element(By.ID, "//lable[text() = 'Đăng nhập']").click()
