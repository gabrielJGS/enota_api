# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from models.notaLoja import notaLoja
from models.notaItem import notaItem
import json
def scraper():
    # selenium instantiation
    browser = webdriver.Chrome(
        executable_path=r'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
    browser.get('http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode?p=33220405868574001252653190000597541667304140|2|1|1|fe0ec1aa2fdcc6587380ec410936c618dca7ee03')

    # get info from store
    lojaInfo = browser.find_element(By.CLASS_NAME, 'txtCenter')
    lojaDivs = lojaInfo.find_elements(By.TAG_NAME, 'div')
    loja = notaLoja(lojaDivs[0].text, lojaDivs[1].text, lojaDivs[2].text, [])

    # get items from table
    table = browser.find_element(By.ID, 'tabResult')
    tbody = table.find_element(By.TAG_NAME, 'tbody')
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

