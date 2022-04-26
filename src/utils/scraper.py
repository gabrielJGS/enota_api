# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from ..models.notaLoja import notaLoja
from ..models.notaItem import notaItem
import json
import os

def scraper(notaUrl):
    if(notaUrl.find("http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode") < 0):
        return {"message": "É necessário informar uma url válida para consultaNFCe"}
    try:
        # selenium instantiation
        #browser = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

        browser.get(notaUrl)

        # get info from store
        lojaInfo = browser.find_element(By.CLASS_NAME, 'txtCenter')
        lojaDivs = lojaInfo.find_elements(By.TAG_NAME, 'div')
        loja = notaLoja(lojaDivs[0].text,
                        lojaDivs[1].text, lojaDivs[2].text, [])

        # get items from table
        table = browser.find_element(By.ID, 'tabResult')
        items = []
        for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
            # get first td whereas contain obj data
            row = row.find_elements(By.TAG_NAME, 'td')[0]
            # get object data
            nome = row.find_element(By.CLASS_NAME, 'txtTit').text
            cod = row.find_element(By.CLASS_NAME, 'RCod').text
            qtd = row.find_element(By.CLASS_NAME, 'Rqtd').text
            unTipo = row.find_element(By.CLASS_NAME, 'RUN').text
            vlUnit = row.find_element(By.CLASS_NAME, 'RvlUnit').text
            # instantiate class obj, format and append to array
            obj = notaItem(nome, cod, qtd, unTipo, vlUnit)
            obj.format_items()
            items.append(obj)
        # end of for
        loja.items = items
        browser.quit()
        return(json.dumps(loja, default=vars))
    except:
        nomeErro = browser.find_element(By.CLASS_NAME, 'avisoErro').text
        browser.quit()
        return {"message": "Ocorreu um erro: "+nomeErro}
