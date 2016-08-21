from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "ittaleem"
	CRAWLER_NAME = "ittaleem crawler"
	LINK_TO_CRAWL = [
		"http://www.ittaleem.com/announcment-greetings/",
		"http://www.ittaleem.com/introduction/",
		"http://www.ittaleem.com/ittaleem-anniversaries/",
		"http://www.ittaleem.com/latest-news/",
		"http://www.ittaleem.com/complains-suggestions/",
		"http://www.ittaleem.com/read-me-first/",
		"http://www.ittaleem.com/ramzan-kareem/",
		"http://www.ittaleem.com/quran-e-kareem/",
		"http://www.ittaleem.com/learn-quran/",
		"http://www.ittaleem.com/hadith-o-sunnat/",
		"http://www.ittaleem.com/hayat-e-rasool-s-w-w/",
		"http://www.ittaleem.com/khatm-e-nubuwwat/",
		"http://www.ittaleem.com/open-forum/",
		"http://www.ittaleem.com/zaarori-maloomat/",
		"http://www.ittaleem.com/islamic-history/",
		"http://www.ittaleem.com/basics-islam/",
		"http://www.ittaleem.com/islamic-audios/",
		"http://www.ittaleem.com/urdu-tutorials/",
		"http://www.ittaleem.com/amin-s/",
		"http://www.ittaleem.com/courses/",
		"http://www.ittaleem.com/computer-hardware/",
		"http://www.ittaleem.com/networking/",
		"http://www.ittaleem.com/urdu-inpage/",
		"http://www.ittaleem.com/video-editing/",
		"http://www.ittaleem.com/adobe-photoshop/",
		"http://www.ittaleem.com/word-pad/",
		"http://www.ittaleem.com/html/",
		"http://www.ittaleem.com/microsoft-excel/",
		"http://www.ittaleem.com/notepad/",
		"http://www.ittaleem.com/internet/",
		"http://www.ittaleem.com/microsoft-frontpage/",
		"http://www.ittaleem.com/microsoft-access/",
		"http://www.ittaleem.com/windows-xp/",
		"http://www.ittaleem.com/ms-paint/",
		"http://www.ittaleem.com/mozilla-firefox/",
		"http://www.ittaleem.com/php/",
		"http://www.ittaleem.com/visual-basic/",
		"http://www.ittaleem.com/arabic-learning/",
		"http://www.ittaleem.com/english-learning/",
		"http://www.ittaleem.com/freehand-mx/",
		"http://www.ittaleem.com/webdesigning/",
		"http://www.ittaleem.com/macromedia-dreamweaver/",
		"http://www.ittaleem.com/c-sharp-c-c/",
		"http://www.ittaleem.com/flash-mx/",
		"http://www.ittaleem.com/window-s-registry/",
		"http://www.ittaleem.com/ms-other-windows/",
		"http://www.ittaleem.com/java-script/",
		"http://www.ittaleem.com/search-engine-optimisation-seo/",
		"http://www.ittaleem.com/c/",
		"http://www.ittaleem.com/corel-draw/",
		"http://www.ittaleem.com/google-adsense/",
		"http://www.ittaleem.com/short-hand/",
		"http://www.ittaleem.com/microsoft-powerpoint/",
		"http://www.ittaleem.com/ccna/",
		"http://www.ittaleem.com/hardware-troubleshooting/",
		"http://www.ittaleem.com/quantity-survey-engineering/",
		"http://www.ittaleem.com/ms-dos/",
		"http://www.ittaleem.com/microsoft-word/",
		"http://www.ittaleem.com/developing-mobile-app/'",
		"http://www.ittaleem.com/articles/",
		"http://www.ittaleem.com/anti-hacking/",
		"http://www.ittaleem.com/website-reviews/",
		"http://www.ittaleem.com/general-discussion/",
		"http://www.ittaleem.com/videos/",
		"http://www.ittaleem.com/mobile-palace/",
		"http://www.ittaleem.com/websites/",
		"http://www.ittaleem.com/applications/",
		"http://www.ittaleem.com/mobile-hardware/",
		"http://www.ittaleem.com/games/",
		"http://www.ittaleem.com/sms-collection/",
		"http://www.ittaleem.com/mobilemasti/",
		"http://www.ittaleem.com/mobile-operator-updates/'",
		"http://www.ittaleem.com/cool-gadgets/",
		"http://www.ittaleem.com/price-watch/'",
		"http://www.ittaleem.com/classes/",
		"http://www.ittaleem.com/9th/",
		"http://www.ittaleem.com/10th/",
		"http://www.ittaleem.com/11th/",
		"http://www.ittaleem.com/12th/",
		"http://www.ittaleem.com/all-others/",
		"http://www.ittaleem.com/results/",
		"http://www.ittaleem.com/online-university/",
		"http://www.ittaleem.com/students-news/",
		"http://www.ittaleem.com/admissions/",
		"http://www.ittaleem.com/date-sheet/",
		"http://www.ittaleem.com/general-knowledge/",
		"http://www.ittaleem.com/historical-places/",
		"http://www.ittaleem.com/videos/",
		"http://www.ittaleem.com/study-abroad/",
		"http://www.ittaleem.com/jobs-corner/",
		"http://www.ittaleem.com/shair-o-shayri/",
		"http://www.ittaleem.com/aansoo-s-choice/",
		"http://www.ittaleem.com/irfansajid-s-choice/",
		"http://www.ittaleem.com/designed-poetry/",
		"http://www.ittaleem.com/ashaar/",
		"http://www.ittaleem.com/ghazal/",
		"http://www.ittaleem.com/nazmein/'",
		"http://www.ittaleem.com/urdu-adab/",
		"http://www.ittaleem.com/urdu-books-novels/",
		"http://www.ittaleem.com/local-languages/",
		"http://www.ittaleem.com/pashtu/",
		"http://www.ittaleem.com/punjabi/",
		"http://www.ittaleem.com/balouchi/",
		"http://www.ittaleem.com/sindhi/",
		"http://www.ittaleem.com/siraiki/",
		"http://www.ittaleem.com/english-literature/",
		"http://www.ittaleem.com/behas-o-mubahisa/",
		"http://www.ittaleem.com/sports-events/",
		"http://www.ittaleem.com/articles/",
		"http://www.ittaleem.com/talk-shows/",
		"http://www.ittaleem.com/biz-news/",
		"http://www.ittaleem.com/interview-zone/",
		"http://www.ittaleem.com/books-reviews/",
		"http://www.ittaleem.com/e-books/",
		"http://www.ittaleem.com/baat-cheet/",
		"http://www.ittaleem.com/humor-jokes/",
		"http://www.ittaleem.com/picture-gallery/",
		"http://www.ittaleem.com/funmaza/",
		"http://www.ittaleem.com/mardon-ki-baithak/",
		"http://www.ittaleem.com/khawateen-markaz/",
		"http://www.ittaleem.com/fashion-beauty/",
		"http://www.ittaleem.com/health-fitness/",
		"http://www.ittaleem.com/khana-khazana/",
		"http://www.ittaleem.com/home-decoration/",
		# "http://www.ittaleem.com/wedding-arrangements/"
        ]
	COUNTRY = "PAK"
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
			"xpath":".//span[@class='date']//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='userinfo']//a/strong//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@id,'post_message_*')]//text()"
			# "xpath":"concat(.//div[@class='postbody']//h2[@class='title icon']/text(),.//div[re:test(@id,'post_message_*')]//text())"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[re:test(@name,'post*')]/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='breadcrumb']//li[@class='navbit lastnavbit']/span/text()"
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
