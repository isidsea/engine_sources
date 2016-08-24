from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "indahnesia"
	CRAWLER_NAME = "indahnesia crawler"
	LINK_TO_CRAWL = [
				# "http://forum.indahnesia.com/forum/32/0/gezocht_aangeboden.php",
		"http://forum.indahnesia.com/forum/1/0/general_chat.php",
		"http://forum.indahnesia.com/forum/2/0/bali_the_island_of_the_gods.php",
		"http://forum.indahnesia.com/forum/3/0/jakarta_the_big_durian.php",
		"http://forum.indahnesia.com/forum/7/0/jawa_java.php",
		"http://forum.indahnesia.com/forum/22/0/sumatera.php",
		"http://forum.indahnesia.com/forum/23/0/sulawesi.php",
		"http://forum.indahnesia.com/forum/9/0/tickets_airlines_and_transport.php",
		"http://forum.indahnesia.com/forum/5/0/indonesia_hotel_information.php",
		"http://forum.indahnesia.com/forum/31/0/blog_indahnesia_com.php",
		"http://forum.indahnesia.com/forum/17/0/in_the_news.php",
		"http://forum.indahnesia.com/forum/20/0/indonesian_history.php",
		"http://forum.indahnesia.com/forum/19/0/a_visum_to_indonesia.php",
		"http://forum.indahnesia.com/forum/12/0/other_talk.php",
		"http://forum.indahnesia.com/forum/24/0/i_039_m_looking_for.php",
		"http://forum.indahnesia.com/forum/25/0/i_039_m_offering_this.php",
		"http://forum.indahnesia.com/forum/26/0/see_my_website.php",
		"http://forum.indahnesia.com/forum/6/0/website_forum_information.php",
		"http://forum.indahnesia.com/forum/8/0/user_feedback.php",
		"http://forum.indahnesia.com/forum/11/0/algemene_indonesi_euml_praat.php",
		"http://forum.indahnesia.com/forum/14/0/het_visumgebeuren.php",
		"http://forum.indahnesia.com/forum/15/0/bali_het_godeneiland.php",
		"http://forum.indahnesia.com/forum/16/0/java.php",
		"http://forum.indahnesia.com/forum/50/0/sumatra.php",
		"http://forum.indahnesia.com/forum/37/0/nusa_tenggara_-_de_kleine_sunda_eilanden.php",
		"http://forum.indahnesia.com/forum/13/0/hotels_in_indonesi_euml.php",
		"http://forum.indahnesia.com/forum/18/0/tickets_luchtvaart_en_vervoer.php",
		"http://forum.indahnesia.com/forum/21/0/indonesi_euml_op_z_039_n_nederlands.php",
		"http://forum.indahnesia.com/forum/34/0/blog_indonesiepagina_nl.php",
		"http://forum.indahnesia.com/forum/27/0/selamat_makan_-_smakelijk_eten.php",
		"http://forum.indahnesia.com/forum/36/0/geloof_in_indonesi_euml.php",
		"http://forum.indahnesia.com/forum/33/0/in_het_nieuws.php",
		"http://forum.indahnesia.com/forum/32/0/gezocht_aangeboden.php",
		"http://forum.indahnesia.com/forum/28/0/andere_praat.php",
		"http://forum.indahnesia.com/forum/29/0/website_forum_informatie.php",
		"http://forum.indahnesia.com/forum/30/0/gebruikers_hebben_wat_te_zeggen.php"
        ]
	COUNTRY = "IDN"
	THREAD_XPATH = "//a[contains(@href,'/topic/') and @style='font-size: 14px;']"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "(//table[@style='margin-top: 3px; margin-bottom: 3px; margin-left: -2px;']//a)[last()]/@href"
	PREV_XPATH = "//table[@style='margin-top: 3px; margin-bottom: 3px; margin-left: -2px;']//td[contains(@style,'background-color: #808080')]/preceding::a[1]/@href"
	POST_XPATH = "(//td[@width='860']/table)[position()>3 and position()<count((//td[@width='860']/table))-4]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//a[contains(@title,'Post made')]/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//a[contains(@href,'/profile/')]//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//tr[2]//div[@class='spacing']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": "concat('http://forum.indahnesia.com/topic',substring-after((//a[contains(@href,'/post/reply/')]/@href)[1],'/post/reply'),substring-after((//a[@class='head'])[last()-1]/@href,'/0/'),'&#',./preceding-sibling::a[1]/@name)"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//a[@class='head' and contains(@href,'/topic/')]/text()"
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
