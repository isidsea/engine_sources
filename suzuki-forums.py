from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "suzuki-forums"
	CRAWLER_NAME = "suzuki-forums crawler"
	LINK_TO_CRAWL = [
		"http://www.suzuki-forums.com/suzuki-news/",
		"http://www.suzuki-forums.com/suzuki-polls/",
		"http://www.suzuki-forums.com/forum-rules/",
		"http://www.suzuki-forums.com/new-member-area-introduction/",
		"http://www.suzuki-forums.com/rotm-submissions-voting/",
		"http://www.suzuki-forums.com/rotm-winner/",
		"http://www.suzuki-forums.com/suzuki-aerio-liana-forum/",
		"http://www.suzuki-forums.com/2g-1999-2005-vitara-grand-vitara/",
		"http://www.suzuki-forums.com/3g-2006-2014-vitara-grand-vitara/",
		"http://www.suzuki-forums.com/1g-2001-2006-xl-7/",
		"http://www.suzuki-forums.com/4g-2015-vitara-grand-vitara/",
		"http://www.suzuki-forums.com/2g-2007-xl7/",
		"http://www.suzuki-forums.com/suzuki-esteem-baleno-forum/",
		"http://www.suzuki-forums.com/suzuki-equator/",
		"http://www.suzuki-forums.com/suzuki-forenza-reno-forum/",
		"http://www.suzuki-forums.com/general-forenza-reno-forum/",
		"http://www.suzuki-forums.com/interiors-exteriors/",
		"http://www.suzuki-forums.com/forenza-reno-performance/",
		"http://www.suzuki-forums.com/suspension-brakes-wheels-tires/",
		"http://www.suzuki-forums.com/general-car-audio-video-electronics/",
		"http://www.suzuki-forums.com/image-video-gallery/",
		"http://www.suzuki-forums.com/street-encounters-competition-racing/",
		"http://www.suzuki-forums.com/suzuki-ignis-forum/",
		"http://www.suzuki-forums.com/suzuki-jimny-sierra-samurai-forum/",
		"http://www.suzuki-forums.com/suzuki-kizashi/",
		"http://www.suzuki-forums.com/suzuki-sidekick-escudo-vitara-geo-x/",
		"http://www.suzuki-forums.com/suzuki-swift-geo-metro-forum/",
		"http://www.suzuki-forums.com/2004-swift/",
		"http://www.suzuki-forums.com/suzuki-verona-chevrolet-epica-daewoo-magnus/",
		"http://www.suzuki-forums.com/other-suzuki-models/",
		"http://www.suzuki-forums.com/suzuki-alto-forum/",
		"http://www.suzuki-forums.com/suzuki-cappuccino-forum/",
		"http://www.suzuki-forums.com/suzuki-carry-every-forum/",
		"http://www.suzuki-forums.com/2014-s-cross/",
		"http://www.suzuki-forums.com/suzuki-sx4-forum/",
		"http://www.suzuki-forums.com/suzuki-wagon-r-forum/",
		"http://www.suzuki-forums.com/general-suzuki-non-model-specific-discussion/",
		"http://www.suzuki-forums.com/other-cars/",
		"http://www.suzuki-forums.com/off-topic-lounge/",
		"http://www.suzuki-forums.com/image-video-gallery/",		
		"http://www.suzuki-forums.com/suzuki-forums-autoguide-support-help/",
		"http://www.suzuki-forums.com/general-car-audio-video-electronics/",
		"http://www.suzuki-forums.com/interiors-exteriors/",
		"http://www.suzuki-forums.com/performance/",
		"http://www.suzuki-forums.com/suspension-wheels-tires/",		
		"http://www.suzuki-forums.com/canada/",
		"http://www.suzuki-forums.com/us-north-east/",
		"http://www.suzuki-forums.com/us-central/",
		"http://www.suzuki-forums.com/us-south-west/",
		"http://www.suzuki-forums.com/us-west/",
		"http://www.suzuki-forums.com/us-mid-west/",
		"http://www.suzuki-forums.com/us-south/",
		"http://www.suzuki-forums.com/asia-pacific/",
		"http://www.suzuki-forums.com/australia/",
		"http://www.suzuki-forums.com/philippines/",
		"http://www.suzuki-forums.com/europe/",
		"http://www.suzuki-forums.com/ireland/",
		"http://www.suzuki-forums.com/uk/",
		"http://www.suzuki-forums.com/carid-com/",
		"http://www.suzuki-forums.com/discount-tire/",
		"http://www.suzuki-forums.com/lexani-wheels/",
		"http://www.suzuki-forums.com/classifieds-sale-trade/",
		"http://www.suzuki-forums.com/classifieds-private-wanted/",
		"http://www.suzuki-forums.com/group-buy/",
		"http://www.suzuki-forums.com/good-guy-bad-guy/"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//a[re:test(@id,'thread_title_*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "(//div[@class='pagenav']//td[@class='vbmenu_control'])[last()]//preceding::a[re:test(@title,'Last Page*') or re:test(@title,'Show results*')][1]/@href"
	PREV_XPATH = "//div[@class='pagenav']//a[@rel='prev']/@href"
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
			"xpath":".//td[re:test(@id,'td_post_*')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[contains(text(),'permalink')]/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//td[@class='navbar']/strong/text()"
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
