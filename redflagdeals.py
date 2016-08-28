from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "redflagdeals"
	CRAWLER_NAME = "redflagdeals crawler"
	LINK_TO_CRAWL = [
		"http://forums.redflagdeals.com/hot-deals-f9/",
		"http://forums.redflagdeals.com/ongoing-deal-discussion-f129/",
		"http://forums.redflagdeals.com/shopping-discussion-f74/",
		"http://forums.redflagdeals.com/coupons-f136/",
		"http://forums.redflagdeals.com/freebies-f12/",
		"http://forums.redflagdeals.com/contests-f34/",
		"http://forums.redflagdeals.com/request-deal-f10/",
		"http://forums.redflagdeals.com/group-deals-f124/",
		"http://forums.redflagdeals.com/group-deal-discussion-f130/",
		"http://forums.redflagdeals.com/expired-offers-f110/",
		"http://forums.redflagdeals.com/expired-hot-deals-f68/",
		"http://forums.redflagdeals.com/target-clearance-deals-f157/",
		"http://forums.redflagdeals.com/expired-contests-f105/",
		"http://forums.redflagdeals.com/expired-coupons-f139/",
		"http://forums.redflagdeals.com/expired-freebies-f104/",
		"http://forums.redflagdeals.com/expired-group-deals-f125/",
		"http://forums.redflagdeals.com/buy-sell-trading-post-f44/",
		"http://forums.redflagdeals.com/bst-apparel-f76/",
		"http://forums.redflagdeals.com/bst-automotive-accessories-f59/",
		"http://forums.redflagdeals.com/bst-cameras-accessories-f131/",
		"http://forums.redflagdeals.com/bst-cell-phones-accessories-f45/",
		"http://forums.redflagdeals.com/bst-computer-hardware-tablets-software-accessories-f11/",
		"http://forums.redflagdeals.com/bst-electronics-f52/",
		"http://forums.redflagdeals.com/bst-gift-cards-f57/",
		"http://forums.redflagdeals.com/bst-textbooks-f49/",
		"http://forums.redflagdeals.com/bst-tickets-f106/",
		"http://forums.redflagdeals.com/bst-video-games-music-movies-f46/",
		"http://forums.redflagdeals.com/bst-everything-else-f25/",
		"http://forums.redflagdeals.com/free-stuff-f99/",
		"http://forums.redflagdeals.com/group-buys-f121/",
		"http://forums.redflagdeals.com/scammers-warnings-f77/",
		"http://forums.redflagdeals.com/archived-bst-posts-f115/",
		"http://forums.redflagdeals.com/welcome-redflagdeals-com-forum-f79/",
		"http://forums.redflagdeals.com/site-comments-suggestions-f13/",
		"http://forums.redflagdeals.com/art-photography-f89/",
		"http://forums.redflagdeals.com/automotive-f40/",
		"http://forums.redflagdeals.com/careers-f58/",
		"http://forums.redflagdeals.com/computers-electronics-f14/",
		"http://forums.redflagdeals.com/cell-phones-f88/",
		"http://forums.redflagdeals.com/entertainment-f17/",
		"http://forums.redflagdeals.com/pc-video-games-f69/",
		"http://forums.redflagdeals.com/entrepreneurship-small-business-f62/",
		"http://forums.redflagdeals.com/fashion-apparel-f67/",
		"http://forums.redflagdeals.com/beauty-wellness-f128/",
		"http://forums.redflagdeals.com/food-drink-f18/",
		"http://forums.redflagdeals.com/home-garden-f53/",
		"http://forums.redflagdeals.com/green-eco-friendly-f90/",
		"http://forums.redflagdeals.com/real-estate-f169/",
		"http://forums.redflagdeals.com/parenting-f78/",
		"http://forums.redflagdeals.com/personal-finance-f41/",
		"http://forums.redflagdeals.com/investing-f134/",
		"http://forums.redflagdeals.com/real-estate-f169/",
		"http://forums.redflagdeals.com/pets-f120/",
		"http://forums.redflagdeals.com/students-f84/",
		"http://forums.redflagdeals.com/sports-recreation-f26/",
		"http://forums.redflagdeals.com/fitness-nutrition-f142/",
		"http://forums.redflagdeals.com/travel-f39/",
		"http://forums.redflagdeals.com/off-topic-f15/",
		"http://forums.redflagdeals.com/off-topic-archive-f133/",
		"http://forums.redflagdeals.com/past-promotions-archives-f23/",
		"http://forums.redflagdeals.com/rfd-3rd-anniversary-create-win-500-wish-list-f22/",
		"http://forums.redflagdeals.com/rfd-4th-anniversary-create-win-400-wish-list-f35/",
		"http://forums.redflagdeals.com/ncix-boxing-week-2006-wish-list-contest-contest-closed-f75/",
		"http://forums.redflagdeals.com/ncix-boxing-week-2006-wish-list-contest-contest-closed-f75/",
		"http://forums.redflagdeals.com/rfd-5th-anniversary-create-win-1000-ncix-wish-list-f51/",
		"http://forums.redflagdeals.com/build-win-2-000-ncix-com-custom-pc-contest-f65/",
		"http://forums.redflagdeals.com/pricecanada-com-1st-anniversary-contest-f71/",
		"http://forums.redflagdeals.com/ncix-com-build-your-back-school-pc-2007-contest-f85/",
		"http://forums.redflagdeals.com/ncix-grand-reopening-contest-f82/",
		"http://forums.redflagdeals.com/ncix-10th-anniversary-create-win-500-ncix-wish-list-f61/",
		"http://forums.redflagdeals.com/ncix-boxing-week-2007-wish-list-contest-f94/",
		"http://forums.redflagdeals.com/create-win-your-3-000-newegg-ca-wish-list-contest-f108/",
		"http://forums.redflagdeals.com/tell-us-your-story-valentines-day-contest-2008-f96/",
		"http://forums.redflagdeals.com/redflagdeals-com-1st-annual-member-awards-f80/",
		"http://forums.redflagdeals.com/2nd-annual-redflagdeals-com-member-awards-f98/",
		"http://forums.redflagdeals.com/3rd-annual-member-awards-congrats-winners-f113/",
		"http://forums.redflagdeals.com/redflagdeals-2013-holiday-wish-list-giveaway-ncix-com-over-2-500-prizes-f146/",
		"http://forums.redflagdeals.com/boxing-day-2012-deals-archive-f147/",
		"http://forums.redflagdeals.com/black-friday-cyber-monday-2012-f138/",
		"http://forums.redflagdeals.com/us-black-friday-cyber-monday-deals-discussion-2013-f144/",
		"http://forums.redflagdeals.com/black-friday-cyber-monday-deals-discussion-2013-f137/",
		"http://forums.redflagdeals.com/boxing-day-2013-deals-archive-f118/",
		"http://forums.redflagdeals.com/boxing-day-2013-discussion-archive-f119/",
		"http://forums.redflagdeals.com/black-friday-cyber-monday-2014-f175/",
		"http://forums.redflagdeals.com/boxing-day-2014-deals-archive-f181/",
		"http://forums.redflagdeals.com/boxing-day-2014-discussion-archive-f183/",
		"http://forums.redflagdeals.com/black-friday-deals-2015-archive-f149/",
		"http://forums.redflagdeals.com/black-friday-discussion-2015-f179/",
		"http://forums.redflagdeals.com/cyber-monday-deals-2015-f177/",
		"http://forums.redflagdeals.com/boxing-day-2015-deals-archive-f151/",
		"http://forums.redflagdeals.com/boxing-day-2015-discussion-archive-f153/"
        ]
	COUNTRY = "CAN"
	THREAD_XPATH = "//a[@class='topic_title_link']"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "//a[re:test(@class,'pagination_last*')]/@href"
	PREV_XPATH = "//a[@rel='prev']/@href"
	POST_XPATH = "//section[@class='thread_posts']//article"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//span[@class='dateline_timestamp']//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//a[@class='postauthor']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post_content']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": "concat((//input[@class='pagination_input_box']/@data-base-url)[last()],.//a[@class='dateline_permalink']/@href)"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//h1[@class='thread_title']/text()"
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
