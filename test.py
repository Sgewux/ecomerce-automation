from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest
import time


class Falabella(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../chromedriver')
        self.driver.get('https://www.falabella.com.co/falabella-co/')
        self.driver.maximize_window()
        time.sleep(2)
    

    def test_search_and_filter(self):
        driver = self.driver
        fake_button = driver.find_element_by_xpath('//*[@id="fake-close"]')
        fake_button.click()

        second_fake_button = driver.find_element_by_xpath('//*[@id="acc-alert-deny"]')
        second_fake_button.click()
        
        #We're going to search "Apple Watch"
        search_field = driver.find_element_by_xpath('/html/body/div[1]/nav/div[3]/div/div[1]/div/div[1]/div/input')
        search_field.send_keys('Apple Watch')
        search_field.send_keys(Keys.ENTER)

        #We're going to filter our search results

        #Sorting our search results by higher to lower price
        display_sort_options_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@class="jsx-861649955 tablet-desktop"][2]/div/button')
            ))
        display_sort_options_button.click()
        higher_price_to_lower_button = driver.find_element_by_xpath('//*[@id="testId-Dropdown-Precio de mayor a menor"]')
        higher_price_to_lower_button.click()
        
        #Filtering our results by color in this case black
        filter_by_color_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="testId-Accordion-Color"]')
            ))
        filter_by_color_button.click()

        select_black_button = driver.find_element_by_xpath('//*[@id="testId-multiSelectForColor-Negro"]/label/div')
        select_black_button.click()

        #Filtering by internal storage
        filter_by_internal_storage_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/section[1]/div[4]/div/ul/li[6]/button/i')
            ))
        filter_by_internal_storage_button.click()
        
        thirty_two_gb_button = driver.find_element_by_id('32GB-5')
        thirty_two_gb_button.click()

        #Finally we will print how many elements we found
        time.sleep(2)
        results = driver.find_elements_by_xpath('//div[@id="testId-searchResults-products"][1]/div[@class="jsx-1585533350 search-results-4-grid grid-pod"]')


        print(f'I found {len(results)} elements.')

        driver.save_screenshot('screenshot.png') #Also we are going to save an screenshot


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
