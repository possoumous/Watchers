from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_basic(self):
        self.open('https://stocktwits.com/symbol/CYTR?q=cytr')            # Navigate to the web page
      
    def get_text(self, selector, by=By.CSS_SELECTOR,
                 timeout=settings.SMALL_TIMEOUT):
        if self.timeout_multiplier and timeout == settings.SMALL_TIMEOUT:
            timeout = self._get_new_timeout(timeout)
        self.wait_for_ready_state_complete()
        time.sleep(0.01)
        element = page_actions.wait_for_element_visible(
            self.driver, selector, by, timeout)
        try:
            element_text = element.text
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete()
            time.sleep(0.06)
            element = page_actions.wait_for_element_visible(
                self.driver, selector, by, timeout)
            element_text = element.text
        return element_text
