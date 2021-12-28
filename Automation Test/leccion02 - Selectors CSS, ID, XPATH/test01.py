import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver')

driver.get('https://demoqa.com/text-box')

# Maximizar ventana:
driver.maximize_window()

# Tiempo de espera con el sleep - le pase por parametros el tiempo en segundos:

# Seleccion de Campos por Xpath:
# Defino una variable para asignarle el xpaht que quiero:

fullName = driver.find_element_by_xpath("//input[@id='userName']")
fullName.send_keys('Hola, como estas?')

driver.find_element_by_xpath("//input[@id='userEmail']").send_keys('leandro.micciche@gmail.com')

time.sleep(2)
driver.close()