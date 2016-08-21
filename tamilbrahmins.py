from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "tamilbrahmins"
	CRAWLER_NAME = "tamilbrahmins crawler"
	LINK_TO_CRAWL = [
		"http://www.tamilbrahmins.com/forumdisplay.php?f=96",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=97",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=83",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=41",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=13",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=24",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=69",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=70",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=92",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=93",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=94",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=25",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=76",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=40",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=88",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=89",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=73",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=49",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=51",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=52",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=58",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=59",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=60",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=61",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=50",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=79",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=63",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=85",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=32",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=57",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=74",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=11",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=19",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=36",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=8",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=27",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=2",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=26",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=80",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=10",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=18",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=21",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=54",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=55",
		"http://www.tamilbrahmins.com/forumdisplay.php?f=4"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//ol[@id='threads']//a[re:test(@id,'thread_title_*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "//div[@class='pagination_top']//span[@class='first_last']/a/@href"
	PREV_XPATH = "//div[@class='pagination_top']//span[@class='prev_next']/a/@href"
	POST_XPATH = "//ol[@class='posts']/li[re:test(@id,'post_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"concat(substring-before(substring-after(substring-after(.//span[@class='date']//text(),'-'),'-'),','),'/',	substring-before(substring-after(.//span[@class='date']//text(),'-'),'-'),'/',substring-before(.//span[@class='date']//text(),'-'),' ',substring-after(substring-after(substring-after(.//span[@class='date']//text(),'-'),'-'),','))"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": "concat(.//div[@class='username_container']//a/strong/text(),.//div[@class='username_container']/span[@class='username guest']/text())"
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
			"xpath": ".//a[@class='postcounter']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//span[@class='threadtitle']//text()"
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
