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

class TestLogoAndHeader(unittest.TestCase):

    def setUp(self):
        # Set up your WebDriver (in this case, Chrome)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://sedekah.je")
        logger.info("Browser opened and navigated to SedekahJe")
    
    def test_logo_is_present_and_correct(self):
        driver = self.driver
        # Wait for the logo to be present
        wait = WebDriverWait(driver, 10)
        logo = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/header/a/img")))
        
        # Verify the logo is displayed
        self.assertTrue(logo.is_displayed(), "Logo is not displayed")
        
        # Verify the logo src attribute
        expected_src = "https://sedekah.je/masjid.svg"  # Replace with actual logo URL
        self.assertEqual(logo.get_attribute("src"), expected_src, "Logo source is incorrect")
        
        # Verify the logo dimensions (if needed)
        self.assertGreater(logo.size['width'], 0, "Logo width is 0 or negative")
        self.assertGreater(logo.size['height'], 0, "Logo height is 0 or negative")
        logger.info("Logo is present and verified")

    def test_header_text_is_correct(self):
        driver = self.driver
        # Locate the paragprah element by its tag or class
        header = driver.find_element(By.XPATH, '/html/body/header/div/a/h1')  # Replace selector with actual tag
        expected_text = "SedekahJe"  # Replace with the actual header text
        self.assertEqual(header.text, expected_text, "Header text does not match the expected value.")
        logger.info("Header is Present")

    def test_subheader_text_is_correct(self):
        driver = self.driver
        # Locate the header element by its tag or class
        header = driver.find_element(By.XPATH, '/html/body/header/div/p')  # Replace selector with actual tag
        expected_text = "Senarai QR masjid, surau, dan institusi."  # Replace with the actual paragraph text
        self.assertEqual(header.text, expected_text, "subheader text does not match the expected value.")
        logger.info("Subheader is Present")

    def tearDown(self):
        # Close the browser after the test is done
        self.driver.quit()
        logger.info("Browser Close")

if __name__ == "__main__":
    unittest.main(verbosity=2)