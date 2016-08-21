from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "pinoyloveforum"
	CRAWLER_NAME = "pinoyloveforum crawler"
	LINK_TO_CRAWL = [
		"http://www.pinoyloveforum.com/index.php?board=1.0",
		"http://www.pinoyloveforum.com/index.php?board=2.0",
		"http://www.pinoyloveforum.com/index.php?board=20.0",
		"http://www.pinoyloveforum.com/index.php?board=22.0",
		"http://www.pinoyloveforum.com/index.php?board=46.0",
		"http://www.pinoyloveforum.com/index.php?board=47.0",
		"http://www.pinoyloveforum.com/index.php?board=48.0",
		"http://www.pinoyloveforum.com/index.php?board=49.0",
		"http://www.pinoyloveforum.com/index.php?board=42.0",
		"http://www.pinoyloveforum.com/index.php?board=44.0",
		"http://www.pinoyloveforum.com/index.php?board=43.0",
		"http://www.pinoyloveforum.com/index.php?board=11.0",
		"http://www.pinoyloveforum.com/index.php?board=12.0",
		"http://www.pinoyloveforum.com/index.php?board=41.0",
		"http://www.pinoyloveforum.com/index.php?board=45.",
		"http://www.pinoyloveforum.com/index.php?board=13.0",
		"http://www.pinoyloveforum.com/index.php?board=26.0",
		"http://www.pinoyloveforum.com/index.php?board=27.",
		"http://www.pinoyloveforum.com/index.php?board=25.0",
		"http://www.pinoyloveforum.com/index.php?board=8.0",
		"http://www.pinoyloveforum.com/index.php?board=40.0",
		"http://www.pinoyloveforum.com/index.php?board=9.0",
		"http://www.pinoyloveforum.com/index.php?board=6.0",
		"http://www.pinoyloveforum.com/index.php?board=37.0",
		"http://www.pinoyloveforum.com/index.php?board=10.0",
		"http://www.pinoyloveforum.com/index.php?board=24.0",
		"http://www.pinoyloveforum.com/index.php?board=56.0",
		"http://www.pinoyloveforum.com/index.php?board=57.",
		"http://www.pinoyloveforum.com/index.php?board=7.0",
		"http://www.pinoyloveforum.com/index.php?board=5.0",
		"http://www.pinoyloveforum.com/index.php?board=15.0",
		"http://www.pinoyloveforum.com/index.php?board=28.0",
		"http://www.pinoyloveforum.com/index.php?board=55.0",
		"http://www.pinoyloveforum.com/index.php?board=3.0",
		"http://www.pinoyloveforum.com/index.php?board=4.0",
		"http://www.pinoyloveforum.com/index.php?board=39.0",
		"http://www.pinoyloveforum.com/index.php?board=38.0",
		"http://www.pinoyloveforum.com/index.php?board=50.0",
		"http://www.pinoyloveforum.com/index.php?board=23.0",
		"http://www.pinoyloveforum.com/index.php?board=51.0",
		"http://www.pinoyloveforum.com/index.php?board=54.0",
		"http://www.pinoyloveforum.com/index.php?board=52.0",
		"http://www.pinoyloveforum.com/index.php?board=16.0",
		"http://www.pinoyloveforum.com/index.php?board=58.0",
		"http://www.pinoyloveforum.com/index.php?board=29.0",
		"http://www.pinoyloveforum.com/index.php?board=59.0",
		"http://www.pinoyloveforum.com/index.php?board=31.0",
		"http://www.pinoyloveforum.com/index.php?board=19.0",
		"http://www.pinoyloveforum.com/index.php?board=32.0",
		"http://www.pinoyloveforum.com/index.php?board=21.0",
		"http://www.pinoyloveforum.com/index.php?board=18.0",
		"http://www.pinoyloveforum.com/index.php?board=17.0",
		"http://www.pinoyloveforum.com/index.php?board=34.0"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = ".//a/@href"
	LAST_PAGE_XPATH = "(//a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "//div[@class='nav']/a[contains(text(),'previous')]/@href"
	POST_XPATH = "//form[@id='quickModForm']//td[@class='windowbg' or @class='windowbg2']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//div[re:test(@id,'subject_*')]/following-sibling::div[1]/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//tr/td[@width='16%']/b//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post']//text()"
			# "xpath":".//div[@class='post']/span//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//div[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//div[@class='nav']//a[@class='nav'])[last()]//text()"
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
