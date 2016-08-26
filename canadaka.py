from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "canadaka"
	CRAWLER_NAME = "canadaka crawler"
	LINK_TO_CRAWL = [
				"http://www.canadaka.net/forums/car-forum-f51/",
        ]
	COUNTRY = "CAN"
	THREAD_XPATH = "//div[@id='pagecontent']//a[@class='topictitle']"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "(//div[@id='pageheader']/div[2]//a)[last()-1]/@href"
	PREV_XPATH = "//div[@id='pageheader']/div[2]//strong/preceding-sibling::a[1]/@href"
	POST_XPATH = "//div[@class='post_container']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//b[contains(text(),'Posted:')]/following-sibling::text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//b[@class='postauthor']/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='postbody']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//div[@class='grey gensmall']/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@id='pageheader']//h1/a/text()"
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
