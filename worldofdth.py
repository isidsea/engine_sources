from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "worldofdth"
	CRAWLER_NAME = "worldofdth crawler"
	LINK_TO_CRAWL = [
		"http://www.worldofdth.com/forums/17-DTH-News",
		"http://www.worldofdth.com/forums/36-TV-Channel-News",
		"http://www.worldofdth.com/forums/9-DD-Free-Dish",
		"http://www.worldofdth.com/forums/10-Dish-TV",
		"http://www.worldofdth.com/forums/18-Dish-TruHD",
		"http://www.worldofdth.com/forums/73-Dish-TruHD-(Plus)",
		"http://www.worldofdth.com/forums/13-Tata-Sky-DTH",
		"http://www.worldofdth.com/forums/21-Tata-Sky-HD",
		"http://www.worldofdth.com/forums/24-TATA-Sky-Transfer",
		"http://www.worldofdth.com/forums/15-Sun-Direct-DTH",
		"http://www.worldofdth.com/forums/19-Sun-Direct-HD",
		"http://www.worldofdth.com/forums/12-Reliance-Digital-TV",
		"http://www.worldofdth.com/forums/20-Reliance-Digital-TV-HD-DVR",
		"http://www.worldofdth.com/forums/68-Reliance-Digital-TV-HD",
		"http://www.worldofdth.com/forums/11-Airtel-Digital-TV",
		"http://www.worldofdth.com/forums/22-Airtel-Digital-TV-HD",
		"http://www.worldofdth.com/forums/69-Airtel-Digital-TV-HD-DVR",
		"http://www.worldofdth.com/forums/14-Videocon-D2H",
		"http://www.worldofdth.com/forums/49-Videocon-D2H-3D-HD-DVR",
		"http://www.worldofdth.com/forums/70-Videocon-D2H-HD",
		"http://www.worldofdth.com/forums/23-Foreign-DTHs",
		"http://www.worldofdth.com/forums/16-Dialog-DTH",
		"http://www.worldofdth.com/forums/51-Dish-Home-DTH-(Dish-Nepal-and-Home-TV)",
		"http://www.worldofdth.com/forums/29-KU-Band-Satellites-Updates",
		"http://www.worldofdth.com/forums/30-Satellites-News",
		"http://www.worldofdth.com/forums/31-Satellites-Hardware-software-and-Member-Setups",
		"http://www.worldofdth.com/forums/35-Cable-Television-News-and-Updates",
		"http://www.worldofdth.com/forums/56-Indian-TV-Channels-Programs",
		"http://www.worldofdth.com/forums/41-Entertainment-TV-Channels",
		"http://www.worldofdth.com/forums/42-Infotainment-Channels",
		"http://www.worldofdth.com/forums/43-Fashion-and-Lifestyle-Channels",
		"http://www.worldofdth.com/forums/44-Sports-Channels",
		"http://www.worldofdth.com/forums/45-Kids-Channels",
		"http://www.worldofdth.com/forums/46-Hindi-English-Movies-Channels",
		"http://www.worldofdth.com/forums/47-Regional-Channels",
		"http://www.worldofdth.com/forums/34-The-WOD-Lobby",
		"http://www.worldofdth.com/forums/26-Fun-zone",
		"http://www.worldofdth.com/forums/27-Computers-Internet-And-Technology",
		"http://www.worldofdth.com/forums/37-Radio-and-HITS",
		"http://www.worldofdth.com/forums/48-Travel-zone",
		"http://www.worldofdth.com/forums/50-Automobile-World",
		"http://www.worldofdth.com/forums/54-Software-Downloads-(-Freeware-)",
		"http://www.worldofdth.com/forums/55-Bollywood-Hollywood-News",
		"http://www.worldofdth.com/forums/64-IPTV-Services",
		"http://www.worldofdth.com/forums/65-Gadgets-Zone",
		"http://www.worldofdth.com/forums/66-Careers-And-Education",
		"http://www.worldofdth.com/forums/72-South-Indian-Movies",
		"http://www.worldofdth.com/forums/32-Broadband-providers",
		"http://www.worldofdth.com/forums/33-Sports-news",
		"http://www.worldofdth.com/forums/75-Cricket",
		"http://www.worldofdth.com/forums/39-Mobile-Phones-and-Accessories",
		"http://www.worldofdth.com/forums/40-Mobile-Telecom-Operators",
		"http://www.worldofdth.com/forums/53-3G-Service-Providers",
		"http://www.worldofdth.com/forums/25-WOD-Announcements",
		"http://www.worldofdth.com/forums/38-Suggestions-And-Feedback"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//ol[@class='stickies' or @class='threads']//li[re:test(@class,'thread_*')]"
	THREAD_LINK_XPATH = ".//a[re:test(@id,'thread_title_*')]/@href"
	LAST_PAGE_XPATH = "//div[@class='pagination_top']//span[@class='first_last']/a/@href"
	PREV_XPATH = "//div[@class='pagination_top']//span[@class='prev_next']/a/@href"
	POST_XPATH = "//ol[@class='posts']/li[re:test(@id,'post_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			# "xpath":"substring-before(.//span[@class='date']//text(),'GMT')"
			"xpath":".//span[@class='date']//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='userinfo']//a/strong/span/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@class,'postrow*')]//text()"
			# "xpath":".//div[@class='postrow']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[@class='postcounter']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			# "xpath":"//span[@class='threadtitle']//text()"
			"xpath":"//div[@class='pagetitle']/h1/span[@class='threadtitle']/a//text()"
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
