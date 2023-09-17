from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time


class NewVisitorTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title, "Browser Title is:%s" % (self.browser.title))
        # header_text = self.browser.find_element_by_tag_name('h1').text
        header_text = self.browser.find_element(By.TAG_NAME,'h1').text
        self.assertIn('To-Do', header_text)

        # inputbox = self.browser.find_element_by_id('id_newitem')
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(5)

        table = self.browser.find_element(By.ID, 'id_list_table')
        print(f"table content: {table}")
        rows = table.find_elements(By.TAG_NAME, 'tr')
        print(f"rows content: {rows}")
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows), "it's text was:\n%s" % (table.text))
        self.fail('Finish the test!')

        
if __name__ == '__main__':
    unittest.main(warnings='ignore')