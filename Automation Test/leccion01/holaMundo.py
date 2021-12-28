from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver')

driver.get('https://demoqa.com/')
title = driver.title

print('El titulo es: ' + driver.title)
print(f'El titulo es: {title}')


driver.close()
