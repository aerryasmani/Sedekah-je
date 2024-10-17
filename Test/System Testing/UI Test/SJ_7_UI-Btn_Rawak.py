from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Btn_Rawak(unittest.TestCase):

    def setUp(self):
        # Set up your WebDriver (in this case, Chrome)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://sedekahje.com")
        logger.info("Browser opened and navigated to SedekahJe")
    
    def test_btn_is_present(self):
        driver = self.driver
        # Wait for the button to be present
        wait = WebDriverWait(driver, 30)
    
        # Locate the button by XPath or other selector (you can adjust the locator as needed)
        btn = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/footer/a[1]/button")))
    
        # Verify the button is displayed
        self.assertTrue(btn.is_displayed(), "Button is not displayed")
    
        # Verify the button text (for different screen sizes)
        button_text = btn.find_element(By.CSS_SELECTOR, "body > section > footer > a:nth-child(1) > button > p").text
        self.assertEqual(button_text, "Sedekah Rawak", "Button text is incorrect")
        logger.info("Button is present and visible")

    def tearDown(self):
        # Close the browser after the test is done
        self.driver.quit()
        logger.info("Browser Close")

if __name__ == "__main__":
    unittest.main(verbosity=2)