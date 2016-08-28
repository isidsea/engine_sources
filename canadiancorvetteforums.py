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
		"http://www.canadiancorvetteforums.com/forums/news.30/",
		"http://www.canadiancorvetteforums.com/forums/forum-q-a.77/",
		"http://www.canadiancorvetteforums.com/forums/events.84/",
		"http://www.canadiancorvetteforums.com/forums/vettes-on-the-net.83/",
		"http://www.canadiancorvetteforums.com/forums/new-users.24/",
		"http://www.canadiancorvetteforums.com/forums/test-board.15/",
		"http://www.canadiancorvetteforums.com/forums/general-corvette-discussion.3/",
		"http://www.canadiancorvetteforums.com/forums/c1-and-c2.55/",
		"http://www.canadiancorvetteforums.com/forums/c3-forum.56/",
		"http://www.canadiancorvetteforums.com/forums/c4-forum.57/",
		"http://www.canadiancorvetteforums.com/forums/c5-forum.58/",
		"http://www.canadiancorvetteforums.com/forums/c6-forum.59/",
		"http://www.canadiancorvetteforums.com/forums/c7-forum.67/",
		"http://www.canadiancorvetteforums.com/forums/c7-z06.74/",
		"http://www.canadiancorvetteforums.com/forums/corvette-performance.4/",
		"http://www.canadiancorvetteforums.com/forums/cosmetic-enhancements.5/",
		"http://www.canadiancorvetteforums.com/forums/detailing-car-care.65/",
		"http://www.canadiancorvetteforums.com/forums/corvette-tech-questions-diy-guides.31/",
		"http://www.canadiancorvetteforums.com/forums/corvette-pictures-video.34/",
		"http://www.canadiancorvetteforums.com/forums/corvette-track-racing.33/",
		"http://www.canadiancorvetteforums.com/forums/general-vehicle-discussions.7/",
		"http://www.canadiancorvetteforums.com/forums/off-topic.14/",
		"http://www.canadiancorvetteforums.com/forums/dasilva-motorsports.42/",
		"http://www.canadiancorvetteforums.com/forums/gateway-chevrolet-corvette.64/",
		"http://www.canadiancorvetteforums.com/forums/dynaplug-tire-repair-tool.69/",
		"http://www.canadiancorvetteforums.com/forums/phobia-street-innovations.70/",
		"http://www.canadiancorvetteforums.com/forums/corvette-central.61/",
		"http://www.canadiancorvetteforums.com/forums/leggat-chevrolet-buick-gmc.80/",
		"http://www.canadiancorvetteforums.com/forums/vehicles-for-sale-wanted.11/",
		"http://www.canadiancorvetteforums.com/forums/parts-for-sale-wanted.12/",
		"http://www.canadiancorvetteforums.com/forums/general-for-sale-wanted.54/",
		"http://www.canadiancorvetteforums.com/forums/604-250-778.17/",
		"http://www.canadiancorvetteforums.com/forums/403-780.16/",
		"http://www.canadiancorvetteforums.com/forums/306.9/",
		"http://www.canadiancorvetteforums.com/forums/204.18/",
		"http://www.canadiancorvetteforums.com/forums/416-519-905.19/",
		"http://www.canadiancorvetteforums.com/forums/705-613.68/",
		"http://www.canadiancorvetteforums.com/forums/514.20/",
		"http://www.canadiancorvetteforums.com/forums/atlantic-canada.21/",
		"http://www.canadiancorvetteforums.com/forums/saskatoon-corvette-club.86/",
		"http://www.canadiancorvetteforums.com/forums/stoney-creek-corvette-club-sccc.87/",
		"http://www.canadiancorvetteforums.com/forums/general-lifestyle.50/",
		"http://www.canadiancorvetteforums.com/forums/restaurants-food.49/",
		"http://www.canadiancorvetteforums.com/forums/clothing-fashion.48/",
		"http://www.canadiancorvetteforums.com/forums/electronics-gadgets.46/",
		"http://www.canadiancorvetteforums.com/forums/cars.169/",
		"http://www.canadiancorvetteforums.com/forums/trucks.170/",
		"http://www.canadiancorvetteforums.com/forums/cars.174/",
		"http://www.canadiancorvetteforums.com/forums/parts.175/"
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
