from selenium import webdriver
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
        self.assertIn('TO-DO', self.browser.title)
        self.fail('Finish the test!')

        
if __name__ == '__main__':
    unittest.main(warnings='ignore')