from selenium import webdriver
import unittest

class NewVisitorTests (unittest.TestCase):
    def setup(self):
        self.browser =webdriver.Chrome(r'C:\Users\mnagr\PycharmProjects\TDD-poprawki\drivers\chromedriver.exe')
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Listy',self.browser.title)
        self.fail('Zakończenie testu!')

if __name__=='__main__':
    unittest.main(warnings='ignore')

