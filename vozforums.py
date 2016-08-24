from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "vozforums"
	CRAWLER_NAME = "vozforums Crawler"
	LINK_TO_CRAWL = [
		"https://vozforums.com/forumdisplay.php?f=2",
		"https://vozforums.com/forumdisplay.php?f=3",
		"https://vozforums.com/forumdisplay.php?f=221",
		"https://vozforums.com/forumdisplay.php?f=26",
		"https://vozforums.com/forumdisplay.php?f=27",
		"https://vozforums.com/forumdisplay.php?f=6",
		"https://vozforums.com/forumdisplay.php?f=25",
		"https://vozforums.com/forumdisplay.php?f=24",
		"https://vozforums.com/forumdisplay.php?f=7",
		"https://vozforums.com/forumdisplay.php?f=8",
		"https://vozforums.com/forumdisplay.php?f=9",
		"https://vozforums.com/forumdisplay.php?f=30",
		"https://vozforums.com/forumdisplay.php?f=13",
		"https://vozforums.com/forumdisplay.php?f=14",
		"https://vozforums.com/forumdisplay.php?f=148",
		"https://vozforums.com/forumdisplay.php?f=15",
		"https://vozforums.com/forumdisplay.php?f=11",
		"https://vozforums.com/forumdisplay.php?f=245",
		"https://vozforums.com/forumdisplay.php?f=12",
		"https://vozforums.com/forumdisplay.php?f=233",
		"https://vozforums.com/forumdisplay.php?f=237",
		"https://vozforums.com/forumdisplay.php?f=241",
		"https://vozforums.com/forumdisplay.php?f=249",
		"https://vozforums.com/forumdisplay.php?f=178",
		"https://vozforums.com/forumdisplay.php?f=47",
		"https://vozforums.com/forumdisplay.php?f=213",
		"https://vozforums.com/forumdisplay.php?f=108",
		"https://vozforums.com/forumdisplay.php?f=112",
		"https://vozforums.com/forumdisplay.php?f=32",
		"https://vozforums.com/forumdisplay.php?f=10",
		"https://vozforums.com/forumdisplay.php?f=31",
		"https://vozforums.com/forumdisplay.php?f=48",
		"https://vozforums.com/forumdisplay.php?f=213",
		"https://vozforums.com/forumdisplay.php?f=222",
		"https://vozforums.com/forumdisplay.php?f=212",
		"https://vozforums.com/forumdisplay.php?f=224",
		"https://vozforums.com/forumdisplay.php?f=170",
		"https://vozforums.com/forumdisplay.php?f=17",
		"https://vozforums.com/forumdisplay.php?f=34",
		"https://vozforums.com/forumdisplay.php?f=145",
		"https://vozforums.com/forumdisplay.php?f=35",
		"https://vozforums.com/forumdisplay.php?f=207",
		"https://vozforums.com/forumdisplay.php?f=18",
		"https://vozforums.com/forumdisplay.php?f=68",
		"https://vozforums.com/forumdisplay.php?f=72",
		"https://vozforums.com/forumdisplay.php?f=76",
		"https://vozforums.com/forumdisplay.php?f=80"
	]
	COUNTRY = "VNM"
	THREAD_XPATH = "//tr//td[re:test(@id,'td_threadtitle_*')]"
	THREAD_LINK_XPATH = ".//a[re:test(@id,'thread_title_*')]/@href"
	LAST_PAGE_XPATH = "//a[re:test(@title,'Last Page*')]/@href"
	PREV_XPATH = "//a[@rel='prev']/@href"
	POST_XPATH = "//table[re:test(@id,'post*')]"
	FIELDS = [
		{"published_date": {
			"single": True, 
			"data_type": "date", 
			"concat": False, 
			"xpath": ".//a[re:test(@name,'post*')]/following-sibling::text()[1]"
			# "xpath":".//tbody//tr[1]//td[@class='thead'][1]/text()[2]"
		}},
		{"permalink": {
			"single": True, 
			"data_type": "url", 
			"concat": False, 
			"xpath": ".//a[re:test(@id,'postcount*')]/@href"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//div[re:test(@id,'postmenu_*')]//a[@class='bigusername']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//td[re:test(@id,'td_post_*')]//text()"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='page']//div[1]//table[@class='tborder']//td[@class='navbar']//strong//text()"
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
