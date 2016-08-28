from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "nasioc"
	CRAWLER_NAME = "nasioc crawler"
	LINK_TO_CRAWL = [
		"http://forums.nasioc.com/forums/forumdisplay.php?f=68",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=34",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=33",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=174",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=25",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=22",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=188",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=192",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=79",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=39",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=63",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=139",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=64",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=163",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=31",		
		"http://forums.nasioc.com/forums/forumdisplay.php?f=37",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=222",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=91",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=92",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=50",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=144",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=80",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=140",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=141",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=142",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=177",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=143",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=145",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=84",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=55",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=32",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=88",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=87",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=199",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=65",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=172",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=9",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=157",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=149",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=150",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=151",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=152",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=153",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=154",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=155",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=156",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=162",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=167",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=168",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=192",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=62",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=89",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=23",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=112",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=180",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=114",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=119",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=115",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=113",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=116",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=175",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=117",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=118",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=161",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=212",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=214",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=228",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=217",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=218",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=225",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=207",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=209",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=223",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=202",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=197",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=216",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=203",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=227",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=78",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=185",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=183",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=111",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=219",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=59",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=58",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=57",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=72",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=123",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=11",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=19",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=26",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=106",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=127",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=12",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=96",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=126",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=18",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=97",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=128",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=14",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=98",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=129",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=17",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=130",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=28",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=131",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=20",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=102",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=133",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=27",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=101",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=132",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=29",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=134",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=30",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=104",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=135",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=15",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=136",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=146",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=147",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=21",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=107",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=137",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=16",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=108",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=138",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=171",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=168",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=110",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=13",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=168",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=36",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=82",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=85",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=210",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=109",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=24",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=90",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=74",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=83",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=10",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=43",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=42",
		"http://forums.nasioc.com/forums/forumdisplay.php?f=40"
        ]
	COUNTRY = "USA"
	THREAD_XPATH = "//a[re:test(@id,'thread_title_*')]"
	THREAD_LINK_XPATH = "concat('forums/',./@href)"
	LAST_PAGE_XPATH = "concat(substring(concat('forums/',(//div[@class='pagenav']//td[@class='vbmenu_control'])[last()]//preceding::a[re:test(@title,'Last Page*') or re:test(@title,'Show results*')][1]/@href),1 div contains((//div[@class='pagenav']//td[@class='vbmenu_control'])[last()]//preceding::a[re:test(@title,'Last Page*') or re:test(@title,'Show results*')][1]/@href,'showthread')),substring('',1 div not(contains((//div[@class='pagenav']//td[@class='vbmenu_control'])[last()]//preceding::a[re:test(@title,'Last Page*') or re:test(@title,'Show results*')][1]/@href,'showthread'))))"
	# LAST_PAGE_XPATH = "concat('forums/',(//div[@class='pagenav']//td[@class='vbmenu_control'])[last()]//preceding::a[re:test(@title,'Last Page*') or re:test(@title,'Show results*')][1]/@href)"
	PREV_XPATH = "concat('forums/',//div[@class='pagenav']//a[re:test(@title,'Prev page*')]/@href)"
	POST_XPATH = "//div[@id='posts']//table[re:test(@id,'post*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
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
			"xpath": "concat('forums/',.//a[re:test(@id,'postcount*')]/@href)"
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
