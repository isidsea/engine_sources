from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "world-a-team"
	CRAWLER_NAME = "world-a-team crawler"
	LINK_TO_CRAWL = [
		"http://world-a-team.com/cricket-forum.php",
		"http://world-a-team.com/international-test-cricket/",
		"http://world-a-team.com/odi-20-20-cricket/",
		"http://world-a-team.com/all-other-cricket/",
		"http://world-a-team.com/world-teams/",
		"http://world-a-team.com/members-guest-lounge/",
		"http://world-a-team.com/great-modern-historical-debates/",
		"http://world-a-team.com/great-posts/",
		"http://world-a-team.com/reported-posts/",
		"http://world-a-team.com/help-feedback/"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//a[re:test(@id,'thread_title_*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "(//div[@class='pagenav']//a[not(contains(text(),'>'))])[last()]/@href"
	PREV_XPATH = "//div[@class='pagenav']//a[contains(text(),'<')]/@href"
	POST_XPATH = "//div[@id='posts']//table[re:test(@id,'post*')]"
	
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"substring(.//a[re:test(@name,'post*')]/following-sibling::text()[1],0,40)"
			# "xpath":"translate(.//a[re:test(@name,'post*')]/following-sibling::text()[1],'in reply to','')"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[re:test(@id,'postmenu_*')]/a//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@id,'post_message_*')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[re:test(@id,'postcount*')]/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//span[@class='navbar'])[last()]/a//text()"
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
