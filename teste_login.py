import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#cria objeto que recebe o driver do chrome
#esse driver tem que ser baixado direto do Google
op = webdriver.ChromeOptions()
op.add_argument('--headless')

browser = webdriver.Chrome(executable_path='/Users/xx/Drivers/chromedriver', options=op)
#instancia objeto para ser capaz de ter acoes no navegador
actions = ActionChains(browser)

try:
    #acessa o site
    browser.get("https://www.autoleitura.com.br")
    #tempo para carregamento
    time.sleep(1)
    #injeta usuario e senha
    username = browser.find_element_by_id("login-email")
    password = browser.find_element_by_id("login-password")
    username.send_keys("X@gmail.com")
    password.send_keys("XXX")
except:
    with open("log.txt", 'w') as file:
        file.write("1")
try:
    #Clique do botao
    wait = WebDriverWait(browser, 5)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.='Entrar']"))).click()
except:
    with open("log.txt", 'w') as file:
        file.write("1")


#tempo para carregar
time.sleep(5)
#acesso aos dados da pagina
DadosEmpresa = browser.find_element_by_xpath("/html/body").text


#condicao para o ALARME
#0 = OK, 1 = NOK


with open("log.txt", 'w') as file:
    if "Você ainda tem"in DadosEmpresa:
        file.write("0")
        print(0)
    else:
        file.write("1")
        print(1)
    time.sleep(5)
    #saida da sessao
    browser.quit()
