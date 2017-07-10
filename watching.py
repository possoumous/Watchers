from pyvirtualdisplay import Display
from selenium import webdriver
import openpyxl

display = Display(visible=0, size=(800, 600))
display.start()

workbook = openpyxl.load_workbook('Test.xlsx')
worksheet = workbook.get_sheet_by_name(name = 'Sheet1')

los = []
url = 'https://stocktwits.com/symbol/'
for col in worksheet['A']:
        los.append(col.value)

print(los)

driver = webdriver.Chrome()

for i in los:
   stocksite = url +i + '?q=' +i 
   print(stocksite)
   driver.get(stocksite) 
   Watchers = driver.find_elements_by_css_selector('a.watchers-top:nth-child(3)').text
   Sentiment =  [x.text for x in Watchers]