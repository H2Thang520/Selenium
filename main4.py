# Bài 5


import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path='/chromedriver')
#driver = webdriver.Chrome(executable_path='/chromedriver', chrome_options=chrome_options)

# with open('Test.csv', 'w', newline='') as f:
#     fieldName = ['user', 'password']
#     writer = csv.DictWriter(f, fieldnames = fieldName)
#     writer.writeheader()
#     writer.writerow ({'user':'2054050210', 'password':'285821804'})
# print(user)
# print(password)

with open('Test.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        user = row['user']
        password = row['password']

driver.get('https://lms.ou.edu.vn/')
driver.find_element(By.CLASS_NAME, 'main-btn').click()
driver.find_element(By.CLASS_NAME, 'login100-form-btn').click()
userType = Select(driver.find_element(By.NAME, 'form-usertype'))
userType.select_by_index(0)
driver.find_element(By.NAME, "form-username").send_keys(user)
driver.find_element(By.NAME, "form-password").send_keys(password)
driver.find_element(By.CLASS_NAME, 'col-xs-12').click()
driver.implicitly_wait(5)
cources = driver.find_elements(By.CSS_SELECTOR, '.dashboard-card .course-info-container .align-items-start a')
cources = driver.find_elements(By.CLASS_NAME, 'multiline')
for c in cources:
    print(c.text)

driver.quit()
