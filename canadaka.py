from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "canadaka"
	CRAWLER_NAME = "canadaka crawler"
	LINK_TO_CRAWL = [
		"http://www.canadaka.net/forums/introductions-f15/",
		"http://www.canadaka.net/forums/canadaka-net-f4/",
		"http://www.canadaka.net/forums/announcements-f10/",
		"http://www.canadaka.net/forums/medals-f41/",
		"http://www.canadaka.net/forums/cka-radio-f46/",
		"http://www.canadaka.net/forums/jibber-jabber-f9/",
		"http://www.canadaka.net/forums/rants-raves-f12/",
		"http://www.canadaka.net/forums/canadian-politics-f17/",
		"http://www.canadaka.net/forums/federal-elections-f43/",
		"http://www.canadaka.net/forums/liberal-party-f63/",
		"http://www.canadaka.net/forums/conservative-party-f64/",
		"http://www.canadaka.net/forums/ndp-f65/",
		"http://www.canadaka.net/forums/green-party-f66/",
		"http://www.canadaka.net/forums/bloc-quebecois-f67/",
		"http://www.canadaka.net/forums/canada-us-relations-f14/",
		"http://www.canadaka.net/forums/international-politics-f2/",
		"http://www.canadaka.net/forums/improve-canada-f19/",
		"http://www.canadaka.net/forums/canadian-immigration-f69/",
		"http://www.canadaka.net/forums/filibuster-cartoons-f72/",
		"http://www.canadaka.net/forums/canada-u-s-border-f100/",
		"http://www.canadaka.net/forums/canada-u-s-relations-f101/",
		"http://www.canadaka.net/forums/civil-liberties-and-privacy-f102/",
		"http://www.canadaka.net/forums/democracy-f104/",
		"http://www.canadaka.net/forums/economics-f115/",
		"http://www.canadaka.net/forums/energy-and-resources-f105/",
		"http://www.canadaka.net/forums/environment-f106/",
		"http://www.canadaka.net/forums/foreign-ownership-f107/",
		"http://www.canadaka.net/forums/health-care-and-social-policy-f108/",
		"http://www.canadaka.net/forums/immigration-f109/",
		"http://www.canadaka.net/forums/labour-f110/",
		"http://www.canadaka.net/forums/rural-issues-and-agriculture-f111/",
		"http://www.canadaka.net/forums/trade-agreements-and-nafta-plus-f112/",
		"http://www.canadaka.net/forums/security-defence-military-f114/",
		"http://www.canadaka.net/forums/first-nations-f91/",
		"http://www.canadaka.net/forums/francophonie-hors-quebec-f92/",
		"http://www.canadaka.net/forums/quebec-f93/",
		"http://www.canadaka.net/forums/canadian-politics-f94/",
		"http://www.canadaka.net/forums/canadian-provincial-politics-f97/",
		"http://www.canadaka.net/forums/international-politics-f98/",
		"http://www.canadaka.net/forums/u-s-politics-f99/",
		"http://www.canadaka.net/forums/actions-and-events-f88/",
		"http://www.canadaka.net/forums/your-experiences-f89/",
		"http://www.canadaka.net/forums/suggestions-f90/",
		"http://www.canadaka.net/forums/social-chatter-f82/",
		"http://www.canadaka.net/forums/editorial-discussions-f113/",
		"http://www.canadaka.net/forums/help-and-support-f86/",
		"http://www.canadaka.net/forums/suggestions-f87/",
		"http://www.canadaka.net/forums/canadian-culture-f3/",
		"http://www.canadaka.net/forums/canadian-achievements-f81/",
		"http://www.canadaka.net/forums/current-events-f59/",
		"http://www.canadaka.net/forums/cka-columns-f61/",
		"http://www.canadaka.net/forums/canadian-military-f23/",
		"http://www.canadaka.net/forums/canadian-history-f11/",
		"http://www.canadaka.net/forums/world-history-f44/",
		"http://www.canadaka.net/forums/military-history-f49/",
		"http://www.canadaka.net/forums/discussion-francaise-f20/",
		"http://www.canadaka.net/forums/native-canadian-f48/",
		"http://www.canadaka.net/forums/health-wellness-f42/",
		"http://www.canadaka.net/forums/lifestyles-f79/",
		"http://www.canadaka.net/forums/sports-f8/",
		"http://www.canadaka.net/forums/hockey-f39/",
		"http://www.canadaka.net/forums/football-cfl-f50/",
		"http://www.canadaka.net/forums/canadian-soccer-f56/",
		"http://www.canadaka.net/forums/canadian-rugby-f73/",
		"http://www.canadaka.net/forums/olympics-f57/",
		"http://www.canadaka.net/forums/the-outdoors-f136/",
		"http://www.canadaka.net/forums/entertainment-f7/",
		"http://www.canadaka.net/forums/canadian-music-f6/",
		"http://www.canadaka.net/forums/canucktube-f70/",
		"http://www.canadaka.net/forums/cka-online-games-f71/",
		"http://www.canadaka.net/forums/computer-internet-f5/",
		"http://www.canadaka.net/forums/games-f22/",
		"http://www.canadaka.net/forums/science-f47/",
		"http://www.canadaka.net/forums/business-f29/",
		"http://www.canadaka.net/forums/travel-f38/",
		"http://www.canadaka.net/forums/car-forum-f51/",
		"http://www.canadaka.net/forums/religious-issues-f68/",
		"http://www.canadaka.net/forums/fashion-home-design-f80/",
		"http://www.canadaka.net/forums/food-drink-f55/",
		"http://www.canadaka.net/forums/poems-writings-f21/",
		"http://www.canadaka.net/forums/art-graphics-f53/",
		"http://www.canadaka.net/forums/canadian-humour-f13/",
		"http://www.canadaka.net/forums/canadian-websites-f1/",
		"http://www.canadaka.net/forums/alberta-f31/",
		"http://www.canadaka.net/forums/british-columbia-f30/",
		"http://www.canadaka.net/forums/prairies-f32/",
		"http://www.canadaka.net/forums/ontario-f33/",
		"http://www.canadaka.net/forums/quebec-f34/",
		"http://www.canadaka.net/forums/atlantic-canada-f35/",
		"http://www.canadaka.net/forums/territories-f36/",
		"http://www.canadaka.net/forums/expat-canadians-f45/"
        ]
	COUNTRY = "CAN"
	THREAD_XPATH = "//div[@id='pagecontent']//a[@class='topictitle']"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "(//div[@id='pageheader']/div[2]//a)[last()-1]/@href"
	PREV_XPATH = "//div[@id='pageheader']/div[2]//strong/preceding-sibling::a[1]/@href"
	POST_XPATH = "//div[@class='post_container']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//b[contains(text(),'Posted:')]/following-sibling::text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//b[@class='postauthor']/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='postbody']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//div[@class='grey gensmall']/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@id='pageheader']//h1/a/text()"
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
