# 这个脚本是用来抓取页面所有url
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests


seedUrl = ''


class GetPageUrlBy(object):
	"""
	"""
	def __init__():
		pass

	def bySoup(seedUrl):
		"""
		"""
		page = set() #链接去重
		pattern = ""
		html = urlopen(seedUrl)
		bsObj = BeautifulSoup(html)
		for link in bsObj.findAll("a",href=re.compile(pattern)):
			if 'href' in link.attrs:
				if link.attrs['href'] not in pages;
				newPage = link.attrs['href']
				print(newPage)
				page.add(newPage)
				getLinks(newPage)

	def byRe():
		# 获取网页内容
		r = requests.get(seedUrl)
		data = r.text
		pattern = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"

		# 利用正则查找所有连接
		link_list =re.findall( pattern,data)
		for url in link_list:
		    print url








getLinks(seedUrl)
