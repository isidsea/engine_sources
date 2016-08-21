from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "e-investing"
	CRAWLER_NAME = "e-investing crawler"
	LINK_TO_CRAWL = [
		"http://www.e-investing.in/rules-guidelines/",
		"http://www.e-investing.in/important-announcements/",
		"http://www.e-investing.in/markets-indices/",
		"http://www.e-investing.in/individual-stocks/",
		"http://www.e-investing.in/individual-portfolios/",
		"http://www.e-investing.in/sectors/",
		"http://www.e-investing.in/day-trading/",
		"http://www.e-investing.in/short-term-outlook/",
		"http://www.e-investing.in/long-term-outlook/",
		"http://www.e-investing.in/initial-public-offerings-ipo-market/",
		"http://www.e-investing.in/world-markets/",
		"http://www.e-investing.in/stock-market-psychology/",
		"http://www.e-investing.in/exchange-traded-funds/",
		"http://www.e-investing.in/fundamental-analysis/",
		"http://www.e-investing.in/technical-analysis/",
		"http://www.e-investing.in/trading-systems/",
		"http://www.e-investing.in/basics-derivatives/",
		"http://www.e-investing.in/index-derivatives/",
		"http://www.e-investing.in/stock-options/",
		"http://www.e-investing.in/stock-futures/",
		"http://www.e-investing.in/indian-economy/",
		"http://www.e-investing.in/world-economy/",
		"http://www.e-investing.in/credit-cards/",
		"http://www.e-investing.in/financial-services/",
		"http://www.e-investing.in/fixed-income-instruments/",
		"http://www.e-investing.in/insurance/",
		"http://www.e-investing.in/loans/",
		"http://www.e-investing.in/mutual-funds/",
		"http://www.e-investing.in/real-estate/",
		"http://www.e-investing.in/money-management/",
		"http://www.e-investing.in/taxation-legal/",
		"http://www.e-investing.in/other-personal-finance-issues/",
		"http://www.e-investing.in/commodities-trading/",
		"http://www.e-investing.in/forex-trading/",
		"http://www.e-investing.in/general-chat/",
		"http://www.e-investing.in/suggestions-feedback/",
		"http://www.e-investing.in/member-month-contest/",
		"http://www.e-investing.in/other-contests/"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//table[@id='threadslist']//td[re:test(@id,'td_threadtitle_*')]"
	THREAD_LINK_XPATH = ".//a[re:test(@id,'thread_title_*')]/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagenav']//td[@class='vbmenu_control'])[last()]//preceding::a[re:test(@title,'Last Page*') or re:test(@title,'Show results*')][1]/@href"
	PREV_XPATH = "//div[@class='pagenav']//a[contains(text(),'<')]/@href"
	POST_XPATH = "//div[@id='posts']//table[re:test(@id,'post*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//a[re:test(@name,'post*')]/following-sibling::text()[1]"
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
