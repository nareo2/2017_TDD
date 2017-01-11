from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	
	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# I want to see homepage!
		self.browser.get(self.live_server_url)

		#Oh title says 'To-Do'..
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#Write to-do itme
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		#Type "Buy peacock feathers" into a text box
		inputbox.send_keys('Buy peacock feathers')

		#When I hit enter, the page updates, and now the page lists
		#"1: Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

		#There is still a text box inviting me to add another item. I
		#enter "Use peacock feathers to make a fly"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		#The page updates again, and now shows both iems on my list
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		self.assertIn(
			'2: Use peacock feathers to make a fly' ,
			[row.text for row in rows]
		)

		#I wonders whether the site will remember my list. Then I sees
		#that the site has generated a unique URL for me -- there is some
		#explanatory text to that effect.

		self.fail('Finish the test!')
#I visit that URL - my to-do lists is still there.

#Satisfied, I goes back to sleep
