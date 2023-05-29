from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Iniciando():
    
    def dados_testes():
        
        driver = webdriver.Chrome()
        driver.get("https://web.whatsapp.com/")        
        sleep(20)
        
        return driver
        
                
    
    def entrando_no_whatsapp():
        
        wbDriver = Iniciando.dados_testes()
        
        nome = 'noiva'
        mensagem = 'Bom dia meu amor <3'
        
        contato = wbDriver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
        contato.send_keys(nome)
        sleep(2)
        contato.send_keys(Keys.ENTER)
        sleep(3)
        msn = wbDriver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p') 
        msn.send_keys(mensagem)
        sleep(2)
        msn.send_keys(Keys.ENTER)
        sleep(60)
        
Iniciando.entrando_no_whatsapp()
