from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Dropdown(unittest.TestCase):

    def setUp(self):
        # Set up your WebDriver (in this case, Chrome)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://sedekahje.com")
        logger.info("Browser opened and navigated to SedekahJe")
    
    def test_dropdown_is_present(self):
        driver = self.driver
        # Wait for the button to be present
        wait = WebDriverWait(driver, 30)
    
        try:
            # Locate the button by XPath or other selector (you can adjust the locator as needed)
            btn = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[2]/div[1]/div[1]/div/button")))
        
            # Verify the button is displayed
            self.assertTrue(btn.is_displayed(), "Dropdown is not displayed")
        
            # Verify the 'role' attribute
            expected_role = "combobox"
            actual_role = btn.get_attribute("role")
            self.assertEqual(actual_role, expected_role, "Dropdown 'role' attribute is incorrect")
        
            # Verify the SVG element
            svg = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button svg.lucide-chevron-down")))
            
            # Verify SVG attributes
            expected_attributes = {
                "xmlns": "http://www.w3.org/2000/svg",
                "width": "24",
                "height": "24",
                "viewBox": "0 0 24 24",
                "fill": "none",
                "stroke": "currentColor",
                "stroke-width": "2",
                "stroke-linecap": "round",
                "stroke-linejoin": "round"
            }

            for attr, expected_value in expected_attributes.items():
                actual_value = svg.get_attribute(attr)
                self.assertEqual(actual_value, expected_value, f"SVG {attr} is incorrect")

            # Verify SVG class
            svg_class = svg.get_attribute("class")
            self.assertIn("lucide lucide-chevron-down h-4 w-4 opacity-50", svg_class, "SVG class is incorrect")

            # Verify path element within SVG
            path = svg.find_element(By.TAG_NAME, "path")
            path_d = path.get_attribute("d")
            self.assertEqual(path_d, "m6 9 6 6 6-6", "SVG path is incorrect")
        
            # Verify the badge (the text)
            badge_text = btn.find_element(By.XPATH, ".//span[@class='rounded-full px-2 py-1 bg-slate-200 text-black']").text
            expected_badge_text = "Semua Negeri"
            self.assertEqual(badge_text, expected_badge_text, "Dropdown text is incorrect")
            
            logger.info("Button with icon, text, and badge is present and verified")

        except TimeoutException:
            self.fail("Timed out waiting for element to be present")
        except NoSuchElementException as e:
            self.fail(f"Could not find element: {e}")
        except AssertionError as e:
            self.fail(f"Assertion failed: {e}")

    def tearDown(self):
        # Close the browser after the test is done
        self.driver.quit()
        logger.info("Browser closed")

if __name__ == "__main__":
    unittest.main(verbosity=2)