from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "rimweb"
	CRAWLER_NAME = "rimweb crawler"
	LINK_TO_CRAWL = [
				# "http://www.rimweb.in/forums/forum/21-reliance-mobile-cdma-postpaid/",
		"http://www.rimweb.in/forums/forum/95-reliance-jio-4g-lte-prepaid-postpaid/",
		"http://www.rimweb.in/forums/forum/106-reliance-mobile/",
		"http://www.rimweb.in/forums/forum/4-data-services/",
		"http://www.rimweb.in/forums/forum/108-miscellaneous/",
		"http://www.rimweb.in/forums/forum/10-reliance-communications/",
		"http://www.rimweb.in/forums/forum/48-other-network-cellular-providers/",
		"http://www.rimweb.in/forums/forum/47-other-broadband-discussion/",
		"http://www.rimweb.in/forums/forum/49-indian-telecom-general-news/",
		"http://www.rimweb.in/forums/forum/88-mobile-number-portability-mnp/",
		"http://www.rimweb.in/forums/forum/112-lyf/",
		"http://www.rimweb.in/forums/forum/113-apple/",
		"http://www.rimweb.in/forums/forum/41-htc/",
		"http://www.rimweb.in/forums/forum/6-lg/",
		"http://www.rimweb.in/forums/forum/15-motorola/",
		"http://www.rimweb.in/forums/forum/7-samsung/",
		"http://www.rimweb.in/forums/forum/20-other-handsets/",
		"http://www.rimweb.in/forums/forum/8-nokia/",
		"http://www.rimweb.in/forums/forum/51-blackberry/",
		"http://www.rimweb.in/forums/forum/78-handset-suggestions/",
		"http://www.rimweb.in/forums/forum/14-technical-os-related/",
		"http://www.rimweb.in/forums/forum/74-android/",
		"http://www.rimweb.in/forums/forum/90-ios-apple/",
		"http://www.rimweb.in/forums/forum/39-ringtones-wallpapers-themes-applications-games/",
		"http://www.rimweb.in/forums/forum/40-tutorial-and-guides/",
		"http://www.rimweb.in/forums/forum/38-general-technical-discussion/",
		"http://www.rimweb.in/forums/forum/11-the-longue/",
		"http://www.rimweb.in/forums/forum/12-forum-feedback/"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//div[@class='ipsBox']//li[@itemprop='itemListElement']"
	THREAD_LINK_XPATH = ".//div[@class='ipsDataItem_main']/h4//a[@itemprop='url']/@href"	
	LAST_PAGE_XPATH = "//ul[@class='ipsPagination']/li[@class='ipsPagination_last']/a/@href"
	PREV_XPATH = "//ul[@class='ipsPagination']/li[@class='ipsPagination_prev']/a/@href"
	POST_XPATH = "//article[re:test(@id,'elComment_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//p[@class='ipsType_reset']//time/@title"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//strong[@itemprop='name']/a/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@data-role='commentContent']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[re:test(@id,'elSharePost_*')]/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//h1[@class='ipsType_pageTitle ipsContained_container']//div[@class='ipsType_break ipsContained']/text()"
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
