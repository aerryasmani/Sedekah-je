import unittest
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Btn_MasjidFilter(unittest.TestCase):
    
    def setUp(self):
        # Set up your WebDriver (in this case, Chrome)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://sedekahje.com")
        logger.info("Browser opened and navigated to SedekahJe")

    def test_click_PopUp(self):
        driver = self.driver
        time.sleep(10)
        try:
            # Wait for the button to be clickable
            popbtn = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="radix-:Rqkq:"]/div[3]/button'))
            )
            popbtn.click()

            logger.info("'Saya Faham' button clicked successfully")

            time.sleep(10)
        except TimeoutException:
            logger.error("'Saya Faham' button not found or not clickable")

        btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/section/div[2]/div[1]/div[1]/div/button"))
        )

        text_to_find = "Semua Negeri"
    
        try:
            # Wait for up to 10 seconds for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/section/div[2]/div[1]/div[1]/div/button/span/span/span"))
            )
            found_text = element.text

            if text_to_find in found_text:
                logger.info(f"Text found on the page: '{text_to_find}'")
            else:
                logger.info(f"Exact text '{text_to_find}' not found, but element contains: '{found_text}'")
        except TimeoutException:
            logger.info(f"The text '{text_to_find}' was not found on the page.")
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")

        # Click Surau Filter
        btn.click()
        logger.info("'Dropdown Filter' button clicked successfully")
        time.sleep(5)
    
        # Verify Dropdown Options
        options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']/li"))
        )

        # Verify the number of options
        self.assertEqual(len(options), 12, "Dropdown should have 12 options")

        # Verify each option is displayed and selectable
        expected_options = ["Semua Negeri", "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", "Pahang", "Perak", "Perlis", "Pulau Pinang", "Selangor", "Terengganu"]
        
        for i, option in enumerate(options):
            self.assertTrue(option.is_displayed(), f"Option {i+1} should be displayed")
            self.assertEqual(option.text, expected_options[i], f"Option {i+1} text should match")
            option.click()
            
            # Wait for the selected option to be reflected in the button text
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, "/html/body/section/div[2]/div[1]/div[1]/div/button/span/span/span"), expected_options[i])
            )
            
            logger.info(f"Option '{expected_options[i]}' selected successfully")
            
            # Reopen the dropdown for the next iteration
            if i < len(options) - 1:
                btn.click()
                time.sleep(1)  # Small delay to ensure dropdown opens
        
    def tearDown(self):
        # Close the browser after the test is done
        self.driver.quit()
        logger.info("Browser closed")

if __name__ == "__main__":
    unittest.main(verbosity=2)