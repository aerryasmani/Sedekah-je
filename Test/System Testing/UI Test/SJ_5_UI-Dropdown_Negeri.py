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

class dropdown(unittest.TestCase):

    def setUp(self):
        # Set up your WebDriver (in this case, Chrome)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://sedekah.je")
        logger.info("Browser opened and navigated to SedekahJe")
    
    def test_dropdown_is_present(self):
        driver = self.driver
        # Wait for the button to be present
        wait = WebDriverWait(driver, 30)
    
        # Locate the button by XPath or other selector (you can adjust the locator as needed)
        btn = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section[1]/div[3]/div[1]/div[1]/div/button")))
    
        # Verify the button is displayed
        self.assertTrue(btn.is_displayed(), "dropdown is not displayed")
    
        # Verify the 'data-active' attribute
        expected_data_active = "combobox"  # Change to "true" if you expect it to be true when active
        actual_data_active = btn.get_attribute("role")
        self.assertEqual(actual_data_active, expected_data_active, "dropdown 'data-active' attribute is incorrect")
    
        # Verify the image source (icon for the Masjid)
        svg = btn.find_element(By.XPATH, "/html/body/section[1]/div[3]/div[1]/div[1]/div/button/svg")  # Look for SVG element within the button
        expected_svg_class = "w-full"  # Update this to match the actual class
        actual_svg_class = svg.get_attribute("class")
        self.assertEqual(expected_svg_class, actual_svg_class, "SVG class is incorrect")
    
        # Verify the badge (the "87" number)
        badge_text = btn.find_element(By.XPATH, "/html/body/section/div[2]/div[1]/div[1]/div/button/span").text
        expected_badge_text = "Semua Negeri"
        self.assertEqual(badge_text, expected_badge_text, "Dropdown text is incorrect")
        logger.info("Button with icon, text, and badge is present and verified")
 
    def tearDown(self):
        # Close the browser after the test is done
        self.driver.quit()
        logger.info("Browser Close")

if __name__ == "__main__":
    unittest.main(verbosity=2)