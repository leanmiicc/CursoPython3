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

fullName = driver.find_element_by_xpath("//input[@id='userName']").send_keys('Hola como estas?')

time.sleep(2)
driver.close()
