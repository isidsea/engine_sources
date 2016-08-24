from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "hiphopindo"
	CRAWLER_NAME = "hiphopindo crawler"
	LINK_TO_CRAWL = [
				# "http://hiphopindo.yuku.com/forums/2/JUALBELI-buyn-sell/JUALBELI-buyn-sell#.V6ma0nV95q8",
		"http://hiphopindo.yuku.com/forums/15/Gigs-Event/Gigs-Event#.V7K83Ch97IU",
		"http://hiphopindo.yuku.com/forums/8/INFO/INFO#.V7K9BSh97IU",
		"http://hiphopindo.yuku.com/forums/13/VideoPictures/VideoPictures#.V7K_Aih97IU",
		"http://hiphopindo.yuku.com/forums/1/FORUM-DISKUSI-discussion-forum/FORUM-DISKUSI-discussion-forum#.V7K_RCh97IU",
		"http://hiphopindo.yuku.com/forums/2/JUALBELI-buyn-sell/JUALBELI-buyn-sell#.V7K_Ryh97IU",
		"http://hiphopindo.yuku.com/forums/4/FREEPASS/FREEPASS#.V7K_SSh97IU",
		"http://hiphopindo.yuku.com/forums/5/MUSIC-CLINIC/MUSIC-CLINIC#.V7K_myh97IU",
		"http://hiphopindo.yuku.com/forums/6/BATTLE-ARENA/BATTLE-ARENA#.V7K_nSh97IU",
		"http://hiphopindo.yuku.com/forums/7/ONEonONE/ONEonONE#.V7K_oCh97IU"
        ]
	COUNTRY = "IDN"
	THREAD_XPATH = "//td[@class='topic-titles']"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//div[@class='pager  pager-list']/div[@class='number'])[last()]/a/@href"
	PREV_XPATH = "//div[@class='pager  pager-list']/div[@class='number current']/preceding::a[1]/@href"
	# POST_XPATH = "//table[@summary='user post and replies']/tbody"
	POST_XPATH = "//table[@summary='user post and replies']//tbody[re:test(@id,'post-id-*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//p[@class='post-date']/span//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//span[@class='user-name']/a/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			# "xpath":"concat(concat(.//td[@class='post-content lastcol ']//text(),''),concat(.//div[@class='post-body ']/div[@class='scrolling']/div[1]//text(),''))"
			# "xpath":"concat(.//td[@class='post-content lastcol ']//text(),'')"
			# "xpath":"concat(.//div[@class='post-body ']/div[@class='scrolling']/div[1]//text(),'')"
			# "xpath":"concat(,//div[@class='post-body ']/div[@class='scrolling']/div[1]//text())"
			"xpath":".//div[re:test(@class,'post-body')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": "concat('http://hiphopindo.yuku.com/sreply/',normalize-space(substring-after(./@id,'post-id-')),'/',//li[@class='odd last']/a/@title)"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//li[@class='odd last']/a/@title"
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
