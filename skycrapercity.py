from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "skyscrapercity"
	CRAWLER_NAME = "Skyscrapercity Crawler"
	LINK_TO_CRAWL = [
		"http://www.skyscrapercity.com/forumdisplay.php?f=4070",
		"http://www.skyscrapercity.com/forumdisplay.php?f=902",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1718",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1720",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1728",
		"http://www.skyscrapercity.com/forumdisplay.php?f=903",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1724",
		"http://www.skyscrapercity.com/forumdisplay.php?f=904",
		"http://www.skyscrapercity.com/forumdisplay.php?f=905",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3252",
		"http://www.skyscrapercity.com/forumdisplay.php?f=607",
		"http://www.skyscrapercity.com/forumdisplay.php?f=4",
		"http://www.skyscrapercity.com/forumdisplay.php?f=440",
		"http://www.skyscrapercity.com/forumdisplay.php?f=192",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2086",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3254",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3215",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3253",
		"http://www.skyscrapercity.com/forumdisplay.php?f=263",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1732",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1734",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1736",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3854",
		"http://www.skyscrapercity.com/forumdisplay.php?f=89",
		"http://www.skyscrapercity.com/forumdisplay.php?f=115",
		"http://www.skyscrapercity.com/forumdisplay.php?f=158",
		"http://www.skyscrapercity.com/forumdisplay.php?f=294",
		"http://www.skyscrapercity.com/forumdisplay.php?f=422",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1584",
		"http://www.skyscrapercity.com/forumdisplay.php?f=162",
		"http://www.skyscrapercity.com/forumdisplay.php?f=327",
		"http://www.skyscrapercity.com/forumdisplay.php?f=9",
		"http://www.skyscrapercity.com/forumdisplay.php?f=468",
		"http://www.skyscrapercity.com/forumdisplay.php?f=7",
		"http://www.skyscrapercity.com/forumdisplay.php?f=128",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3544",
		"http://www.skyscrapercity.com/forumdisplay.php?f=438",
		"http://www.skyscrapercity.com/forumdisplay.php?f=129",
		"http://www.skyscrapercity.com/forumdisplay.php?f=4032",
		"http://www.skyscrapercity.com/forumdisplay.php?f=4043",
		"http://www.skyscrapercity.com/forumdisplay.php?f=812",
		"http://www.skyscrapercity.com/forumdisplay.php?f=130",
		"http://www.skyscrapercity.com/forumdisplay.php?f=813",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1088",
		"http://www.skyscrapercity.com/forumdisplay.php?f=504",
		"http://www.skyscrapercity.com/forumdisplay.php?f=8",
		"http://www.skyscrapercity.com/forumdisplay.php?f=103",
		"http://www.skyscrapercity.com/forumdisplay.php?f=431",
		"http://www.skyscrapercity.com/forumdisplay.php?f=283",
		"http://www.skyscrapercity.com/forumdisplay.php?f=843",
		"http://www.skyscrapercity.com/forumdisplay.php?f=104",
		"http://www.skyscrapercity.com/forumdisplay.php?f=346",
		"http://www.skyscrapercity.com/forumdisplay.php?f=513",
		"http://www.skyscrapercity.com/forumdisplay.php?f=427",
		"http://www.skyscrapercity.com/forumdisplay.php?f=105",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3031",
		"http://www.skyscrapercity.com/forumdisplay.php?f=879",
		"http://www.skyscrapercity.com/forumdisplay.php?f=842",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3730",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3361",
		"http://www.skyscrapercity.com/forumdisplay.php?f=331",
		"http://www.skyscrapercity.com/forumdisplay.php?f=390",
		"http://www.skyscrapercity.com/forumdisplay.php?f=428",
		"http://www.skyscrapercity.com/forumdisplay.php?f=429",
		"http://www.skyscrapercity.com/forumdisplay.php?f=65",
		"http://www.skyscrapercity.com/forumdisplay.php?f=191",
		"http://www.skyscrapercity.com/forumdisplay.php?f=4056",
		"http://www.skyscrapercity.com/forumdisplay.php?f=372",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1476",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1479",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2345",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2971",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2098",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2206",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2875",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2146",
		"http://www.skyscrapercity.com/forumdisplay.php?f=701",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2939",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1474",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3389",
		"http://www.skyscrapercity.com/forumdisplay.php?f=378",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2204",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3178",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1478",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2873",
		"http://www.skyscrapercity.com/forumdisplay.php?f=37",
		"http://www.skyscrapercity.com/forumdisplay.php?f=476",
		"http://www.skyscrapercity.com/forumdisplay.php?f=248",
		"http://www.skyscrapercity.com/forumdisplay.php?f=597",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2427",
		"http://www.skyscrapercity.com/forumdisplay.php?f=927",
		"http://www.skyscrapercity.com/forumdisplay.php?f=629",
		"http://www.skyscrapercity.com/forumdisplay.php?f=694",
		"http://www.skyscrapercity.com/forumdisplay.php?f=559",
		"http://www.skyscrapercity.com/forumdisplay.php?f=641",
		"http://www.skyscrapercity.com/forumdisplay.php?f=377",		
		"http://www.skyscrapercity.com/forumdisplay.php?f=1010",
		"http://www.skyscrapercity.com/forumdisplay.php?f=583",
		"http://www.skyscrapercity.com/forumdisplay.php?f=95",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3574",
		"http://www.skyscrapercity.com/forumdisplay.php?f=928",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2517",
		"http://www.skyscrapercity.com/forumdisplay.php?f=305",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3371",
		"http://www.skyscrapercity.com/forumdisplay.php?f=403",
		"http://www.skyscrapercity.com/forumdisplay.php?f=353",
		"http://www.skyscrapercity.com/forumdisplay.php?f=404",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3372",
		"http://www.skyscrapercity.com/forumdisplay.php?f=278",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1054",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3618",
		"http://www.skyscrapercity.com/forumdisplay.php?f=451",
		"http://www.skyscrapercity.com/forumdisplay.php?f=333",
		"http://www.skyscrapercity.com/forumdisplay.php?f=759",
		"http://www.skyscrapercity.com/forumdisplay.php?f=405",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3617",
		"http://www.skyscrapercity.com/forumdisplay.php?f=295",		
		"http://www.skyscrapercity.com/forumdisplay.php?f=766",
		"http://www.skyscrapercity.com/forumdisplay.php?f=585",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3365",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3366",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3367",
		"http://www.skyscrapercity.com/forumdisplay.php?f=733",
		"http://www.skyscrapercity.com/forumdisplay.php?f=586",
		"http://www.skyscrapercity.com/forumdisplay.php?f=872",
		"http://www.skyscrapercity.com/forumdisplay.php?f=450",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2232",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1228",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1229",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1370",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1230",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1232",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1233",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1234",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2236",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1372",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1236",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3120",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3039",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3043",
		"http://www.skyscrapercity.com/forumdisplay.php?f=542",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1247",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1256",
		"http://www.skyscrapercity.com/forumdisplay.php?f=541",
		"http://www.skyscrapercity.com/forumdisplay.php?f=491",
		"http://www.skyscrapercity.com/forumdisplay.php?f=402",
		"http://www.skyscrapercity.com/forumdisplay.php?f=326",
		"http://www.skyscrapercity.com/forumdisplay.php?f=588",
		"http://www.skyscrapercity.com/forumdisplay.php?f=164",
		"http://www.skyscrapercity.com/forumdisplay.php?f=332",
		"http://www.skyscrapercity.com/forumdisplay.php?f=363",
		"http://www.skyscrapercity.com/forumdisplay.php?f=926",
		"http://www.skyscrapercity.com/forumdisplay.php?f=606",
		"http://www.skyscrapercity.com/forumdisplay.php?f=364",
		"http://www.skyscrapercity.com/forumdisplay.php?f=669",
		"http://www.skyscrapercity.com/forumdisplay.php?f=925",
		"http://www.skyscrapercity.com/forumdisplay.php?f=365",
		"http://www.skyscrapercity.com/forumdisplay.php?f=133",
		"http://www.skyscrapercity.com/forumdisplay.php?f=391",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1974",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1338",
		"http://www.skyscrapercity.com/forumdisplay.php?f=272",
		"http://www.skyscrapercity.com/forumdisplay.php?f=550",
		"http://www.skyscrapercity.com/forumdisplay.php?f=551",
		"http://www.skyscrapercity.com/forumdisplay.php?f=910",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2004",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1340",
		"http://www.skyscrapercity.com/forumdisplay.php?f=882",
		"http://www.skyscrapercity.com/forumdisplay.php?f=822",
		"http://www.skyscrapercity.com/forumdisplay.php?f=883",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3577",
		"http://www.skyscrapercity.com/forumdisplay.php?f=261",
		"http://www.skyscrapercity.com/forumdisplay.php?f=884",
		"http://www.skyscrapercity.com/forumdisplay.php?f=808",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1342",
		"http://www.skyscrapercity.com/forumdisplay.php?f=552",
		"http://www.skyscrapercity.com/forumdisplay.php?f=945",
		"http://www.skyscrapercity.com/forumdisplay.php?f=944",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2002",
		"http://www.skyscrapercity.com/forumdisplay.php?f=975",
		"http://www.skyscrapercity.com/forumdisplay.php?f=553",
		"http://www.skyscrapercity.com/forumdisplay.php?f=391",		
		"http://www.skyscrapercity.com/forumdisplay.php?f=746",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3693",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1009",
		"http://www.skyscrapercity.com/forumdisplay.php?f=272",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1602",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1109",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1111",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1113",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1115",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1117",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1119",
		"http://www.skyscrapercity.com/forumdisplay.php?f=550",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1387",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3700",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1388",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3701",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1390",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3702",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1391",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3708",
		"http://www.skyscrapercity.com/forumdisplay.php?f=966",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1397",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3706",
		"http://www.skyscrapercity.com/forumdisplay.php?f=551",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3550",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3549",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3551",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3548",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1149",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1147",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1146",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1148",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3547",
		"http://www.skyscrapercity.com/forumdisplay.php?f=26",
		"http://www.skyscrapercity.com/forumdisplay.php?f=521",
		"http://www.skyscrapercity.com/forumdisplay.php?f=523",
		"http://www.skyscrapercity.com/forumdisplay.php?f=522",
		"http://www.skyscrapercity.com/forumdisplay.php?f=602",
		"http://www.skyscrapercity.com/forumdisplay.php?f=524",
		"http://www.skyscrapercity.com/forumdisplay.php?f=656",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3455",
		"http://www.skyscrapercity.com/forumdisplay.php?f=80",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2365",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3402",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3403",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3404",
		"http://www.skyscrapercity.com/forumdisplay.php?f=552",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2671",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2673",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2675",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2723",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2725",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2669",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1320",
		"http://www.skyscrapercity.com/forumdisplay.php?f=975",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1330",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1624",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2072",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2953",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2066",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2068",
		"http://www.skyscrapercity.com/forumdisplay.php?f=553",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1073",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1544",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1546",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1970",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1972",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3152",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3154",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1074",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1075",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1542",		
		"http://www.skyscrapercity.com/forumdisplay.php?f=1346",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3552",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1930",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1436",
		"http://www.skyscrapercity.com/forumdisplay.php?f=409",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1129",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1358",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2839",
		"http://www.skyscrapercity.com/forumdisplay.php?f=494",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1364",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1376",
		"http://www.skyscrapercity.com/forumdisplay.php?f=75",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1284",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1135",
		"http://www.skyscrapercity.com/forumdisplay.php?f=684",
		"http://www.skyscrapercity.com/forumdisplay.php?f=488",
		"http://www.skyscrapercity.com/forumdisplay.php?f=474",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1282",
		"http://www.skyscrapercity.com/forumdisplay.php?f=29",
		"http://www.skyscrapercity.com/forumdisplay.php?f=729",
		"http://www.skyscrapercity.com/forumdisplay.php?f=335",
		"http://www.skyscrapercity.com/forumdisplay.php?f=336",
		"http://www.skyscrapercity.com/forumdisplay.php?f=380",
		"http://www.skyscrapercity.com/forumdisplay.php?f=447",
		"http://www.skyscrapercity.com/forumdisplay.php?f=647",
		"http://www.skyscrapercity.com/forumdisplay.php?f=492",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1596",
		"http://www.skyscrapercity.com/forumdisplay.php?f=59",
		"http://www.skyscrapercity.com/forumdisplay.php?f=218",
		"http://www.skyscrapercity.com/forumdisplay.php?f=58",
		"http://www.skyscrapercity.com/forumdisplay.php?f=32",
		"http://www.skyscrapercity.com/forumdisplay.php?f=866",
		"http://www.skyscrapercity.com/forumdisplay.php?f=867",
		"http://www.skyscrapercity.com/forumdisplay.php?f=868",
		"http://www.skyscrapercity.com/forumdisplay.php?f=968",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1199",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3774",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3926",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3940",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3941",
		"http://www.skyscrapercity.com/forumdisplay.php?f=12",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1295",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1814",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1816",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1374",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1818",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1297",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3457",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2020",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2309",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2198",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2309",
		"http://www.skyscrapercity.com/forumdisplay.php?f=45",
		"http://www.skyscrapercity.com/forumdisplay.php?f=51",
		"http://www.skyscrapercity.com/forumdisplay.php?f=323",
		"http://www.skyscrapercity.com/forumdisplay.php?f=314",
		"http://www.skyscrapercity.com/forumdisplay.php?f=819",
		"http://www.skyscrapercity.com/forumdisplay.php?f=820",
		"http://www.skyscrapercity.com/forumdisplay.php?f=829",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1097",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3205",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2449",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3209",
		"http://www.skyscrapercity.com/forumdisplay.php?f=833",
		"http://www.skyscrapercity.com/forumdisplay.php?f=832",
		"http://www.skyscrapercity.com/forumdisplay.php?f=834",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1025",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3568",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3590",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3591",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3569",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3717",
		"http://www.skyscrapercity.com/forumdisplay.php?f=169",
		"http://www.skyscrapercity.com/forumdisplay.php?f=345",
		"http://www.skyscrapercity.com/forumdisplay.php?f=417",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1016",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1014",
		"http://www.skyscrapercity.com/forumdisplay.php?f=439",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1056",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1132",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2032",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1133",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2078",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2080",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2082",
		"http://www.skyscrapercity.com/forumdisplay.php?f=739",		
		"http://www.skyscrapercity.com/forumdisplay.php?f=2849",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2851",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2513",
		"http://www.skyscrapercity.com/forumdisplay.php?f=634",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2485",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2375",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2373",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2377",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1291",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1976",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1978",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2250",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1980",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3938",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2248",
		"http://www.skyscrapercity.com/forumdisplay.php?f=4031",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1982",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1988",
		"http://www.skyscrapercity.com/forumdisplay.php?f=1984",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2056",
		"http://www.skyscrapercity.com/forumdisplay.php?f=307",
		"http://www.skyscrapercity.com/forumdisplay.php?f=456",
		"http://www.skyscrapercity.com/forumdisplay.php?f=807",
		"http://www.skyscrapercity.com/forumdisplay.php?f=2120",
		"http://www.skyscrapercity.com/forumdisplay.php?f=348",
		"http://www.skyscrapercity.com/forumdisplay.php?f=298",
		"http://www.skyscrapercity.com/forumdisplay.php?f=652",
		"http://www.skyscrapercity.com/forumdisplay.php?f=3519",
		"http://www.skyscrapercity.com/forumdisplay.php?f=25",		
		"http://www.skyscrapercity.com/forumdisplay.php?f=454"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//tbody[re:test(@id,'threadbits_forum_*')]/tr"
	THREAD_LINK_XPATH = ".//a[re:test(@id,'thread_title_*')]/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagenav']//td[@class='vbmenu_control'])[last()]//preceding::a[re:test(@title,'Last Page*') or re:test(@title,'Show results*')][1]/@href"
	PREV_XPATH = "//div[@class='pagenav']//a[@rel='prev']/@href"
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
			"xpath": "concat(.//a[@class='bigusername']//text(),.//div[re:test(@id,'postmenu_*')]//text())"
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
			"xpath": ".//a[re:test(@id,'postcount*')]/@href"
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
                        "exception":'"content is not defined"'
                },
                "has_to_have_published_date":{
                        "condition":'"published_date" in document',
                        "exception":'"published_date is not defined"'
                },
                "has_to_have_title":{
                        "condition":'"title" in document',
                        "exception":'"title is not defined"'
                },
                "has_to_have_author_name":{
                        "condition":'"author_name" in document',
                        "exception":'"author_name is not defined"'
                },
                "has_to_have_permalink":{
                        "condition":'"permalink" in document',
                        "exception":'"permalink is not defined"'
                },
                "content_cannot_be_empty":{
                        "condition":'len(document["content"]) > 0',
                        "exception":'"content cannot be empty"'
                },
                "published_date_cannot_be_empty":{
                        "condition":'document["published_date"] is not None',
                        "exception":'"published_date cannot be empty"'
                },
                "title_cannot_be_empty":{
                        "condition":'len(document["title"]) > 0',
                        "exception":'"title cannot be empty"'
                },
                "author_name_cannot_be_empty":{
                        "condition":'len(document["author_name"]) > 0',
                        "exception":'"author_name cannot be empty"'
                },
                "permalink_cannot_be_empty":{
                        "condition":'len(document["permalink"]) > 0',
                        "exception":'"permalink cannot be empty"'
                },
        }
#end class
