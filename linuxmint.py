from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "linuxmint"
	CRAWLER_NAME = "linuxmint crawler"
	LINK_TO_CRAWL = [
				# "https://forums.linuxmint.com/viewforum.php?f=90",
		"https://forums.linuxmint.com/viewforum.php?f=17",
		"https://forums.linuxmint.com/viewforum.php?f=143",
		"https://forums.linuxmint.com/viewforum.php?f=90",
		"https://forums.linuxmint.com/viewforum.php?f=46",
		"https://forums.linuxmint.com/viewforum.php?f=47",
		"https://forums.linuxmint.com/viewforum.php?f=231",
		"https://forums.linuxmint.com/viewforum.php?f=49",
		"https://forums.linuxmint.com/viewforum.php?f=50",
		"https://forums.linuxmint.com/viewforum.php?f=51",
		"https://forums.linuxmint.com/viewforum.php?f=52",
		"https://forums.linuxmint.com/viewforum.php?f=150",
		"https://forums.linuxmint.com/viewforum.php?f=53",
		"https://forums.linuxmint.com/viewforum.php?f=157",
		"https://forums.linuxmint.com/viewforum.php?f=54",
		"https://forums.linuxmint.com/viewforum.php?f=18",
		"https://forums.linuxmint.com/viewforum.php?f=6",
		"https://forums.linuxmint.com/viewforum.php?f=48",
		"https://forums.linuxmint.com/viewforum.php?f=42",
		"https://forums.linuxmint.com/viewforum.php?f=235",
		"https://forums.linuxmint.com/viewforum.php?f=211",
		"https://forums.linuxmint.com/viewforum.php?f=214",
		"https://forums.linuxmint.com/viewforum.php?f=212",
		"https://forums.linuxmint.com/viewforum.php?f=213",
		"https://forums.linuxmint.com/viewforum.php?f=180",
		"https://forums.linuxmint.com/viewforum.php?f=60",
		"https://forums.linuxmint.com/viewforum.php?f=61",
		"https://forums.linuxmint.com/viewforum.php?f=58",
		"https://forums.linuxmint.com/viewforum.php?f=225",
		"https://forums.linuxmint.com/viewforum.php?f=19",
		"https://forums.linuxmint.com/viewforum.php?f=120",
		"https://forums.linuxmint.com/viewforum.php?f=163",
		"https://forums.linuxmint.com/viewforum.php?f=29",
		"https://forums.linuxmint.com/viewforum.php?f=43",
		"https://forums.linuxmint.com/viewforum.php?f=63",
		"https://forums.linuxmint.com/viewforum.php?f=64",
		"https://forums.linuxmint.com/viewforum.php?f=65",
		"https://forums.linuxmint.com/viewforum.php?f=68",
		"https://forums.linuxmint.com/viewforum.php?f=145",
		"https://forums.linuxmint.com/viewforum.php?f=224",
		"https://forums.linuxmint.com/viewforum.php?f=67",
		"https://forums.linuxmint.com/viewforum.php?f=71",
		"https://forums.linuxmint.com/viewforum.php?f=227",
		"https://forums.linuxmint.com/viewforum.php?f=172",
		"https://forums.linuxmint.com/viewforum.php?f=66",
		"https://forums.linuxmint.com/viewforum.php?f=72",
		"https://forums.linuxmint.com/viewforum.php?f=75",
		"https://forums.linuxmint.com/viewforum.php?f=243"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//ul[@class='topiclist topics']/li"
	THREAD_LINK_XPATH = ".//a[@class='topictitle']/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagination']//a[not(contains(text(),'Next'))])[last()]/@href"
	PREV_XPATH = "//div[@class='pagination']//a[@rel='prev']/@href"
	POST_XPATH = "//div[@id='page-body']/div[re:test(@id,'p*') and re:test(@class,'post has-profile bg*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//div[@class='postbody']//p[@class='author']/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": "concat(.//p[@class='author']//a[re:test(@class,'username')]/text(),.//p[@class='author']//span[re:test(@class,'username')]/text())"
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
