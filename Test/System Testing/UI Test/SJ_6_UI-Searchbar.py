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

class searchbar(unittest.TestCase):

    def setUp(self):
        # Set up your WebDriver (in this case, Chrome)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://sedekah.je")
        logger.info("Browser opened and navigated to SedekahJe")
    
    def test_searchbar_is_present(self):
        driver = self.driver
        # Wait for the button to be present
        wait = WebDriverWait(driver, 30)
    
        # Locate the button by XPath or other selector (you can adjust the locator as needed)
        searchbar = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[2]/div[1]/div[2]/div/div/input")))
    
        # Verify the button is displayed
        self.assertTrue(searchbar.is_displayed(), "Searchbar is not displayed")
    
        # Verify the 'data-active' attribute
        expected_data_active = "search"  # Change to "true" if you expect it to be true when active
        actual_data_active = searchbar.get_attribute("type")
        self.assertEqual(actual_data_active, expected_data_active, "Searchbar attribute is incorrect")
    
        # Wait until the search bar is present and visible
        searchbar = WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Cari masjid/ surau/ institusi...']")))

        # Verify the image source (icon for the Masjid)
        svg = searchbar.find_element(By.XPATH, "/html/body/section/div[2]/div[1]/div[2]/div/div/div")  # Look for SVG element within the button
        expected_svg_class = "absolute left-1.5 top-1/2 transform -translate-y-1/2"  # Update this to match the actual class
        actual_svg_class = svg.get_attribute("class")
        self.assertEqual(expected_svg_class, actual_svg_class, "SVG class is incorrect")

        # Verify the badge (the "87" number)
        # Verify the badge (the "Cari masjid/ surau/ institusi..." placeholder)
        searchbar = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Cari masjid/ surau/ institusi...']")
        badge_text = searchbar.get_attribute("placeholder")
        expected_badge_text = "Cari masjid/ surau/ institusi..."
        self.assertEqual(badge_text, expected_badge_text, "Searchbar placeholder text is incorrect")
        logger.info("Searchbar with icon and placeholder text is present and verified")


    def tearDown(self):
        # Close the browser after the test is done
        self.driver.quit()
        logger.info("Browser Close")

if __name__ == "__main__":
    unittest.main(verbosity=2)