from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "r2iclubforums"
	CRAWLER_NAME = "r2iclubforums crawler"
	LINK_TO_CRAWL = [
		"http://www.r2iclubforums.com/forums/forumdisplay.php/11-R2I-Dilemma",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/137-R2I-Planning-amp-Preparation",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/16-R2I-Diaries",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/136-R2I-Goods-to-Take-to-India",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/138-R2I-Packing-Shipping-Questions",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/21-Shipping-Companies-amp-Experience",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/113-I-Wish-to-Share-Container",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/35-To-Chennai-Bengaluru-Tamil-Nadu-Karnataka",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/14-To-Hyderabad-amp-AP",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/99-To-Pune-Mumbai-Maharashtra",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/23-To-NCR-North-India",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/102-To-Kolkata-Eastern-India",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/51-To-Other-India-cities",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/49-Back-to-USA",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/20-R2I-Settle-down",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/19-OCI-PIO-Visa-Citizenship",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/132-R2I-Charity-Drive",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/59-General",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/52-Sports-Music-Movies-Travel-Entertainment",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/107-Cuisine",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/53-Family-amp-Kids",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/108-Health-Exercise",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/37-Religion-Philosophy-amp-Ethics",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/50-Science-Technology-Electronics",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/12-Women-s-Corner",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/47-Member-Blogs-amp-Articles",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/112-Misc-Classifieds",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/89-Global-Finance-amp-Economy",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/45-Asset-Allocation-Plans-(AAP)",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/88-USA-Finance-amp-Investments-General",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/17-USA-Banks-Savings-Credit-Card",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/46-USA-Fixed-Income-Insurance-Social-Security",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/111-USA-Mutual-Funds-Stocks-Derivatives",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/109-USA-401k-IRA-Roth-Strategy",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/48-USA-Real-Estate-amp-Home-loans",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/87-USA-Taxes",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/34-US-India-Dual-Tax-Cross-country-tax-FBAR",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/33-Other-countries-Investments-amp-Taxes",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/104-Indian-Investments-General-amp-News",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/7-Indian-Bank-Accounts-amp-Money-Transfer",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/114-Indian-Post-Office-Schemes-amp-Fixed-Income",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/5-Indian-Mutual-Funds-Stocks-IPO-PAN-card",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/117-Indian-Insurance-LIC-ULIP-Plans",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/24-Indian-Real-Estate-amp-Home-loans",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/36-Indian-Taxes",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/115-Rajesh-s-FEMA-amp-Tax-Forum",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/139-Investment-Basics-by-RRK",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/9-Self-Development",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/131-Career-Change-amp-Development",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/130-Job-Search-Preparation-Interview",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/133-Business-Ideas-Startup-Self-Employment",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/54-Indian-Jobs-amp-Career",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/129-Salary-CTC-Benefits",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/123-Bengaluru-Jobs",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/125-Chennai-Jobs",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/124-Hyderabad-Jobs",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/126-Mumbai-Pune-Jobs",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/116-Delhi-Gurgaon-Noida-Jobs",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/97-Jobs-Available",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/127-Jobs-Wanted",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/128-USA-Jobs-amp-Career",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/60-Life-in-USA",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/118-USA-Immigration-H1-GC-USC",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/55-Life-in-UK-Europe",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/42-Life-in-Other-Countries",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/120-Kids-Education-Abroad-(School-College)",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/119-News-Politics-Current-Affairs-Abroad",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/58-Life-in-India",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/103-Indian-Schools-amp-Education",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/98-Regional-Forums",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/30-Bengaluru-Karnataka",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/28-Chennai",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/100-Coimbatore-amp-Tamil-Nadu",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/26-Delhi-NCR",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/31-Hyderabad-amp-Andhra-Pradesh",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/27-Mumbai",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/25-Pune",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/40-Kerala-Cities",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/41-Kolkota-amp-W-Bengal",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/29-Other-Indian-Cities",
		"http://www.r2iclubforums.com/forums/forumdisplay.php/105-Forum-Usage-FAQ"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//li[re:test(@id,'thread_*')]"
	THREAD_LINK_XPATH = "concat('forums/',.//a[@class='title']/@href)"
	LAST_PAGE_XPATH = "concat(substring(concat('forums/',//div[@class='pagination_top']//span[@class='first_last']/a/@href),1 div contains(//div[@class='pagination_top']//span[@class='first_last']/a/@href, 'showthread')),substring('',	1 div not(contains(//div[@class='pagination_top']//span[@class='first_last']/a/@href, 'showthread'))))"
	PREV_XPATH = "concat(substring(concat('forums/',//div[@class='pagination_top']//a[@rel='prev']/@href),1 div contains(//div[@class='pagination_top']//a[@rel='prev']/@href, 'showthread')),substring('',1 div not(contains(//div[@class='pagination_top']//a[@rel='prev']/@href, 'showthread'))))"
	POST_XPATH = "//ol[@class='posts']/li[re:test(@id,'post_[0-9]+')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//span[re:test(@class,'postdate')]//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='contact']//strong//span/text()"
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
			"xpath": ".//a[@class='postcounter']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//h2[@class='posttitle icon']//text()"
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
