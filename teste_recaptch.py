from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path='/Users/xxx/Drivers/chromedriver')
driver.get("https://servicos.receita.fazenda.gov.br/servicos/cpf/consultasituacao/consultapublica.asp")

cpf = driver.find_element_by_id("txtCPF")
datanasc = driver.find_element_by_id("txtDataNascimento")
time.sleep(1)
cpf.send_keys("22222222222")
time.sleep(2)
datanasc.send_keys("11/11/1111")
time.sleep(2)

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
