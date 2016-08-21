from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "hardwarezone"
	CRAWLER_NAME = "hardwarezone crawler"
	LINK_TO_CRAWL = [
		"http://forums.hardwarezone.com.ph/forumdisplay.php?f=52",
		"http://forums.hardwarezone.com.ph/forumdisplay.php?f=41",
		"http://forums.hardwarezone.com.ph/forumdisplay.php?f=55",
		"http://forums.hardwarezone.com.ph/forumdisplay.php?f=56",
		"http://forums.hardwarezone.com.ph/forumdisplay.php?f=57",
		"http://forums.hardwarezone.com.ph/forumdisplay.php?f=60",
		"http://forums.hardwarezone.com.ph/forumdisplay.php?f=67",
		"http://forums.hardwarezone.com.ph/forumdisplay.php?f=63",
		"http://forums.hardwarezone.com.ph/forumdisplay.php?f=64"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//a[re:test(@id,'thread_title_*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "(//div[@class='pagination']//a[not(contains(text(),'Next'))])[last()]/@href"
	PREV_XPATH = "//div[@class='pagination']//a[contains(text(),'Prev')]/@href"
	POST_XPATH = "//div[@id='posts']//table[re:test(@id,'post*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//a[re:test(@name,'post*')]/following-sibling::text()[1]"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//a[@class='bigusername']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@id,'post_message_*')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[re:test(@id,'postcount*')]/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//h2[@class='header-gray']//text()"
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
