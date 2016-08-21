from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "pinstack"
	CRAWLER_NAME = "pinstack crawler"
	LINK_TO_CRAWL = [
		"http://forums.pinstack.com/f61/",
		"http://forums.pinstack.com/f23/",
		"http://forums.pinstack.com/f73/",
		"http://forums.pinstack.com/f74/",
		"http://forums.pinstack.com/f75/",
		"http://forums.pinstack.com/f76/",
		"http://forums.pinstack.com/f77/",
		"http://forums.pinstack.com/f57/",
		"http://forums.pinstack.com/f233/",
		"http://forums.pinstack.com/f10/",
		"http://forums.pinstack.com/f30/",
		"http://forums.pinstack.com/f54/",
		"http://forums.pinstack.com/f297/",
		"http://forums.pinstack.com/f25/",
		"http://forums.pinstack.com/f3/",
		"http://forums.pinstack.com/f59/",
		"http://forums.pinstack.com/f28/",
		"http://forums.pinstack.com/f55/",
		"http://forums.pinstack.com/f112/",
		"http://forums.pinstack.com/f60/",
		"http://forums.pinstack.com/f235/",
		"http://forums.pinstack.com/f256/",
		"http://forums.pinstack.com/f254/",
		"http://forums.pinstack.com/f214/",
		"http://forums.pinstack.com/f238/",
		"http://forums.pinstack.com/f344/",
		"http://forums.pinstack.com/f234/",
		"http://forums.pinstack.com/f255/",
		"http://forums.pinstack.com/f216/",
		"http://forums.pinstack.com/f236/",
		"http://forums.pinstack.com/f257/",
		"http://forums.pinstack.com/f351/",
		"http://forums.pinstack.com/f353/",
		"http://forums.pinstack.com/f261/",
		"http://forums.pinstack.com/f316/",
		"http://forums.pinstack.com/f318/",
		"http://forums.pinstack.com/f319/",
		"http://forums.pinstack.com/f355/",
		"http://forums.pinstack.com/f93/",
		"http://forums.pinstack.com/f24/",
		"http://forums.pinstack.com/f219/",
		"http://forums.pinstack.com/f258/",
		"http://forums.pinstack.com/f259/",
		"http://forums.pinstack.com/f210/",
		"http://forums.pinstack.com/f221/",
		"http://forums.pinstack.com/f232/",
		"http://forums.pinstack.com/f52/",
		"http://forums.pinstack.com/f228/",
		"http://forums.pinstack.com/f227/",
		"http://forums.pinstack.com/f229/",
		"http://forums.pinstack.com/f245/",
		"http://forums.pinstack.com/f230/",
		"http://forums.pinstack.com/f246/"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//div[@id='threadlist']//a[@class='title']"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "//div[@class='pagination_top']//span[@class='first_last']/a/@href"
	PREV_XPATH = "//div[@class='pagination_top']//span[@class='prev_next']/a/@href"
	POST_XPATH = "//ol[@class='posts']/li[re:test(@id,'post_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			# "xpath":"substring-before(.//span[@class='date']//text(),'GMT')"
			"xpath":".//span[@class='date']//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='userinfo']//a/strong//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@class,'postrow*')]/div[re:test(@class,'content*')]//text()"
			# "xpath":".//div[re:test(@class,'postrow*')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[@class='postcounter']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@id='breadcrumb']//li[@class='navbit lastnavbit']//text()"
		}}       
	]
	CONDITIONS={
		"has_to_have_content":{
			"condition":'"content" in document',
			"exception":'"Content is not defined"'
		},
		"content_cannot_be_empty":{
			"condition":'len(document["content"]) > 0',
			"exception":'"Content cannot be empty"'
		}
	}
#end class
