from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "lancer-exclusive"
	CRAWLER_NAME = "lancer-exclusive crawler"
	LINK_TO_CRAWL = [
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=19",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=20",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=4",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=25",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=7",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=6",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=10",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=9",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=8",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=12",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=23",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=28",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=30",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=34",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=17",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=26",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=22",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=27",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=29",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=59",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=31",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=50",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=51",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=52",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=53",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=54",
		"http://www.lancer-exclusive.com/forums/forumdisplay.php?f=56"
        ]
	COUNTRY = "THA"
	THREAD_XPATH = "//ol[@class='threads']/li[re:test(@class,'thread_*') and not(contains(@class,'moved'))]"
	THREAD_LINK_XPATH = "concat('forums/',.//a[re:test(@id,'thread_title_*')]/@href)"
	LAST_PAGE_XPATH = "concat(substring(concat('forums/',//div[@class='pagination_top']//span[@class='first_last']/a/@href),1 div contains(//div[@class='pagination_top']//span[@class='first_last']/a/@href,'showthread')),substring('',1 div not(contains(//div[@class='pagination_top']//span[@class='first_last']/a/@href,'showthread'))))"
	PREV_XPATH = "concat('forums/',//div[@class='pagination_top']//span[@class='prev_next']/a/@href)"
	POST_XPATH = "//ol[@class='posts']/li[re:test(@id,'post_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//span[re:test(@class,'postdate')]//text()"
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
			"xpath":".//div[re:test(@class,'postrow*')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": "concat('forums/',.//a[@class='postcounter']/@href)"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//span[@class='threadtitle']//text()"
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
