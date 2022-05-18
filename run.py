import os
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager 


# SETUP DOWNLOAD CONFIGS
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
})

# SET CHROME DRIVER
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


# SET PATH TO DRIVER (LINUX)
path_to_file = os.getcwd() + '/assets/login.html'
driver.get('file:///' + path_to_file)

# LOG IN
login = driver.find_element(By.XPATH, '/html/body/div/form/input[1]')
login.send_keys(str(os.getenv("LOGIN")))

password = driver.find_element(By.XPATH, '/html/body/div/form/input[2]')
password.send_keys(str(os.getenv("PASSWORD")))

driver.find_element(By.TAG_NAME, 'button').click()
time.sleep(1)

# IMPORT DATABASE
clients_table = pd.read_excel('assets/NotasEmitir.xlsx')

# LOOP THROUGH ALL CLIENTS (LINE BY LINE >>> .index)
for client in clients_table.index:
    time.sleep(1)

    # FILL UP THE FORM
    name = driver.find_element(By.NAME, 'nome')
    name.send_keys(clients_table.loc[client, 'Cliente'])

    address = driver.find_element(By.NAME, 'endereco')
    address.send_keys(clients_table.loc[client, 'Endereço'])

    district = driver.find_element(By.NAME, 'bairro')
    district.send_keys(clients_table.loc[client, 'Bairro'])

    city = driver.find_element(By.NAME, 'municipio')
    city.send_keys(clients_table.loc[client, 'Municipio'])

    cep = driver.find_element(By.NAME, 'cep')
    cep.send_keys(str(clients_table.loc[client, 'CEP']))

    state = driver.find_element(By.NAME, 'uf')
    state_select = Select(state)
    state_select.select_by_visible_text(clients_table.loc[client, 'UF'])

    cnpj = driver.find_element(By.NAME, 'cnpj')
    cnpj.send_keys(str(clients_table.loc[client, 'CPF/CNPJ']))

    subscription = driver.find_element(By.NAME, 'inscricao')
    subscription.send_keys(str(clients_table.loc[client, 'Inscricao Estadual']))

    desscription = driver.find_element(By.NAME, 'descricao')
    text = clients_table.loc[client, 'Descrição']
    desscription.send_keys(text)

    quantity = driver.find_element(By.NAME, 'quantidade')
    quantity.send_keys(str(clients_table.loc[client, 'Quantidade']))

    value = driver.find_element(By.NAME, 'valor_unitario')
    value.send_keys(str(clients_table.loc[client, 'Valor Unitario']))

    total_value = driver.find_element(By.NAME, 'total')
    total_value_number = float(quantity.get_attribute('value')) * float(value.get_attribute('value'))
    total_value.send_keys(total_value_number)

    driver.find_element(By.CLASS_NAME, 'registerbtn').click()
        
    # REFRESH PAGE TO CLEAR FORM
    driver.refresh()
    
driver.quit()