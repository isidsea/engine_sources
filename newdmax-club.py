from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "newdmaxclub"
	CRAWLER_NAME = "Newdmaxclub Crawler"
	LINK_TO_CRAWL = ['http://www.newdmax-club.com/index.php?board=1.0.html',
		 'http://www.newdmax-club.com/index.php?board=39.0.html',
		 'http://www.newdmax-club.com/index.php?board=25.0.html',
		 'http://www.newdmax-club.com/index.php?board=15.0.html',
		 'http://www.newdmax-club.com/index.php?board=52.0.html',
		 'http://www.newdmax-club.com/index.php?board=16.0.html',
		 'http://www.newdmax-club.com/index.php?board=17.0.html',
		 'http://www.newdmax-club.com/index.php?board=24.0.html',
		 'http://www.newdmax-club.com/index.php?board=37.0.html',
		 'http://www.newdmax-club.com/index.php?board=18.0.html',
		 'http://www.newdmax-club.com/index.php?board=45.0.html',
		 'http://www.newdmax-club.com/index.php?board=46.0.html',
		 'http://www.newdmax-club.com/index.php?board=47.0.html',
		 'http://www.newdmax-club.com/index.php?board=48.0.html',
		 'http://www.newdmax-club.com/index.php?board=49.0.html',
		 'http://www.newdmax-club.com/index.php?board=50.0.html',
		 'http://www.newdmax-club.com/index.php?board=51.0.html',
		 'http://www.newdmax-club.com/index.php?board=6.0.html',
		 'http://www.newdmax-club.com/index.php?board=7.0.html',
		 'http://www.newdmax-club.com/index.php?board=12.0.html',
		 'http://www.newdmax-club.com/index.php?board=33.0.html',
		 'http://www.newdmax-club.com/index.php?board=13.0.html',
		 'http://www.newdmax-club.com/index.php?board=14.0.html',
		 'http://www.newdmax-club.com/index.php?board=27.0.html',
		 'http://www.newdmax-club.com/index.php?board=28.0.html',
		 'http://www.newdmax-club.com/index.php?board=31.0.html',
		 'http://www.newdmax-club.com/index.php?board=32.0.html',
		 'http://www.newdmax-club.com/index.php?board=41.0.html',
		 'http://www.newdmax-club.com/index.php?board=9.0.html',
		 'http://www.newdmax-club.com/index.php?board=10.0.html',
		 'http://www.newdmax-club.com/index.php?board=11.0.html',
		 'http://www.newdmax-club.com/index.php?board=3.0.html',
		 'http://www.newdmax-club.com/index.php?board=4.0.html',
		 'http://www.newdmax-club.com/index.php?board=5.0.html',
		 'http://www.newdmax-club.com/index.php?board=8.0.html',
		 'http://www.newdmax-club.com/index.php?board=19.0.html',
		 'http://www.newdmax-club.com/index.php?board=20.0.html',
		 'http://www.newdmax-club.com/index.php?board=21.0.html',
		 'http://www.newdmax-club.com/index.php?board=43.0.html',
		 'http://www.newdmax-club.com/index.php?board=42.0.html',
		 'http://www.newdmax-club.com/index.php?board=22.0.html',
		 'http://www.newdmax-club.com/index.php?board=36.0.html',
		 'http://www.newdmax-club.com/index.php?board=40.0.html'
	]
	COUNTRY = "THA"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagelinks floatleft']/a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "//div[@class='pagelinks floatleft']/strong/preceding-sibling::a[1]/@href" 
	POST_XPATH = "//form[@id='quickModForm']//div[@class='post_wrapper']"
	FIELDS = [
		 {"published_date": {
		 	"single": True,
		 	"data_type": "date",
		 	"concat": False,
		 	"xpath": "substring-before(concat(.//div[@class='keyinfo']//div[@class='smalltext']/text()[2],substring-after(.//div[@class='keyinfo']//div[@class='smalltext']/text()[3],'เวลา')),'»')"
		 }},
		{"author_name": {
			"single": True,
			"data_type": "string",
			"concat": False,
			"xpath": "normalize-space(.//div[@class='poster']/h4/a/text())"
		}},
		{"content": {
			"single": True,
			"data_type": "string",
			"concat": False,
			"xpath": ".//div[@class='postarea']//div[@class='post']//div[re:test(@id,'msg_*')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//div[@class='postarea']//div[@class='keyinfo']//h5[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title": {
			"single": True,
			"data_type": "string",
			"concat": False,
			"xpath":"normalize-space(substring-before(substring-after(//div[@id='forumposts']//div[@class='cat_bar']//h3[@class='catbg']//text()[3],':'),'('))"
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
