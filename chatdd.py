from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "chatdd"
	CRAWLER_NAME = "chatdd crawler"
	LINK_TO_CRAWL = [
		"http://forum.chatdd.com/forumdisplay.php?f=11",
		"http://forum.chatdd.com/forumdisplay.php?f=31",
		"http://forum.chatdd.com/forumdisplay.php?f=14",
		"http://forum.chatdd.com/forumdisplay.php?f=51",
		"http://forum.chatdd.com/forumdisplay.php?f=95",
		"http://forum.chatdd.com/forumdisplay.php?f=75",
		"http://forum.chatdd.com/forumdisplay.php?f=81",
		"http://forum.chatdd.com/forumdisplay.php?f=78",
		"http://forum.chatdd.com/forumdisplay.php?f=76",
		"http://forum.chatdd.com/forumdisplay.php?f=80",
		"http://forum.chatdd.com/forumdisplay.php?f=77",
		"http://forum.chatdd.com/forumdisplay.php?f=13",
		"http://forum.chatdd.com/forumdisplay.php?f=25",
		"http://forum.chatdd.com/forumdisplay.php?f=49",		
		"http://forum.chatdd.com/forumdisplay.php?f=19",
		"http://forum.chatdd.com/forumdisplay.php?f=22",
		"http://forum.chatdd.com/forumdisplay.php?f=39",
		"http://forum.chatdd.com/forumdisplay.php?f=86",
		"http://forum.chatdd.com/forumdisplay.php?f=92",
		"http://forum.chatdd.com/forumdisplay.php?f=93",
		"http://forum.chatdd.com/forumdisplay.php?f=26",
		"http://forum.chatdd.com/forumdisplay.php?f=29",
		"http://forum.chatdd.com/forumdisplay.php?f=27",
		"http://forum.chatdd.com/forumdisplay.php?f=28",
		"http://forum.chatdd.com/forumdisplay.php?f=36",
		"http://forum.chatdd.com/forumdisplay.php?f=56",
		"http://forum.chatdd.com/forumdisplay.php?f=82",
		"http://forum.chatdd.com/forumdisplay.php?f=97",
		"http://forum.chatdd.com/forumdisplay.php?f=69",
		"http://forum.chatdd.com/forumdisplay.php?f=98",
		"http://forum.chatdd.com/forumdisplay.php?f=100",
		"http://forum.chatdd.com/forumdisplay.php?f=32",
		"http://forum.chatdd.com/forumdisplay.php?f=52",
		"http://forum.chatdd.com/forumdisplay.php?f=30",
		"http://forum.chatdd.com/forumdisplay.php?f=54",
		"http://forum.chatdd.com/forumdisplay.php?f=16",
		"http://forum.chatdd.com/forumdisplay.php?f=91",
		"http://forum.chatdd.com/forumdisplay.php?f=94",
		"http://forum.chatdd.com/forumdisplay.php?f=90",
		"http://forum.chatdd.com/forumdisplay.php?f=88",
		"http://forum.chatdd.com/forumdisplay.php?f=89",
		"http://forum.chatdd.com/forumdisplay.php?f=33",
		"http://forum.chatdd.com/forumdisplay.php?f=84",
		"http://forum.chatdd.com/forumdisplay.php?f=85",
		"http://forum.chatdd.com/forumdisplay.php?f=23",
		"http://forum.chatdd.com/forumdisplay.php?f=45",
		"http://forum.chatdd.com/forumdisplay.php?f=44",
		"http://forum.chatdd.com/forumdisplay.php?f=61",
		"http://forum.chatdd.com/forumdisplay.php?f=41",
		"http://forum.chatdd.com/forumdisplay.php?f=10",
		"http://forum.chatdd.com/forumdisplay.php?f=96"
        ]
	COUNTRY = "PAK"
	THREAD_XPATH = "//ol[@class='stickies' or @class='threads']//li[re:test(@class,'thread_*')]"
	THREAD_LINK_XPATH = ".//a[re:test(@id,'thread_title_*')]/@href"
	LAST_PAGE_XPATH = "//div[@class='pagination_top']//span[@class='first_last']/a/@href"
	PREV_XPATH = "//div[@class='pagination_top']//span[@class='prev_next']/a/@href"
	POST_XPATH = "//ol[@class='posts']/li[re:test(@id,'post_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//span[@class='date']//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='userinfo']//div[@class='username_container']//a/strong//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='content']//text()"
			# "xpath":".//div[re:test(@id,'post_message_*')]/blockquote/div[1]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[re:test(@name,'post*')]/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='breadcrumb']//li[@class='navbit lastnavbit']/span/text()"
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
