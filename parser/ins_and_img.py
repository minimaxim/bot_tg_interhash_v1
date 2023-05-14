import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=chrome_options)

url = 'https://whattomine.com/asic'

response = requests.get(url)
page_content = response.content

soup = BeautifulSoup(page_content, 'html.parser')

form = soup.find('form', {'class': 'form-horizontal'})

asic_type_select = form.find('select', {'name': 'algo'})

asic_type_option = asic_type_select.find('option', {'value': 'sha-256'})
asic_type_option['selected'] = True

hashrate_input = form.find('input', {'id': 'hr'})

hashrate_input['value'] = '15000'

submit_button = form.find('button', {'class': 'btn-primary'})
response = driver.execute_script(
    "arguments[0].scrollIntoView(true);arguments[0].click();", submit_button)

driver.implicitly_wait(10)

page_content = driver.page_source

soup = BeautifulSoup(page_content, 'html.parser')

result_table = soup.find('table', {'class': 'table-sm'})

table_image = driver.find_element_by_xpath('//table').screenshot_as_png

with open('table.png', 'wb') as f:
    f.write(table_image)

driver.quit()