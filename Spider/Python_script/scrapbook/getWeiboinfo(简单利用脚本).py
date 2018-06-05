import sys
import re
import requests
from datetime import datetime
from datetime import timedelta
from lxml import etree


weibo_contents = []  # 微博内容
publish_times = []
up_nums = []  # 微博对应的点赞数
retweet_nums = []  # 微博对应的转发数
comment_nums = []
pattern = r"\d+\.?\d*"  

def get_weibo_info():
	
	for page in range(1,1103):
		if page < 10:
			pages = '00' + str(page)
		elif page < 100:
			pages = '0' + str(page)
		else:
			pages = str(page)
		url = "http://localhost/haust/5648790156_{}.html".format(pages)
		html = requests.get(url).content
		selector = etree.HTML(html)
		info = selector.xpath("//div[@class='c']")
		if len(info) > 3:
			for i in range(0,len(info) - 2):
				str_t = info[i].xpath("div/span[@class='ctt']")
				weibo_content = str_t[0].xpath("string(.)").encode(sys.stdout.encoding,"ignore").decode(sys.stdout.encoding)
				weibo_contents.append(weibo_content)
				print("weibo content:" + weibo_content)

				str_time = info[i].xpath("div/span[@class='ct']")
				str_time = str_time[0].xpath("string(.)").encode(sys.stdout.encoding,"ignore").decode(sys.stdout.encoding)
				publish_time = str_time.split(u'来自')[0]
				if u"刚刚" in publish_time:
					publish_time = datetime.now().strftime("%Y-%m-%d %H:%M")
				elif u"分钟" in publish_time:
					miniute = publish_time[:publish_time.find(u"分钟")]
					miniute = timedelta(miniute=int(miniute))
					publish_time = (datetime.now()-minute).strftime("%Y-%m-%d %H:%M")
				elif u"今天" in publish_time:
					today = datetime.now().strftime("%Y-%m-%d")
					time = publish_time[3:]
					publish_time = today + "" + time
				elif u"月" in publish_time:
					year = datetime.now().strftime("%Y")
					month = publish_time[0:2]
					day = publish_time[3:5]
					time = publish_time[7:12]
					publish_time = (year + "-" + month + "-" +day + "" + time)
				else:
					publish_time = publish_time[:16]
					publish_times.append(publish_time)
					print(u"publish time:"  + publish_time)
			# 点赞数
			"""
			str_zan = info[i].xpath("div/a/text()")[-4]
			guid = re.findall(pattern, str_zan, re.M)
			if  guid != None:
				up_num = int(guid[0])
				up_nums.append(up_num)
				print(u"点赞数: " + str(up_num))  
			"""
			retweet = info[i].xpath("div/a/text()")[-3]
			guid = re.findall(pattern, retweet, re.M)

			retweet_num = int(guid[0])
			retweet_nums.append(retweet_num)
			print(u"转发数: " + str(retweet_num))
			comment = info[i].xpath("div/a/text()")[-2]
			guid = re.findall(pattern, comment, re.M)

			comment_num = int(guid[0])
			comment_nums.append(comment_num)
			print(u"评论数: " + str(comment_num))





get_weibo_info()