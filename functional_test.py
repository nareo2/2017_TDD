from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	def tearDown(self):
		self.browser.quit()
	def test_can_start_a_list_and_retrive_it_later(self):
		#blah blah blah
		#my game list : darkest dungeon
		self.browser.get('http://localhost:8000')

		#civilization V
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		#dungeon crawl stone soup
		#and so on..
if __name__ == '__main__':
	unittest.main(warnings='ignore')
