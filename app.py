from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask
import time


app = Flask(__name__)
@app.route('/CPF/<CPF>')
def ok(CPF):
    url = 'https://pje.app.tjpe.jus.br/1g/ConsultaPublica/listView.seam'
    cpfO = CPF
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    time.sleep(3)
    cpfCorrigido = [cpfO[0], cpfO[1], cpfO[2], cpfO[10], cpfO[3], cpfO[4], cpfO[5], cpfO[9], cpfO[6], cpfO[7], cpfO[8]]
    browser.find_element("xpath",'//*[@id="fPP:dpDec:documentoParte"]').send_keys(cpfCorrigido)
    time.sleep(3)
    Pesquisar = browser.find_element("xpath",'//*[@id="fPP:searchProcessos"]')
    Pesquisar.click()
    time.sleep(10)
    andamento = browser.find_element("xpath", '/html/body/div[5]/div/div/div/div[2]/form/div[2]/div/table/tbody/tr[1]/td[3]').text
    return andamento

