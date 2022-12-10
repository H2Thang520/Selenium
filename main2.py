from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path='/chromedriver')
driver.get('https://www.vnexpress.net/')

article =  driver.find_elements(By.CSS_SELECTOR, 'article.item-news')

for ar in article:
    try:
        title = ar.find_element(By.TAG_NAME,'h3').text
        description = ar.find_element(By.TAG_NAME,'p').text
        link = ar.find_element(By.CSS_SELECTOR, 'h3.title-news > a').get_attribute('href')

        print(title)
        print(description)
        print(link)
        print('=================================')
    except:
        print('Loi')

driver.close()