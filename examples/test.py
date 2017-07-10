from seleniumbase import BaseCase
print "hello"

class MyTestClass(BaseCase):

    def test_basic(self):
        self.open('https://stocktwits.com/symbol/CYTR?q=cytr')            # Navigate to the web page
        self.assert_element('a.watchers-top:nth-child(3)')       # Assert element on page
       # Click on link with the text
        self.assert_text('a.watchers-top:nth-child(3)')
        header_text = self.get_text('a.watchers-top:nth-child(3)')   # Grab text from page element
        print "GOod Bye"
        
