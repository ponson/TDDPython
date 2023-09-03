from selenium import webdriver
from selenium.webdriver.common import keys
import unittest


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
        self.assertIn('To-Do', self.browser.title)
        # header_text = self.browser.find_element_by_tag_name('h1').text
        header_text = self.browser.find_element('name','h1').text
        self.assertIn('TO-DO', header_text)

        # inputbox = self.browser.find_element_by_id('id_newitem')
        inputbox = self.browser.find_element('id', 'id_newitem')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(keys.ENTER)

        # table = self.browser.find_element_by_id('id_list_table')
        table = self.browser.find_element('id', 'id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows))
        self.fail('Finish the test!')

        
if __name__ == '__main__':
    unittest.main(warnings='ignore')