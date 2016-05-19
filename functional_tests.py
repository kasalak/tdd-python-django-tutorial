from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a new online to-do app. She goes to check out its
        # homepage
        browser.get('http://localhost:8000')

        # She notices the page title/header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # She is prompted to enter a to-do item
        # She does other things the author is too tired to currently write about
        # Eventually, after entering in things for her list, she checks the URL later
        # and sees her list still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')
