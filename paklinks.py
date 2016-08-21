from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "paklinks"
	CRAWLER_NAME = "paklinks crawler"
	LINK_TO_CRAWL = [
		"http://www.paklinks.com/gs/humor-rated-g-/",
		"http://www.paklinks.com/gs/gupshup-voice-gallery-/",
		"http://www.paklinks.com/gs/general/",
		"http://www.paklinks.com/gs/travel-and-tourism/",
		"http://www.paklinks.com/gs/business-and-career/",
		"http://www.paklinks.com/gs/showbiz-pakistan/",
		"http://www.paklinks.com/gs/bollywood/",
		"http://www.paklinks.com/gs/world-entertainment/",
		"http://www.paklinks.com/gs/images-central/",
		"http://www.paklinks.com/gs/audio-gallery/",
		"http://www.paklinks.com/gs/video-gallery/",
		"http://www.paklinks.com/gs/cricketnama/",
		"http://www.paklinks.com/gs/other-sports/",
		"http://www.paklinks.com/gs/pakistan-affairs/",
		"http://www.paklinks.com/gs/world-affairs/",
		"http://www.paklinks.com/gs/religion-and-philosophy/",
		"http://www.paklinks.com/gs/poetry/",
		"http://www.paklinks.com/gs/intikhaab/",
		"http://www.paklinks.com/gs/sho-ra-e-gupshup/",
		"http://www.paklinks.com/gs/culture-literature-and-linguistics/",
		"http://www.paklinks.com/gs/history/",
		"http://www.paklinks.com/gs/indo-pak-history/",
		"http://www.paklinks.com/gs/world-history/",
		"http://www.paklinks.com/gs/canvas/",
		"http://www.paklinks.com/gs/gs-book-club/",
		"http://www.paklinks.com/gs/relationships/",
		"http://www.paklinks.com/gs/fashion-and-beauty/",
		"http://www.paklinks.com/gs/wedding/",
		"http://www.paklinks.com/gs/bazaar-talk/",
		"http://www.paklinks.com/gs/classified-ads/",
		"http://www.paklinks.com/gs/health-and-fitness/",
		"http://www.paklinks.com/gs/parenting/",
		"http://www.paklinks.com/gs/household-affairs-and-cuisine-corner/",
		"http://www.paklinks.com/gs/science-and-nature/",
		"http://www.paklinks.com/gs/computer-and-information-technology/",
		"http://www.paklinks.com/gs/gaming/",
		"http://www.paklinks.com/gs/machines-gadgets-and-automotive/",
		"http://www.paklinks.com/gs/gs-site-news-archive/",
		"http://www.paklinks.com/gs/gs-support-archives-resolved/",
		"http://www.paklinks.com/gs/gs-support-help/",
		"http://www.paklinks.com/gs/gs-support-archives-resolved/",
		"http://www.paklinks.com/gs/portal-articles-support/"
        ]
	COUNTRY = "PAK"
	THREAD_XPATH = "//ol[@class='stickies' or @class='threads']//li[re:test(@class,'thread_*')]"
	THREAD_LINK_XPATH = ".//a[re:test(@id,'thread_title_*')]/@href"
	LAST_PAGE_XPATH = "//div[@class='pagination_top']//span[@class='first_last']/a/@href"
	PREV_XPATH = "//div[@class='pagination_top']//span[@class='prev_next']/a/@href"
	POST_XPATH = "//ol[@class='posts']/li[re:test(@id,'post_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//span[@class='date']//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='userinfo']//a/strong/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='content']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[re:test(@name,'post*')]/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='breadcrumb']//li[@class='navbit lastnavbit']/span/text()"
		}}       
	]
	# CONDITIONS={
	# 	"has_to_have_content":{
	# 		"condition":'"content" in document',
	# 		"exception":'"Content is not defined"'
	# 	},
	# 	"content_cannot_be_empty":{
	# 		"condition":'len(document["content"]) > 0',
	# 		"exception":'"Content cannot be empty"'
	# 	}
	# }
#end class
