#!/usr/bin/env python


import os
os.environ["DISPLAY"]=":0"

from selenium import webdriver
from selenium.webdriver.support import ui

import time
from datetime import datetime
import random
import json
import urllib
import getpass


class BitCrawl:

	def __init__(self, user, password):
		self.browser = webdriver.Firefox()
		self.browser.set_page_load_timeout(30)
		self.user = user
		self.password = password


	def login(self):
		try:
			self.browser.get("https://my.bitcasa.com") 
			self.browser.implicitly_wait(5) # Bitcasa is really slow
			
			user_input = self.browser.find_element_by_xpath('//*[@id="user"]')
			user_input.send_keys(self.user)

			user_input = self.browser.find_element_by_xpath('//*[@id="password"]')
			user_input.send_keys(self.password)

			button = self.browser.find_element_by_xpath('//*[@id="content"]/form/ul/li[5]/button')
			button.click()
		except:
			print "Bitcasa login sucks"
			self.login()

	def get_items(self, url):
		self.browser.get(url)
		pre = self.browser.find_element_by_xpath('/html/body/pre')
		return json.loads(pre.text)['items']

	def get_short_url(self, item):
		name = urllib.quote(item['name'].encode('utf8'))
		path = urllib.quote(item['path'].encode('utf8'))

		share_url = "https://my.bitcasa.com/share?name={0}&selection=%7B%22paths%22%3A%5B%22{1}%22%5D%2C%22albums%22%3A%7B%7D%2C%22artists%22%3A%5B%5D%2C%22photo_albums%22%3A%5B%5D%7D".format(name,path)
		
		self.browser.get(share_url)

		ans_url = b.browser.find_element_by_xpath('/html/body/pre')

		return json.loads(ans_url.text)['short_url']


	def get_size_direct_url(self, short_url):
		self.browser.get(short_url)
		size = b.browser.find_element_by_xpath('//*[@class="file-info"]/p[2]/span').text
		direct_url = b.browser.find_element_by_xpath('//a[contains(@class, "file-action")]').get_attribute('href')
		return size, direct_url


	def getLinks(self, url):


		items = self.get_items(url)
		
		print "<ul>"

		for item in items:
			short_url = self.get_short_url(item)
			size, direct_url = self.get_size_direct_url(short_url)
			print "<li>(<a href='{}'>DL</a>) - <a href='{}'>{}</a> - ({})</li>".format(
				direct_url,
				self.get_short_url(item),
				item['name'].encode('utf8'),
				size)

		print "</ul>"

	def quit(self):
		self.browser.quit()


if __name__ == "__main__":

	print "Bitcasa username:"
	user = raw_input()
	
	pw = getpass.getpass()

	print "URL: (go to https://my.bitcasa.com/, open developer tools > Network > select XHR, get the F** Request URL)"
	print "It looks like https://my.bitcasa.com/directory/41911e413516101d84115e109101dabaee(cbd7de83994beffbcb156f87840168/Pictures/?bottom=500&show-incomplete=true&sort_ascending=true&sort_column=name&top=0"
	url = raw_input()

	b = BitCrawl(user, pw)
	b.login()
	# Todo get xhr url from the path
	b.getLinks(url)
	b.quit()