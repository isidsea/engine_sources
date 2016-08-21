from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "virtualassistantforums"
	CRAWLER_NAME = "virtualassistantforums crawler"
	LINK_TO_CRAWL = [
		"http://www.virtualassistantforums.com/business-planning-development",
		"http://www.virtualassistantforums.com/your-home-office",
		"http://www.virtualassistantforums.com/software-apps-virtual-assistant-businesses",
		"http://www.virtualassistantforums.com/branding-your-virtual-assistant-business",
		"http://www.virtualassistantforums.com/establishing-your-niche",
		"http://www.virtualassistantforums.com/determining-your-virtual-assistant-services",
		"http://www.virtualassistantforums.com/finding-keeping-clients",
		"http://www.virtualassistantforums.com/rates-billing",
		"http://www.virtualassistantforums.com/policies-procedures",
		"http://www.virtualassistantforums.com/virtual-assistant-contracts",
		"http://www.virtualassistantforums.com/business-taxes-legal-issues",
		"http://www.virtualassistantforums.com/social-media",
		"http://www.virtualassistantforums.com/websites-blogs",
		"http://www.virtualassistantforums.com/networking-offline",
		"http://www.virtualassistantforums.com/general-marketing",
		"http://www.virtualassistantforums.com/member-introductions",		
		"http://www.virtualassistantforums.com/local-virtual-assistant-meetups",
		"http://www.virtualassistantforums.com/forum-faq-feedback"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//a[re:test(@id,'thread_title_*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "//div[@class='pagenav']//a[@rel='next']/preceding::a[1]/@href"
	PREV_XPATH = "//div[@class='pagenav']//a[@rel='prev']/@href"
	POST_XPATH = "//div[@id='posts']//table[re:test(@id,'post*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			# "xpath":".//table[re:test(@id,'post*')]//tr[1]/td[1]/text()"
			"xpath":".//a[re:test(@name,'post*')]/following-sibling::text()[1]"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//div[re:test(@id,'postmenu_*')]//text()"
			# "xpath": ".//a[@class='bigusername']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//td[re:test(@id,'td_post_*')]//text()"
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
			"xpath":"//div[@id='navbar-row']//h1//text()"
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
