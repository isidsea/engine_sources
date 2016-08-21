from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "cricistan"
	CRAWLER_NAME = "cricistan crawler"
	LINK_TO_CRAWL = [
		"https://cricistan.com/forums/cricket_talk/",
		"https://cricistan.com/forums/sportistan.6/",
		"https://cricistan.com/forums/commentary_archive/",
		"https://cricistan.com/forums/the-pavilion.10/"
        ]
	COUNTRY = "PAK"
	THREAD_XPATH = "//ol/li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//h3[@class='title']/a/@href"
	LAST_PAGE_XPATH = "(//div[@class='PageNav']/nav/a)[last()-1]/@href"
	PREV_XPATH = "//div[@class='PageNav']/nav//a[contains(text(),'< Prev')]/@href"
	POST_XPATH = "//form[@class='InlineModForm section']/ol/li[re:test(@id,'post-*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "concat(.//div[@class='privateControls hiddenResponsiveMedium hiddenResponsiveNarrow']//a[@class='datePermalink']/abbr/text(),.//div[@class='privateControls hiddenResponsiveMedium hiddenResponsiveNarrow']//a[@class='datePermalink']/span/@title)"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//h3[@class='userText']//a//text()"
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
			"xpath": ".//div[@class='publicControls']/a[@title='Permalink']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='titleBar']/h1//text()"
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
