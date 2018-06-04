#
# 这个代码为演示代码，记录了从发送url请求，到获取网页源码数据的过程，其中介绍了三个模块的获取方式，其中又以是否含有header区分函数，凸显header的独特作用
# 其中值得注意的是:
#	该过程可总结为url-->response-->bytes-->str
#	函数统一返回html为bytes对象
#

from urllib .request import urlopen
from urllib.request import Request
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
import time



class GetHtmlInUrllib():
	"""获取网页通过urlopen模块
	"""
	def inHearder():
		url = "https://weibo.cn/u/5648790156?page=1"
		req = Request(url) # <class 'urllib.request.Request'>
		# Customize the default User-Agent header value:
		req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0')
		req.add_header('Cookie','_T_WM=7dae7424fb85ebbd7658cad9c57eef81; SUB=_2A253C8d_DeRhGeNJ61oX-CnPyT2IHXVU9-k3rDV6PUJbkdANLVXwkW0oQbTi2Ukr-Nh7rZuSwjgt1SkVPA..; SUHB=04Wu5raxNgcdH-; SCF=AnB1DdJtID-GPJAZnyvTzX6vTyd1YdxKwgKup3pL5mROFu6eHkc6J-KcMt80zqTeC4fCm3G2_UZWFgLc_dxilc8.; SSOLoginState=1510979375')
								 
		response = urlopen(req) # <class 'http.client.HTTPResponse'>
		html = response.read() # <class 'bytes'>
		data = html.decode("utf-8") # <class 'str'>
		print(data)
		return html 


	def noUseragent():
		url = "http://jwc.haust.edu.cn/"
		response = urlopen(url) # <class 'http.client.HTTPResponse'>
		html = response.read() # <class 'bytes'>
		print(html.decode("utf-8"))
		return html

class GetHtmlInRequest():
	"""获取网页通过requests模块
	"""

	
	def inHearder():

		url = "https://weibo.cn/u/5648790156?page=1"
		cookie = {"Cookie": "_T_WM=7dae7424fb85ebbd7658cad9c57eef81; SUB=_2A253C8d_DeRhGeNJ61oX-CnPyT2IHXVU9-k3rDV6PUJbkdANLVXwkW0oQbTi2Ukr-Nh7rZuSwjgt1SkVPA..; SUHB=04Wu5raxNgcdH-; SCF=AnB1DdJtID-GPJAZnyvTzX6vTyd1YdxKwgKup3pL5mROFu6eHkc6J-KcMt80zqTeC4fCm3G2_UZWFgLc_dxilc8.; SSOLoginState=1510979375"}
		
		response = requests.get(url,cookies=cookie) # <class 'requests.models.Response'>
		html = response.content #<class 'bytes'>

		print(html.decode("utf-8"))
		return html 



class GetHtmlInSelenium():
	"""获取网页通过selenium模块+PhantomJS浏览器
		由于智慧校园有安全防护所以初次使用没设置user-agent则会被拦截，见02.png，
		当设置user-agent后则可顺利通过，见01.png，一经设置，则之后访问网页就不在需要设置user-agent，可长期使用
		
	"""

	def noUseragent():
		url = "http://my.haust.edu.cn/rrt-quanzi/topic/search/all"
		username="151416120408" 
		passwd="****"
		path = "/root/Downloads/phantomjs-2.1.1-linux-i686/bin/phantomjs"
		driver = webdriver.PhantomJS(
			executable_path=path
			)
		driver.get(url)
		driver.find_element_by_id("username").send_keys(username)
		driver.find_element_by_id("password").send_keys(passwd)
		driver.find_element_by_id("submit1").click()
		#driver.get_screenshot_as_file('02.png')
		pageSource = driver.page_source # <class 'str'>
		print(type(pageSource))
	def inUseragent():
		url = "http://my.haust.edu.cn/rrt-quanzi/topic/search/all"
		username="151416120408" 
		passwd="****"
		path = "/root/Downloads/phantomjs-2.1.1-linux-i686/bin/phantomjs"
		userAgents = ["Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0"]
		dcap = dict(DesiredCapabilities.PHANTOMJS)
		dcap["phantomjs.page.settings.userAgent"] = (random.choice(userAgents))
		driver = webdriver.PhantomJS(
			executable_path=path,
			desired_capabilities=dcap
			)
		driver.get(url)
		driver.implicitly_wait(10)
		driver.find_element_by_id("username").send_keys(username)
		driver.find_element_by_id("password").send_keys(passwd)
		driver.find_element_by_id("submit1").click()
		#driver.get_screenshot_as_file('01.png')
		pageSource = driver.page_source
		print(type(pageSource))
		
	def weibologin():
		url = "https://weibo.cn/u/5648790156?page=1"
		path = "/root/Downloads/phantomjs-2.1.1-linux-i686/bin/phantomjs"
		dcap = dict(DesiredCapabilities.PHANTOMJS)
		dcap["phantomjs.page.settings.resourceTimeout"] = 1000
		dcap["phantomjs.page.settings.loadImages"] = False
		dcap["phantomjs.page.settings.disk-cache"] = True
		dcap["phantomjs.page.customHeaders.Cookie"] = "_T_WM=7dae7424fb85ebbd7658cad9c57eef81; SUB=_2A253DGkyDeRhGeNJ61oX-CnPyT2IHXVUD3d6rDV6PUJbkdAKLW3ykW0Xn_ri-It9M0bSUcy9UcKY-CE4kw..; SUHB=0C1CZvNG95S0Gw; SCF=AnB1DdJtID-GPJAZnyvTzX6vTyd1YdxKwgKup3pL5mROFu6eHkc6J-KcMt80zqTeC4fCm3G2_UZWFgLc_dxilc8.; SSOLoginState=1510480226"
		driver = webdriver.PhantomJS(
			executable_path=path,
			desired_capabilities=dcap
			)

		driver.get(url)
		driver.implicitly_wait(10)
		driver.get_screenshot_as_file('aa.png')


class scrapy(object):
	"""关于scrapy的response
	"""
	def __init__(self, arg):
		super(scrapy, self).__init__()
		self.arg = arg
		pass

	def response():
		#scrapy shell url
		#response.xpath().xpath()
		pass

		




if __name__ == '__main__':
	#GetHtmlInUrllib.inHearder()
	GetHtmlInUrllib.noUseragent()
	#GetHtmlInRequest.inHearder()
	#GetHtmlInSelenium.noUseragent()
	#GetHtmlInSelenium.inUseragent()
	#GetHtmlInSelenium.weibologin()
	
