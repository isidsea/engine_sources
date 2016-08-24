from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "exbii"
	CRAWLER_NAME = "exbii crawler"
	LINK_TO_CRAWL = [
			"http://exbii.com/forumdisplay.php?f=4",
			"http://exbii.com/forumdisplay.php?f=10",
			"http://exbii.com/forumdisplay.php?f=50",
			"http://exbii.com/forumdisplay.php?f=53",
			"http://exbii.com/forumdisplay.php?f=32",
			"http://exbii.com/forumdisplay.php?f=29",
			"http://exbii.com/forumdisplay.php?f=56",
			"http://exbii.com/forumdisplay.php?f=37",
			"http://exbii.com/forumdisplay.php?f=45",
			"http://exbii.com/forumdisplay.php?f=7",
			"http://exbii.com/forumdisplay.php?f=69",
			"http://exbii.com/forumdisplay.php?f=11"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//table[@id='threadslist']//td[re:test(@id,'td_threadtitle_*')]"
	THREAD_LINK_XPATH = ".//a[re:test(@id,'thread_title_*')]/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagenav']//td[@class='vbmenu_control'])[last()]//preceding::a[re:test(@title,'Last Page*') or re:test(@title,'Show results*')][1]/@href"
	PREV_XPATH = "//div[@class='pagenav']//a[re:test(@title,'Prev Page*')]/@href"
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
			"xpath":"(//span[@class='navbar'])[last()]/following-sibling::strong/text()"
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
