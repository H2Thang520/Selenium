from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/chromedriver')
driver.get('https://www.google.com/')

str = input("Nhap vao tu khoa: ")
con = driver.find_element(By.NAME, 'q')
con.send_keys(str)
con.submit()

results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

for r in results:
    text = r.find_element(By.TAG_NAME,'a').text
    link = r.find_element(By.TAG_NAME,'a').get_attribute('href')

    print(text)
    print(link)

driver.close()