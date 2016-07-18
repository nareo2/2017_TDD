from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	def tearDown(self):
		self.browser.quit()
	def test_can_start_a_list_and_retrive_it_later(self):
		#blah blah blah
		#game list : darkest dungeon
		self.browser.get('http://localhost:8000')

		#civilization V
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		self.assertIn(
			'2: Use peacock feathers to make a fly' ,
			[row.text for row in rows]
    )
	
		self.fail('Finish the test!')

		#dungeon crawl stone soup
		#and so on..
if __name__ == '__main__':
	unittest.main(warnings='ignore')
