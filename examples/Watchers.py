Import openpyxl
from seleniumbase import BaseCase

los = []
url = 'https://stocktwits.com/symbol/'
workbook = openpyxl.load_workbook('Test.xlsx')
worksheet = workbook.get_sheet_by_name(name = 'Sheet1') 
for col in worksheet['A']:
    los.append(col.value)
los2 = []
print(los)

class MyTestClass(BaseCase):



#for i in los:
  # stocksite = url +i + '?q=' +i 
   
       #driver.get(stocksite) 
       #driver.find_element_by_id('sentiment-tab').click()
       #Bullish = driver.find_elements_by_css_selector('span.bullish:nth-child(1)')
       #Sentiment =  [x.text for x in Bullish]
       #los2.append(Sentiment[0])
       
