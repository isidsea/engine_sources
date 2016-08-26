from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "canadiancorvetteforums"
	CRAWLER_NAME = "canadiancorvetteforums crawler"
	LINK_TO_CRAWL = [
				"http://www.canadiancorvetteforums.com/forums/c7-forum.67/",
        ]
	COUNTRY = "CAN"
	THREAD_XPATH = "//ol[@class='discussionListItems']/li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//h3[@class='title']/a[@class='PreviewTooltip']/@href"
	LAST_PAGE_XPATH = "(//span[@class='pageNavHeader']/following-sibling::nav//a)[last()-1]/@href"
	PREV_XPATH = "(//nav//a[@class='currentPage ']//preceding-sibling::a[1])[last()]/@href"
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
			"xpath":"(//span[@class='crumbs']//a[@class='crumb'])[last()]/span/text()"
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
