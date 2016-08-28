from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "aurorah"
	CRAWLER_NAME = "aurorah crawler"
	LINK_TO_CRAWL = [
		"http://aurorah.proboards.com/board/11/acna-notices-policies",
		"http://aurorah.proboards.com/board/21/forum-features-navigation",
		"http://aurorah.proboards.com/board/7/introductions",
		"http://aurorah.proboards.com/board/5/aurora-general-discussion",
		"http://aurorah.proboards.com/board/10/aurora-showroom",
		"http://aurorah.proboards.com/board/3/automotive-news-reviews",
		"http://aurorah.proboards.com/board/9/water-cooler",
		"http://aurorah.proboards.com/board/4/exterior",
		"http://aurorah.proboards.com/board/6/interior",
		"http://aurorah.proboards.com/board/26/wrecks-body-repairs",
		"http://aurorah.proboards.com/board/23/tires-wheels",
		"http://aurorah.proboards.com/board/19/products-services",
		"http://aurorah.proboards.com/board/2/audio-electric-lighting-95-99",
		"http://aurorah.proboards.com/board/29/audio-electric-lighting-01-03",
		"http://aurorah.proboards.com/board/28/steering-suspension-brakes-95-03",
		"http://aurorah.proboards.com/board/1/classic-aurora-mechanical-maintenance",
		"http://aurorah.proboards.com/board/17/2nd-gen-aurora-mechanical-maintenance",
		"http://aurorah.proboards.com/board/13/aurora-performance",
		"http://aurorah.proboards.com/board/24/aurora-roadtrips",
		"http://aurorah.proboards.com/board/8/acna-meets",
		"http://aurorah.proboards.com/board/20/acna-marketplace",
		"http://aurorah.proboards.com/board/22/test-forum"
        ]
	COUNTRY = "USA"
	THREAD_XPATH = "//span[@class='link target']"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//li[@class='ui-pagination-page ui-pagination-slot'])[last()]/a/@href"
	PREV_XPATH = "//li[@class='ui-pagination-page ui-pagination-prev']/a/@href"
	POST_XPATH = "//table[@class='list']//tr[re:test(@id,'post-*')]"

	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"substring-before(.//span[@class='date']/abbr/text(),'GMT')"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='mini-profile']/a[1]/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='message']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": "substring-after(substring-before(.//a[contains(text(),'Quote')]/@href,'/quote/'),'/')"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='title-bar']//h1/text()"
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
