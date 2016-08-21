from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "inforum"
	CRAWLER_NAME = "inforum crawler"
	LINK_TO_CRAWL = [
		"http://www.inforum.in/forums/general-indian-domain-name-discussion.4/",
		"http://www.inforum.in/forums/indian-idns.6/",
		"http://www.inforum.in/forums/lll-in-and-lll-co-in.5/",
		"http://www.inforum.in/forums/registrars.7/",
		"http://www.inforum.in/forums/resources.8/",
		"http://www.inforum.in/forums/available-expiring-indian-domain-names.22/",
		"http://www.inforum.in/forums/non-indian-domains.27/",
		"http://www.inforum.in/forums/new-gtlds.28/",
		"http://www.inforum.in/forums/for-sale.9/",
		"http://www.inforum.in/forums/non-india-related-domains.14/",
		"http://www.inforum.in/forums/domains-wanted.15/",
		"http://www.inforum.in/forums/websites.16/",
		"http://www.inforum.in/forums/auctions.10/",
		"http://www.inforum.in/forums/external-auctions.12/",
		"http://www.inforum.in/forums/adult-domains.11/",
		"http://www.inforum.in/forums/for-sale-advertising.13/",
		"http://www.inforum.in/forums/domain-appraisals.19/",
		"http://www.inforum.in/forums/legal-issues-and-dispute.23/",
		"http://www.inforum.in/forums/business-and-economy.20/",
		"http://www.inforum.in/forums/indian-websites-and-start-ups.24/",
		"http://www.inforum.in/forums/parking.21/",
		"http://www.inforum.in/forums/development-options.36/",
		"http://www.inforum.in/forums/webmaster-forum.25/",
		"http://www.inforum.in/forums/marketing-your-website.38/",
		"http://www.inforum.in/forums/hosting.37/",
		"http://www.inforum.in/forums/website-reviews.26/",
		"http://www.inforum.in/forums/introduce-yourself.18/",
		"http://www.inforum.in/forums/the-lounge.17/"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//ol[@class='discussionListItems']/li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//a[@class='PreviewTooltip']/@href"
	LAST_PAGE_XPATH = "(//div[@class='PageNav']//a[not (contains(text(),'Next >'))])[last()]/@href"
	PREV_XPATH = "//div[@class='PageNav']//a[contains(text(),'< Prev')]/@href"
	POST_XPATH = "//ol[@id='messageList']/li[re:test(@id,'post-*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"concat(.//span[@class='DateTime']/@title,.//abbr[@class='DateTime']/text())"
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
			"xpath":".//div[@class='messageContent']//blockquote/text()"
			# "xpath":".//div[@class='messageContent']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[@title='Permalink']/@href"
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
