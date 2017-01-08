from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	
	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# I want to see homepage!
		self.browser.get('http://localhost:8000')

		#Oh title says 'To-Do'..
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

#Write to-do itme

#Type "Buy peacock feathers" into a text box

#When I hit enter, the page updates, and now the page lists
#"1: Buy peacock feathers" as an item in a to-do list

#There is still a text box inviting me to add another item. I
#enter "Use peacock feathers to make a fly"

#The page updates again, and now shows both iems on my list

#I wonders whether the site will remember my list. Then I sees
#that the site has generated a unique URL for me -- there is some
#explanatory text to that effect.

#I visit that URL - my to-do lists is still there.

#Satisfied, I goes back to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')
