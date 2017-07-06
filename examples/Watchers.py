from seleniumbase import BaseCase
import getpass
import json
import logging
import math
import os
import pytest
import sys
import time
import traceback
import unittest
import uuid
from BeautifulSoup import BeautifulSoup
from pyvirtualdisplay import Display
from seleniumbase.config import settings
from seleniumbase.core.application_manager import ApplicationManager
from seleniumbase.core.s3_manager import S3LoggingBucket
from seleniumbase.core.testcase_manager import ExecutionQueryPayload
from seleniumbase.core.testcase_manager import TestcaseDataPayload
from seleniumbase.core.testcase_manager import TestcaseManager
from seleniumbase.core import browser_launcher
from seleniumbase.core import log_helper
from seleniumbase.fixtures import constants
from seleniumbase.fixtures import page_actions
from seleniumbase.fixtures import page_utils
from seleniumbase.fixtures import xpath_to_css
from selenium.common.exceptions import (StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

class MyTestClass(BaseCase):

    def test_basic(self):
        self.open('https://stocktwits.com/symbol/CYTR?q=cytr')            # Navigate to the web page
      
    def get_text(<a class="watchers-top" href="/symbol/CYTR/watchers"> 17,379 Watchers </a>)
                 
