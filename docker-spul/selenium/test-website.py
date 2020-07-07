import unittest, logging, os, datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class WebsiteTest(unittest.TestCase):
    def setUp(self):
        format = "%Y%m%d%H%M"
        date = datetime.datetime.now()
        logging.basicConfig(level=logging.INFO, filename = 'c:\\Logging\\test-website-'+date.strftime(format)+'.log')
        logging.info("Setting up Driver")
        WAIT = 30
        os.environ['MOZ_HEADLESS'] = '1'
        binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
        #binary = FirefoxBinary('/usr/local/firefox/firefox')
        self.driver = webdriver.Firefox(firefox_binary=binary)
        
        logging.info("Setting Driver Settings")
        self.driver.implicitly_wait(WAIT)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, WAIT)

    def test_PoC(self):
        logging.info("Starting PoC")
        driver, wait = self.driver, self.wait
        logging.info("Going to Test website")
        link = "http://127.0.0.1:80"
        driver.get(link)
        
        elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p')))
        if str(elem.text) != "Dit is een simpele statische website.":
            logging.error("De tekst op de website komt niet overeen met de verwachte tekst")
            raise Exception('De tekst op de website komt niet overeen met de verwachte tekst')
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()