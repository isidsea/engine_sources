from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "paksc"
	CRAWLER_NAME = "paksc crawler"
	LINK_TO_CRAWL = [
		"http://forum.paksc.org/Forum-Introductions",
		"http://forum.paksc.org/Forum-Scientific-Questions-Answers",
		"http://forum.paksc.org/Forum-Books",
		"http://forum.paksc.org/Forum-jobs-opportunities",
		"http://forum.paksc.org/Forum-Share-your-Problems",
		"http://forum.paksc.org/Forum-Events",
		"http://forum.paksc.org/Forum-In-the-News",
		"http://forum.paksc.org/Forum-Site-Feedback",
		"http://forum.paksc.org/Forum-Academic-Guidance",
		"http://forum.paksc.org/Forum-Career-Guidance",
		"http://forum.paksc.org/Forum-Renewable-Energy--11",
		"http://forum.paksc.org/Forum-BIOMASS",
		"http://forum.paksc.org/Forum-Biogas-Plant",
		"http://forum.paksc.org/Forum-Biodiesel",
		"http://forum.paksc.org/Forum-Solar-Energy",
		"http://forum.paksc.org/Forum-Solar-Panel",
		"http://forum.paksc.org/Forum-Solar-Heating-Discussion",		
		"http://forum.paksc.org/Forum-Wind-Turbine-Alternator",
		"http://forum.paksc.org/Forum-Wind-Turbine-Blades",
		"http://forum.paksc.org/Forum-Free-Energy",
		"http://forum.paksc.org/Forum-Human-Power",
		"http://forum.paksc.org/Forum-Hybrid-and-Electric-Cars",
		"http://forum.paksc.org/Forum-Hydrogen-Fuel-Cells",
		"http://forum.paksc.org/Forum-General-Discussion--28",
		"http://forum.paksc.org/Forum-New-Science-Fair-Projects-Ideas",
		"http://forum.paksc.org/Forum-Final-Year-Projects",
		"http://forum.paksc.org/Forum-Homemade-UPS-inverter",
		"http://forum.paksc.org/Forum-Water-Rocket",
		"http://forum.paksc.org/Forum-DIY-Wind-Turbine",
		"http://forum.paksc.org/Forum-DIY-Do-it-Yourself-Help",
		"http://forum.paksc.org/Forum-Computer-Science",
		"http://forum.paksc.org/Forum-Computer-Hardware",
		"http://forum.paksc.org/Forum-Computer-Software",
		"http://forum.paksc.org/Forum-Internet-Marketing",
		"http://forum.paksc.org/Forum-SEO-Tips-and-Tricks",
		"http://forum.paksc.org/Forum-Microbiology-and-Immunology",
		"http://forum.paksc.org/Forum-General-Discussion--44",
		"http://forum.paksc.org/Forum-Class-3-to-5",
		"http://forum.paksc.org/Forum-Science-Competitions-Intel-ISEF-Google-Science-Fair-GIKI-NUST-Olympiad",
		"http://forum.paksc.org/Forum-Hand-on-Science--57"
        ]
	COUNTRY = "PAK"
	# THREAD_XPATH = "//span[re:test(@id,'tid_*')]"
	THREAD_XPATH = "//tr[@class='inline_row']//span[@class=' subject_new']"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "//div[@class='pagination']/a[@class='pagination_next']/preceding-sibling::a[1]/@href"
	PREV_XPATH = "//div[@class='pagination']/a[@class='pagination_previous']/@href"
	POST_XPATH = "//div[@id='posts']//div[re:test(@id,'post_*') and @class='post classic ']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//span[@class='post_date']/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='author_information']/strong/span//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@id,'pid_*')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//div[@class='post_head']//strong/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//fieldset[@class='breadcrumb']//span[@class='crust'][last()]/a/text()"
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
