from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "stockmarketpilipinas"
	CRAWLER_NAME = "stockmarketpilipinas crawler"
	LINK_TO_CRAWL = [
		"http://www.stockmarketpilipinas.com/forum-4.html",
		"http://www.stockmarketpilipinas.com/forum-2.html",
		"http://www.stockmarketpilipinas.com/forum-23.html",
		"http://www.stockmarketpilipinas.com/forum-10.html",
		"http://www.stockmarketpilipinas.com/forum-12.html",
		"http://www.stockmarketpilipinas.com/forum-13.html",
		"http://www.stockmarketpilipinas.com/forum-21.html",
		"http://www.stockmarketpilipinas.com/forum-22.html"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//a[re:test(@id,'tid_*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "//div[@class='pagination']//a[@class='pagination_last']/@href"
	PREV_XPATH = "//div[@class='pagination']//a[@class='pagination_previous']/@href"
	POST_XPATH = "//div[@id='posts']//table[re:test(@id,'post_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//td[@class='tcat']/div[1]/text()[1]"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//td[@class='post_author']//a//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//td[@class='trow2 post_content ']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//td[@class='tcat']//strong/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='navigation']//span[@class='active']/text()"
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
