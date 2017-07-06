from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_basic(self):
        self.open('https://stocktwits.com/symbol/CYTR?q=cytr')            # Navigate to the web page
        self.assert_element('sentiment-tab')       # Assert element on page
        self.click('sentiment-tab')                  # Click element on page
        
