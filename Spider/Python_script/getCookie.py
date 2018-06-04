from selenium import webdriver
import requests


class GetCookieInSelenium():
	def __init__():
		pass

	def inSelenium():
		url = "url to login website"
		path = r"<path to PhantomJS>"
		driver = webdriver.PhantomJS(
			executable_path=path)
		driver.get(url)
		cookie = driver.get_cookies()
		print(cookie)
		driver.close()
		return cookie

class GetCookieInRequests(object):
	"""
	"""
	def __init__(self, arg):
		pass

	def noSession():
		url = ""
		params = {"username":"","password":""}
		reqpost = requests.post(url,params)
		cookie = reqpost.cookies 

	def inSession():
		url = ""
		session = requests.Session()
		params = {"username":"","password":""}
		sepost = session.post(url,params)
		cookie = sepost.cookies

		

