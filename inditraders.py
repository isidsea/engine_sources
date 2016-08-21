from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "inditraders"
	CRAWLER_NAME = "inditraders crawler"
	LINK_TO_CRAWL = [
		"http://www.inditraders.com/announcements/",
		"http://www.inditraders.com/introductions/",
		"http://www.inditraders.com/beginners-section/",
		"http://www.inditraders.com/markets-general/",
		"http://www.inditraders.com/journals/",
		"http://www.inditraders.com/view-only-journals/",
		"http://www.inditraders.com/stocks/",
		"http://www.inditraders.com/fundamentals/",
		"http://www.inditraders.com/economics/",
		"http://www.inditraders.com/stocks-indices/",
		"http://www.inditraders.com/futures-options/",
		"http://www.inditraders.com/forex/",
		"http://www.inditraders.com/technical-analysis/",
		"http://www.inditraders.com/auto-algo-trading/",
		"http://www.inditraders.com/market-profile/",
		"http://www.inditraders.com/price-volume-analysis/",
		"http://www.inditraders.com/indicators-systems/",
		"http://www.inditraders.com/automated-trading/",
		"http://www.inditraders.com/software/",
		"http://www.inditraders.com/amibroker/",
		"http://www.inditraders.com/arthachitra/",
		"http://www.inditraders.com/matlab/",
		"http://www.inditraders.com/metastock/",
		"http://www.inditraders.com/metatrader/",
		"http://www.inditraders.com/ninjatrader/",
		"http://www.inditraders.com/tradestation/",
		"http://www.inditraders.com/other-platforms/",
		"http://www.inditraders.com/hardware/",
		"http://www.inditraders.com/data/",
		"http://www.inditraders.com/brokers/",
		"http://www.inditraders.com/psychology/",
		"http://www.inditraders.com/trade-management/",
		"http://www.inditraders.com/resources/",
		"http://www.inditraders.com/reviews/",
		"http://www.inditraders.com/chit-chat/",
		"http://www.inditraders.com/feedback/"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//table[@id='threadslist']//td[re:test(@id,'td_threadtitle_*')]"
	THREAD_LINK_XPATH = ".//a[re:test(@id,'thread_title_*')]/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagenav']//td[@class='vbmenu_control'])[last()]//preceding::a[re:test(@title,'Last Page*') or re:test(@title,'Show results*')][1]/@href"
	PREV_XPATH = "//div[@class='pagenav']//a[@rel='prev']/@href"
	POST_XPATH = "//div[@id='posts']//div[re:test(@id,'edit*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"concat(substring-before(substring-after(substring-after(.//a[re:test(@name,'post*')]/following-sibling::text()[1],'-'),'-'),','),'/',	substring-before(substring-after(.//a[re:test(@name,'post*')]/following-sibling::text()[1],'-'),'-'),'/',substring-before(.//a[re:test(@name,'post*')]/following-sibling::text()[1],'-'),' ',	substring-after(substring-after(substring-after(.//a[re:test(@name,'post*')]/following-sibling::text()[1],'-'),'-'),','))"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//a[@class='bigusername']//text()"
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
			"xpath":"//td[@class='navbar']/strong/text()"
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
