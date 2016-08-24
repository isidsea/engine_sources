from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "diendancacanh"
	CRAWLER_NAME = "diendancacanh crawler"
	LINK_TO_CRAWL = [
		"http://www.diendancacanh.com/forums/thong-bao.10/",
		"http://www.diendancacanh.com/forums/huong-dan-gop-y-thac-mac.62/",
		"http://www.diendancacanh.com/forums/tin-tuc.65/",
		"http://www.diendancacanh.com/forums/bai-viet.12/",
		"http://www.diendancacanh.com/forums/sach-tai-lieu.64/", 
		"http://www.diendancacanh.com/forums/hoi-nhom-cau-lac-bo.63/",
		"http://www.diendancacanh.com/forums/ha-noi-betta-club.77/",
		"http://www.diendancacanh.com/forums/saigon-sunday-betta-club.105/",
		"http://www.diendancacanh.com/forums/2011.189/",
		"http://www.diendancacanh.com/forums/betta-ba-ria-vung-tau.108/",
		"http://www.diendancacanh.com/forums/can-tho-betta-club.212/",
		"http://www.diendancacanh.com/forums/underworld-fancy-club.216/",
		"http://www.diendancacanh.com/forums/bai-viet-tuyen-chon-ca-betta.19/",
		"http://www.diendancacanh.com/forums/tong-hop-kinh-nghiem-ve-ca-betta.26/",
		"http://www.diendancacanh.com/forums/lai-tao-ca-betta.24/",
		"http://www.diendancacanh.com/forums/danh-gia-ca-betta.49/",
		"http://www.diendancacanh.com/forums/tong-hop-kinh-nghiem-ve-ca-da-ca-choi.58/",
		"http://www.diendancacanh.com/forums/bai-viet-tuyen-chon-ca-da-ca-choi.188/",
		"http://www.diendancacanh.com/forums/gallery-hinh-anh-ca-betta.25/",
		"http://www.diendancacanh.com/forums/mua-ban-trao-doi-ca-betta.28/",
		"http://www.diendancacanh.com/forums/clb-la-han-ha-noi.103/",
		"http://www.diendancacanh.com/forums/bai-viet-tuyen-chon-ca-la-han.86/",
		"http://www.diendancacanh.com/forums/tong-hop-kinh-nghiem-ve-ca-la-han.42/",
		"http://www.diendancacanh.com/forums/gallery-hinh-anh-ca-la-han.43/",
		"http://www.diendancacanh.com/forums/lai-tao-ca-la-han.46/",
		"http://www.diendancacanh.com/forums/mua-ban-trao-doi-ca-la-han.44/",
		"http://www.diendancacanh.com/forums/clb-ca-dia-sai-gon.132/",
		"http://www.diendancacanh.com/forums/clb-ca-dia-ha-noi.133/",
		"http://www.diendancacanh.com/forums/bai-viet-tuyen-chon-ca-dia.135/",
		"http://www.diendancacanh.com/forums/tong-hop-kinh-nghiem-ve-ca-dia.134/",
		"http://www.diendancacanh.com/forums/gallery-hinh-anh-ca-dia.87/",
		"http://www.diendancacanh.com/forums/mua-ban-trao-doi-ca-dia.52/",
		"http://www.diendancacanh.com/forums/bai-viet-tuyen-chon-ca-rong.106/",
		"http://www.diendancacanh.com/forums/tong-hop-kinh-nghiem-ve-ca-rong.36/",
		"http://www.diendancacanh.com/forums/he-thong-loc-va-xu-ly-nuoc-ca-rong.175/",
		"http://www.diendancacanh.com/forums/gallery-hinh-anh-ca-rong.37/",
		"http://www.diendancacanh.com/forums/mua-ban-trao-doi-ca-rong.38/",
		"http://www.diendancacanh.com/forums/hoi-hop-giao-luu-ca-bay-mau.167/",
		"http://www.diendancacanh.com/forums/saigon-guppy-club.264/",
		"http://www.diendancacanh.com/forums/bai-viet-tuyen-chon-ca-bay-mau.163/",
		"http://www.diendancacanh.com/forums/tong-hop-kinh-nghiem-ve-ca-bay-mau.164/",
		"http://www.diendancacanh.com/forums/gallery-hinh-anh-ca-bay-mau.165/",
		"http://www.diendancacanh.com/forums/mua-ban-trao-doi-ca-bay-mau.166/",
		"http://www.diendancacanh.com/forums/hoi-hop-giao-luu-ca-vang.194/",
		"http://www.diendancacanh.com/forums/saigon-goldfish-club.263/",
		"http://www.diendancacanh.com/forums/bai-viet-tuyen-chon-ca-vang-ca-chep.186/",
		"http://www.diendancacanh.com/forums/tong-hop-kinh-nghiem-ve-ca-vang-ca-chep.140/",
		"http://www.diendancacanh.com/forums/gallery-hinh-anh-ve-ca-vang-ca-chep.185/",
		"http://www.diendancacanh.com/forums/mua-ban-trao-doi-ca-vang-ca-chep.191/",
		"http://www.diendancacanh.com/forums/bai-viet-tuyen-chon-ca-cichlid.299/",
		"http://www.diendancacanh.com/forums/tong-hop-kinh-nghiem-ve-ca-cichlid.300/",
		"http://www.diendancacanh.com/forums/gallery-hinh-anh-ca-cichlid.301/",
		"http://www.diendancacanh.com/forums/mua-ban-trao-doi-ca-cichlid.302/",
		"http://www.diendancacanh.com/forums/bai-viet-tuyen-chon-ga.171/",
		"http://www.diendancacanh.com/forums/tong-hop-kinh-nghiem-ve-ga.172/",
		"http://www.diendancacanh.com/forums/gallery-hinh-anh-ve-ga.173/",
		"http://www.diendancacanh.com/forums/mua-ban-trao-doi-ga.174/",
		"http://www.diendancacanh.com/forums/bai-viet-tuyen-chon-chim.218/",
		"http://www.diendancacanh.com/forums/tong-hop-kinh-nghiem-ve-chim.219/",
		"http://www.diendancacanh.com/forums/gallery-hinh-anh-ve-chim.220/",
		"http://www.diendancacanh.com/forums/mua-ban-trao-doi-chim.221/",
		"http://www.diendancacanh.com/forums/sinh-vat-canh.5/",
		"http://www.diendancacanh.com/forums/ca-canh.2/",
		"http://www.diendancacanh.com/forums/sinh_vat_canh.109/",
		"http://www.diendancacanh.com/forums/gallery-hinh-anh.15/",
		"http://www.diendancacanh.com/forums/mua-ban-trao-doi-sinh-vat-canh-phu-kien.17/",
		"http://www.diendancacanh.com/forums/bai-viet-tuyen-chon-thuy-sinh.110/",
		"http://www.diendancacanh.com/forums/tong-hop-kinh-nghiem-ve-thuy-sinh.55/",
		"http://www.diendancacanh.com/forums/hoi-dap-ve-thuy-sinh.60/",
		"http://www.diendancacanh.com/forums/gallery-hinh-anh-ve-thuy-sinh.56/",
		"http://www.diendancacanh.com/forums/ho-cua-thanh-vien.107/",
		"http://www.diendancacanh.com/forums/mua-ban-trao-doi-ve-thuy-sinh.57/",
		"http://www.diendancacanh.com/forums/dau-gia.192/",
		"http://www.diendancacanh.com/forums/tan-man.13/",
		"http://www.diendancacanh.com/forums/vui-cuoi-24-7.90/",
		"http://www.diendancacanh.com/forums/goc-cong-nghe.318/",
		"http://www.diendancacanh.com/forums/tranh-cai.297/"
        ]
	COUNTRY = "VNM"
	THREAD_XPATH = "//li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//a[@class='PreviewTooltip']/@href"	
	LAST_PAGE_XPATH = "(//div[@class='PageNav']//a[not(contains(text(),'>'))])[last()]/@href"
	PREV_XPATH = "//div[@class='PageNav']//a[contains(text(),'<')]/@href"
	POST_XPATH = "//ol[@id='messageList']//li[re:test(@id,'post-*')]"
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
			"xpath": ".//a[@class='username']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='messageContent']//text()"
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
			"xpath":"//div[@class='titleBar']//h1//text()"
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
