from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "realindianfreebies"
	CRAWLER_NAME = "realindianfreebies crawler"
	LINK_TO_CRAWL = [
		"http://forum.realindianfreebies.in/Forum-Welcome-to-RIF",
		"http://forum.realindianfreebies.in/Forum-Hot-Offers-Deals",
		"http://forum.realindianfreebies.in/Forum-Daily-Deals",
		"http://forum.realindianfreebies.in/Forum-Discount-Coupons",
		"http://forum.realindianfreebies.in/Forum-Indian-Free-Samples-Freebies",
		"http://forum.realindianfreebies.in/Forum-Contests-Winning-Secrets",
		"http://forum.realindianfreebies.in/Forum-Find-a-Deal",
		"http://forum.realindianfreebies.in/Forum-Reviews",
		"http://forum.realindianfreebies.in/Forum-Others"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//a[re:test(@id,'tid_*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "//div[@class='pagination']//a[@class='pagination_next']/preceding-sibling::a[1]/@href"
	PREV_XPATH = "//div[@class='pagination']//a[@class='pagination_previous']/@href"
	POST_XPATH = "//table[re:test(@id,'post_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//td[@class='tcat']/div[1]//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//td[@class='post_author']/strong/span/a//text()"
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
			"xpath": ".//td[@class='tcat']//a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='navigation']/span[@class='active']//text()"
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
