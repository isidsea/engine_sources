from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "gourmetindia"
	CRAWLER_NAME = "gourmetindia crawler"
	LINK_TO_CRAWL = [
		"http://www.gourmetindia.com/forum/8-gourmet-india-rules/",
		"http://www.gourmetindia.com/forum/15-news-media-gourmet-food-wine/",
		"http://www.gourmetindia.com/forum/16-gourmet-india-members-only/",
		"http://www.gourmetindia.com/forum/39-nostalgia/",
		"http://www.gourmetindia.com/forum/5-indian-cuisine/",
		"http://www.gourmetindia.com/forum/6-global-cuisine/",
		"http://www.gourmetindia.com/forum/7-chefs/",
		"http://www.gourmetindia.com/forum/12-restaurant-reviews/",
		"http://www.gourmetindia.com/forum/17-gdf/",
		"http://www.gourmetindia.com/forum/18-food-photo-blog/",
		"http://www.gourmetindia.com/forum/9-anything-else/",
		"http://www.gourmetindia.com/forum/25-recipes/",
		"http://www.gourmetindia.com/forum/27-pubs-and-bars-digest/",
		"http://www.gourmetindia.com/forum/28-cooking-videos/",
		"http://www.gourmetindia.com/forum/47-food-issues-and-concerns/",
		"http://www.gourmetindia.com/forum/2-whisky/",
		"http://www.gourmetindia.com/forum/49-amrut-whisky/",
		"http://www.gourmetindia.com/forum/10-wine/",
		"http://www.gourmetindia.com/forum/4-spirits/",
		"http://www.gourmetindia.com/forum/26-cocktail-recipes/",
		"http://www.gourmetindia.com/forum/23-desserts/",
		"http://www.gourmetindia.com/forum/33-mithai-indian-sweets/",
		"http://www.gourmetindia.com/forum/30-non-food/",
		"http://www.gourmetindia.com/forum/54-general-chat-about-travel-in-india/",
		"http://www.gourmetindia.com/forum/189-meals-tiffin-and-chai/",
		"http://www.gourmetindia.com/forum/225-phones-internet-amp-radio/",
		"http://www.gourmetindia.com/forum/247-money/",
		"http://www.gourmetindia.com/forum/226-public-holidays-in-india/",
		"http://www.gourmetindia.com/forum/129-cultural-tips-amp-etiquette/",
		"http://www.gourmetindia.com/forum/167-it-can-happen-only-in-india33/",
		"http://www.gourmetindia.com/forum/128-indians-away-from-home/",
		"http://www.gourmetindia.com/forum/280-the-weather/",
		"http://www.gourmetindia.com/forum/287-youtube-videos/",
		"http://www.gourmetindia.com/forum/228-members39-area/",
		"http://www.gourmetindia.com/forum/131-thetravelswami-forum/",
		"http://www.gourmetindia.com/forum/127-general-chit-chat/",
		"http://www.gourmetindia.com/forum/66-who-are-you/",
		"http://www.gourmetindia.com/forum/190-jokes-and-fun/",
		"http://www.gourmetindia.com/forum/169-happy-birthday-to-you33/",
		"http://www.gourmetindia.com/forum/191-meetups/",
		"http://www.gourmetindia.com/forum/229-what-are-you-listening-to-now/",
		"http://www.gourmetindia.com/forum/80-agra/",
		"http://www.gourmetindia.com/forum/255-ahmedabad/",
		"http://www.gourmetindia.com/forum/77-bangalore/",
		"http://www.gourmetindia.com/forum/78-chennai/",
		"http://www.gourmetindia.com/forum/74-new-delhi/",
		"http://www.gourmetindia.com/forum/79-hyderabad/",
		"http://www.gourmetindia.com/forum/248-jaipur/",
		"http://www.gourmetindia.com/forum/76-kolkata/",
		"http://www.gourmetindia.com/forum/82-ladakh/",
		"http://www.gourmetindia.com/forum/75-mumbai/",
		"http://www.gourmetindia.com/forum/81-varanasi/",
		"http://www.gourmetindia.com/forum/83-all-the-indian-states/",
		"http://www.gourmetindia.com/forum/107-andhra-pradesh/",
		"http://www.gourmetindia.com/forum/108-gujarat/",
		"http://www.gourmetindia.com/forum/109-himachal-pradesh/",
		"http://www.gourmetindia.com/forum/110-jammu-amp-kashmir/",
		"http://www.gourmetindia.com/forum/196-jharkhand/",
		"http://www.gourmetindia.com/forum/111-karnataka/",
		"http://www.gourmetindia.com/forum/112-kerala/",
		"http://www.gourmetindia.com/forum/113-ladakh-amp-zanskar/",
		"http://www.gourmetindia.com/forum/114-madhya-pradesh-amp-chattisgarh/",
		"http://www.gourmetindia.com/forum/115-maharashtra/",
		"http://www.gourmetindia.com/forum/116-orissa/",
		"http://www.gourmetindia.com/forum/117-punjab-amp-haryana/",
		"http://www.gourmetindia.com/forum/118-rajasthan/",
		"http://www.gourmetindia.com/forum/119-sikkim/",
		"http://www.gourmetindia.com/forum/120-tamil-nadu/",
		"http://www.gourmetindia.com/forum/121-uttar-pradesh-amp-uttaranchal/",
		"http://www.gourmetindia.com/forum/122-west-bengal/",
		"http://www.gourmetindia.com/forum/123-the-north-eastern-states/",
		"http://www.gourmetindia.com/forum/124-all-other-areas/",
		"http://www.gourmetindia.com/forum/178-goa/",
		"http://www.gourmetindia.com/forum/179-getting-there/",
		"http://www.gourmetindia.com/forum/180-hotels/",
		"http://www.gourmetindia.com/forum/181-restaurants/",
		"http://www.gourmetindia.com/forum/182-beaches/",
		"http://www.gourmetindia.com/forum/184-places-to-visit/",
		"http://www.gourmetindia.com/forum/185-entertainment/",
		"http://www.gourmetindia.com/forum/186-shopping-amp-markets/",
		"http://www.gourmetindia.com/forum/187-hiring-a-two-wheeler/",
		"http://www.gourmetindia.com/forum/188-everything-else/",
		"http://www.gourmetindia.com/forum/230-real-estate-in-goa/",
		"http://www.gourmetindia.com/forum/92-activities-sightseeing-amp-trekking/",
		"http://www.gourmetindia.com/forum/95-wildlife-amp-national-parks/",
		"http://www.gourmetindia.com/forum/96-trekking-amp-mountaineering/",
		"http://www.gourmetindia.com/forum/97-off-the-beaten-track/",
		"http://www.gourmetindia.com/forum/98-sporting-holidays/",
		"http://www.gourmetindia.com/forum/84-islands-amp-neighbouring-countries/",
		"http://www.gourmetindia.com/forum/106-andaman-amp-nicobar-islands/",
		"http://www.gourmetindia.com/forum/295-bangladesh/",
		"http://www.gourmetindia.com/forum/88-bhutan/",
		"http://www.gourmetindia.com/forum/183-burma-myanmar/",
		"http://www.gourmetindia.com/forum/91-lakshadweep/",
		"http://www.gourmetindia.com/forum/90-maldives/",
		"http://www.gourmetindia.com/forum/86-nepal/",
		"http://www.gourmetindia.com/forum/85-pakistan/",
		"http://www.gourmetindia.com/forum/87-sri-lanka/",
		"http://www.gourmetindia.com/forum/89-tibet/",
		"http://www.gourmetindia.com/forum/55-transport-amp-travel/",
		"http://www.gourmetindia.com/forum/56-air-travel/",
		"http://www.gourmetindia.com/forum/57-rail/",
		"http://www.gourmetindia.com/forum/58-car/",
		"http://www.gourmetindia.com/forum/289-bus-travel/",
		"http://www.gourmetindia.com/forum/59-rickshaws/",
		"http://www.gourmetindia.com/forum/60-sea/",
		"http://www.gourmetindia.com/forum/61-2-wheelers/",
		"http://www.gourmetindia.com/forum/278-maps/",
		"http://www.gourmetindia.com/forum/279-google-earth-placemarks/",
		"http://www.gourmetindia.com/forum/227-news/",
		"http://www.gourmetindia.com/forum/231-travelers-gone-missing-in-india/",
		"http://www.gourmetindia.com/forum/69-photography/",
		"http://www.gourmetindia.com/forum/293-where-is-this-what-is-this/",
		"http://www.gourmetindia.com/forum/63-passports-amp-visas/",
		"http://www.gourmetindia.com/forum/64-packing-your-bags33/",
		"http://www.gourmetindia.com/forum/268-telephone-internet-cable-amp-tv/",
		"http://www.gourmetindia.com/forum/65-scams-touts-amp-beggars/",
		"http://www.gourmetindia.com/forum/67-yoga-religion-spiritual/",
		"http://www.gourmetindia.com/forum/68-volunteering-amp-charity-work/",
		"http://www.gourmetindia.com/forum/132-sports/",
		"http://www.gourmetindia.com/forum/93-plan-your-itinerary/",
		"http://www.gourmetindia.com/forum/94-travel-partners/",
		"http://www.gourmetindia.com/forum/62-health-amp-well-being/",
		"http://www.gourmetindia.com/forum/285-ayurveda/",
		"http://www.gourmetindia.com/forum/282-dentists-amp-dental-treatment/",
		"http://www.gourmetindia.com/forum/286-health-tips/",
		"http://www.gourmetindia.com/forum/281-spectacles-amp-contact-lenses/",
		"http://www.gourmetindia.com/forum/284-malaria-tablets-amp-mosquitos/",
		"http://www.gourmetindia.com/forum/283-vaccinations/",
		"http://www.gourmetindia.com/forum/105-literary-fine-arts-movies-amp-music/",
		"http://www.gourmetindia.com/forum/70-books/",
		"http://www.gourmetindia.com/forum/288-online-books/",
		"http://www.gourmetindia.com/forum/71-music/",
		"http://www.gourmetindia.com/forum/72-movies/",
		"http://www.gourmetindia.com/forum/130-fine-arts/",
		"http://www.gourmetindia.com/forum/294-tv/",
		"http://www.gourmetindia.com/forum/297-misc-travel-discussions/"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//div[@class='ipsBox']//li[@itemprop='itemListElement']"
	THREAD_LINK_XPATH = ".//div[@class='ipsDataItem_main']/h4//a[@itemprop='url']/@href"
	LAST_PAGE_XPATH = "//li[@class='ipsPagination_last']/a/@href"
	PREV_XPATH = "//li[@class='ipsPagination_prev']/a/@href"
	POST_XPATH = "//article[re:test(@id,'elComment_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//time/@title"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//h3//a/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@data-role='commentContent']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[@class='ipsType_blendLinks']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//h1[@class='ipsType_pageTitle ipsContained_container']/div//text()"
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
