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

class Btn_lain(unittest.TestCase):

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
        btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[img[@alt='Lain-lain']]")))
    
        # Verify the button is displayed
        self.assertTrue(btn.is_displayed(), "Button is not displayed")
    
        # Verify the 'data-active' attribute
        expected_data_active = "false"  # Change to "true" if you expect it to be true when active
        actual_data_active = btn.get_attribute("data-active")
        self.assertEqual(actual_data_active, expected_data_active, "Button 'data-active' attribute is incorrect")
    
        # Verify the image source (icon for the Masjid)
        img = btn.find_element(By.TAG_NAME, "img")
        expected_img_src = "/lain/lain-figma.svg"
        actual_img_src = img.get_attribute("src")
        self.assertTrue(expected_img_src in actual_img_src, "Button icon source is incorrect")
    
        # Verify the button text (for different screen sizes)
        button_text = btn.find_element(By.XPATH, ".//span[@class='hidden md:block']").text
        self.assertEqual(button_text, "Lain-lain", "Button text is incorrect")
    
        # Verify the badge (the "87" number)
        badge_text = btn.find_element(By.XPATH, ".//span[@class='rounded-full px-2 py-1 bg-slate-200 text-black']").text
        expected_badge_text = "87"
        self.assertEqual(badge_text, expected_badge_text, "Button badge number is incorrect")
        logger.info("Button with icon, text, and badge is present and verified")

    def tearDown(self):
        # Close the browser after the test is done
        self.driver.quit()
        logger.info("Browser Close")

if __name__ == "__main__":
    unittest.main(verbosity=2)