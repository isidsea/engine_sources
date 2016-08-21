from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "cartalk"
	CRAWLER_NAME = "cartalk crawler"
	LINK_TO_CRAWL = [
		"http://www.cartalk.in/forums/indian-automotive-scene.5/",
		"http://www.cartalk.in/forums/international-automotive-scene.20/",
		"http://www.cartalk.in/forums/reviews.27/",
		"http://www.cartalk.in/forums/emerging-technologies.29/",
		"http://www.cartalk.in/forums/introduce-yourself.3/",
		"http://www.cartalk.in/forums/show-us-your-ride.11/",
		"http://www.cartalk.in/forums/off-topic.25/",
		"http://www.cartalk.in/forums/motor-sports.28/",
		"http://www.cartalk.in/forums/what-car-should-i-buy.22/",
		"http://www.cartalk.in/forums/basic-guides.24/",
		"http://www.cartalk.in/forums/pictures-and-photography.15/",
		"http://www.cartalk.in/forums/videos.9/",
		"http://www.cartalk.in/forums/general-maintenance.14/",
		"http://www.cartalk.in/forums/parts-information.18/",
		"http://www.cartalk.in/forums/diy-zone-the-techincal-era.13/",
		"http://www.cartalk.in/forums/alloy-wheels-tyres.17/",
		"http://www.cartalk.in/forums/feedback.2/"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//ol[@class='discussionListItems']/li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//h3[@class='title']/a[@class='PreviewTooltip']/@href"
	LAST_PAGE_XPATH = "(//div[@class='PageNav']//a)[last()-1]/@href"
	PREV_XPATH = "//div[@class='PageNav']//a[contains(text(),'< Prev')]/@href"
	POST_XPATH = "//ol[@class='messageList']/li"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"concat(.//span[@class='DateTime']/@title,.//abbr[@class='DateTime']/text())"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//a[@class='username']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='messageContent']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[@title='Permalink']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='titleBar']/h1//text()"
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
