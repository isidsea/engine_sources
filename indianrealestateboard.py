from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "indianrealestateboard"
	CRAWLER_NAME = "indianrealestateboard crawler"
	LINK_TO_CRAWL = [
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/49-Bengaluru-Real-Estate?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/116-Bengaluru-Central-Apartment-Villa-Projects?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/130-North-Bengaluru-Apartment-Villa-Projects?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/137-South-Bengaluru-Apartment-Villa-Projects?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/121-Bengaluru-Plots-Layouts?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/122-Mysuru-amp-Karnatak-Real-Estate?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/30-Bengaluru-Karnataka-General-Topics?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/53-Bengaluru-Karnataka-Real-Estate-Classifieds?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/131-Classifieds-by-service-providers-in-Karnataka?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/23-Chennai-Real-Estate?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/24-Chennai-Apartment-Villa-Projects?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/128-Chennai-OMR-ECR-Apartment-Villa-Projects?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/134-Chennai-GST-Apartment-Villa-Projects?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/135-Chennai-West-Apartment-Villa-Projects?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/136-Chennai-South-Apartment-Villa-Projects?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/101-Chennai-Plots-Layouts?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/100-Coimbatore-amp-Tamil-Nadu-Real-Estate?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/28-Chennai-Tamil-Nadu-General-Topics?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/107-Chennai-Classifieds?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/129-Tamil-Nadu-Classifieds?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/132-Classifieds-by-service-providers-in-Tamilnadu?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/14-Hyderabad-Real-Estate?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/54-Hyderabad-Secunderabad-Apartment-Villa?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/16-Hyderabad-West-Area-Apartment-Villa-Projects?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/35-Hyderabad-Plots-Layouts?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/39-Andhra-Pradesh-Cities-Real-Estate?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/31-Hyderabad-amp-Andhra-General-Topics?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/108-Hyderabad-amp-Andhra-Real-Estate-Classifieds?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/26-Delhi-NCR-Gurgaon-Noida-Real-Estate?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/119-Delhi-NCR-Gurgaon-Noida-Apartments-Villa?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/120-Delhi-NCR-Gurgaon-Noida-General-Topics?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/18-Delhi-NCR-Gurgaon-Noida-Classifieds?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/102-Mumbai-Real-Estate?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/42-Mumbai-Real-Estate-Classifieds?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/127-Maharashtra-Cities-Real-Estate?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/27-Mumbai-General-Topics?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/38-Indian-Real-Estate-General-Discussions?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/21-Gujarat-Cities-Ahmedabad?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/40-Kerala-Cities-Kochi-Trivandrum?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/41-Kolkota-amp-W-Bengal?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/9-Chandigarh-Panchkula-Punjab?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/51-Indian-Real-Estate-Other-Cities?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/48-Real-Estate-USA-amp-Other-Countries?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/36-Indian-Real-Estate-Laws-Documentation?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/20-Indian-Real-Estate-Investments-by-NRI?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/37-Building-Materials-Furnishing?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/59-Off-Topic-amp-Chit-Chat?",
		"http://www.indianrealestateboard.com/forums/forumdisplay.php/105-Forum-Usage-FAQ?"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//ol[@id='threads']/li[re:test(@id,'thread_*')]"
	THREAD_LINK_XPATH = "concat('forums/',.//a[re:test(@id,'thread_title_*')]/@href)"
	LAST_PAGE_XPATH = "concat(substring(concat('forums/',(//div[@id='pagination_top']//span[@class='first_last'])[last()]/a/@href),1 div contains(concat('forums/',(//div[@id='pagination_top']//span[@class='first_last'])[last()]/a/@href),'showthread')),substring(		'',	1 div not(contains(concat('forums/',(//div[@id='pagination_top']//span[@class='first_last'])[last()]/a/@href),'showthread'))))"
	PREV_XPATH = "concat('forums/',//div[@id='pagination_top']//span[@class='prev_next']/a/@href)"
	POST_XPATH = "//div[@id='postlist']//ol[@class='posts']/li[re:test(@id,'post_*')]//div[@class='posthead']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//span[@class='date']//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='username_container']//a/strong/span/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='postrow']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": "concat('forums/',.//a[@class='postcounter']/@href)"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//span[@class='threadtitle']//text()"
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
