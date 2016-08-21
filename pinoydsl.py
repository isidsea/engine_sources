from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "pinoydsl"
	CRAWLER_NAME = "pinoydsl crawler"
	LINK_TO_CRAWL = [
		"http://www.pinoydsl.net/forums/pinoydsl-net-news.4/",
		"http://www.pinoydsl.net/forums/dsl-info-tech-news.5/",
		"http://www.pinoydsl.net/forums/suggestions-problems-bugs.6/",
		"http://www.pinoydsl.net/forums/chat-lounge-im-bored.8/",
		"http://www.pinoydsl.net/forums/cdr-king-products.58/",
		"http://www.pinoydsl.net/forums/review-me.18/",
		"http://www.pinoydsl.net/forums/software.10/",
		"http://www.pinoydsl.net/forums/hardware.11/",
		"http://www.pinoydsl.net/forums/games.12/",
		"http://www.pinoydsl.net/forums/pc-modifications.13/",
		"http://www.pinoydsl.net/forums/internet-cafe-business.14/",
		"http://www.pinoydsl.net/forums/technicians-lab.15/",
		"http://www.pinoydsl.net/forums/voice-over-ip-voip.16/",
		"http://www.pinoydsl.net/forums/pfsense-m0n0wall-ipcop-others-pc-based-routers.57/",
		"http://www.pinoydsl.net/forums/captive-portal.59/",
		"http://www.pinoydsl.net/forums/general-topics.26/",
		"http://www.pinoydsl.net/forums/pldt-home-fibr.60/",
		"http://www.pinoydsl.net/forums/pldt-dsl.20/",
		"http://www.pinoydsl.net/forums/bayandsl-skydsl.21/",
		"http://www.pinoydsl.net/forums/globe-dsl.23/",
		"http://www.pinoydsl.net/forums/greendot-dsl-pt-t.22/",
		"http://www.pinoydsl.net/forums/eastern-dsl.24/",
		"http://www.pinoydsl.net/forums/belltel-dsl.25/",
		"http://www.pinoydsl.net/forums/digitel-dsl.27/",
		"http://www.pinoydsl.net/forums/mozcom-dsl.28/",
		"http://www.pinoydsl.net/forums/modem-router-config-settings.29/",
		"http://www.pinoydsl.net/forums/wi-tribe.55/",
		"http://www.pinoydsl.net/forums/now-cable.31/",
		"http://www.pinoydsl.net/forums/zpdee-cable.32/",
		"http://www.pinoydsl.net/forums/destiny-cable.33/",
		"http://www.pinoydsl.net/forums/belltel-icable.34/",
		"http://www.pinoydsl.net/forums/satellite-internet.35/",
		"http://www.pinoydsl.net/forums/dialuppers.36/",
		"http://www.pinoydsl.net/forums/wireless-internet.37/",
		"http://www.pinoydsl.net/forums/bandwidth-speed-meter.39/",
		"http://www.pinoydsl.net/forums/utilities-and-appz.40/",
		"http://www.pinoydsl.net/forums/tips-tricks-and-howto.41/",
		"http://www.pinoydsl.net/forums/p2p-torrents.42/",
		"http://www.pinoydsl.net/forums/it-worx-services.17/",
		"http://www.pinoydsl.net/forums/hire-me.49/",
		"http://www.pinoydsl.net/forums/for-sale-it-related.9/",
		"http://www.pinoydsl.net/forums/misc-sale-non-it-related.53/",
		"http://www.pinoydsl.net/forums/looking-for.52/"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//a[@class='PreviewTooltip']/@href"
	LAST_PAGE_XPATH = "(//div[@class='PageNav']//a[not(contains(text(),'Next >'))])[last()]/@href"
	PREV_XPATH = "//div[@class='PageNav']//a[contains(text(),'< Prev')]/@href"
	POST_XPATH = "//ol[@class='messageList']//li[re:test(@id,'post-*')]"
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
			"xpath": ".//a[@class='username']//text()"
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
			"xpath":"//div[@class='titleBar']//h1/text()"
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
