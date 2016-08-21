from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "mosh"
	CRAWLER_NAME = "mosh crawler"
	LINK_TO_CRAWL = [
		"http://forum.mosh.ph/viewforum.php?f=13",
		"http://forum.mosh.ph/viewforum.php?f=32"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//ul[@class='topiclist topics']//a[@class='topictitle']"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "//div[@class='pagination']//a[@rel='next']/preceding::a[1]/@href"
	PREV_XPATH = "//div[@class='pagination']//a[@rel='prev']/@href"
	POST_XPATH = "//div[@id='page-body']/div[re:test(@id,'p*') and re:test(@class,'post has-profile bg*')]"
	# POST_XPATH = "//div[@id='page-body']/div[re:test(@id,'p*')]//div[@class='postbody']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//p[@class='author']/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//p[@class='author']//a[re:test(@class,'username')]/text()"
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
			"xpath": "concat(substring-after(//h2[@class='topic-title']/a/@href,'./'),'&#',./@id)"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//h2[@class='topic-title']/a/text()"
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
