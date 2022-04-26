from selenium import webdriver
from selenium.webdriver.common.by import By
from src.models.itemClass import itemClass
browser = webdriver.Chrome(
    executable_path=r'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
browser.get('http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode?p=33220405868574001252653190000597541667304140|2|1|1|fe0ec1aa2fdcc6587380ec410936c618dca7ee03')
# search_box = driver.find_element(By.ID, "tabResult")
table = browser.find_element(By.ID, 'tabResult')
tbody = table.find_element(By.TAG_NAME, 'tbody')
items = []
for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
    obj = itemClass()
    row = row.find_elements(By.TAG_NAME, 'td')
    row = row[0]
    print(row.text)
    obj.txtTit = row.find_element(By.CLASS_NAME, 'txtTit').text
    obj.RCod = row.find_element(By.CLASS_NAME, 'RCod').text
    obj.Rqtd = row.find_element(By.CLASS_NAME, 'Rqtd').text
    obj.RUN = row.find_element(By.CLASS_NAME, 'RUN').text
    obj.RvlUnit = row.find_element(By.CLASS_NAME, 'RvlUnit').text
    items.append(obj)
print(items[0])
browser.quit()
