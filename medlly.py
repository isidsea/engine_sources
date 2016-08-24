from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "medlly"
	CRAWLER_NAME = "medlly crawler"
	LINK_TO_CRAWL = [
				# "http://medlly.com/discussions",
		"http://medlly.com/categories/delhi-ncr-hospital-review",
		"http://medlly.com/categories/bangalore-hospital-review",
		"http://medlly.com/categories/pune-hospital-review",
		"http://medlly.com/categories/hyderabad-hospital-review",
		"http://medlly.com/categories/kolkata-hospital-review",
		"http://medlly.com/categories/chennai-hospital-review",
		"http://medlly.com/categories/mumbai-hospital-review",
		"http://medlly.com/categories/ahmedabad-hospital-review",
		"http://medlly.com/categories/other-cities",
		"http://medlly.com/categories/weekly-post"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//tr[re:test(@id,'Discussion_*')]"
	THREAD_LINK_XPATH = ".//a[@class='Title']/@href"
	LAST_PAGE_XPATH = "(//span[@id='PagerBefore']//a[@rel='next'])[last()]/preceding-sibling::a[1]/@href"
	PREV_XPATH = "(//span[@id='PagerBefore']//a[@rel='prev'])[1]/@href"
	POST_XPATH = "//div[re:test(@class,'Item-Header*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//time/@title"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//a[@class='Username']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":"./following-sibling::div[1]//div[@class='Message']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[@class='Permalink']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='PageTitle']/h1/text()"
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
