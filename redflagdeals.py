from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "redflagdeals"
	CRAWLER_NAME = "redflagdeals crawler"
	LINK_TO_CRAWL = [
				"http://forums.redflagdeals.com/automotive-f40/",
        ]
	COUNTRY = "CAN"
	THREAD_XPATH = "//a[@class='topic_title_link']"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "//a[re:test(@class,'pagination_last*')]/@href"
	PREV_XPATH = "//a[@rel='prev']/@href"
	POST_XPATH = "//section[@class='thread_posts']//article"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//span[@class='dateline_timestamp']//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//a[@class='postauthor']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post_content']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": "concat((//input[@class='pagination_input_box']/@data-base-url)[last()],.//a[@class='dateline_permalink']/@href)"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//h1[@class='thread_title']/text()"
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
