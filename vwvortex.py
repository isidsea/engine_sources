from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "vwvortex"
	CRAWLER_NAME = "vwvortex crawler"
	LINK_TO_CRAWL = [
		"http://forums.vwvortex.com/forumdisplay.php?5001-VW-Model-Specific-Forums",
		"http://forums.vwvortex.com/forumdisplay.php?17-The-Volkswagen-Lounge",
		"http://forums.vwvortex.com/forumdisplay.php?1080-VW-Motorsport",
		"http://forums.vwvortex.com/forumdisplay.php?9-Air-cooled",
		"http://forums.vwvortex.com/forumdisplay.php?152-Cabriolet",
		"http://forums.vwvortex.com/forumdisplay.php?1062-CC",
		"http://forums.vwvortex.com/forumdisplay.php?8-Corrado",
		"http://forums.vwvortex.com/forumdisplay.php?1149-Dasher-and-Quantum",
		"http://forums.vwvortex.com/forumdisplay.php?786-Eos",
		"http://forums.vwvortex.com/forumdisplay.php?71-Fox",
		"http://forums.vwvortex.com/forumdisplay.php?11-Golf-I-amp-Jetta-I",
		"http://forums.vwvortex.com/forumdisplay.php?2-Golf-II-amp-Jetta-II",
		"http://forums.vwvortex.com/forumdisplay.php?3-Golf-III-amp-Jetta-III",
		"http://forums.vwvortex.com/forumdisplay.php?4-Golf-IV-amp-Jetta-IV",
		"http://forums.vwvortex.com/forumdisplay.php?25-GTI-337-20th-Anniversary-Jetta-GLI-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?145-Golf-IV-R32",
		"http://forums.vwvortex.com/forumdisplay.php?142-Golf-V-amp-Jetta-V",
		"http://forums.vwvortex.com/forumdisplay.php?5292-Golf-V-amp-Jetta-V-Vendor-Marketplace",
		"http://forums.vwvortex.com/forumdisplay.php?865-Golf-V-R32",
		"http://forums.vwvortex.com/forumdisplay.php?1136-Golf-GTI-VI",
		"http://forums.vwvortex.com/forumdisplay.php?5288-Golf-GTI-VI-Vendor-Marketplace",
		"http://forums.vwvortex.com/forumdisplay.php?1190-Golf-VI-R",
		"http://forums.vwvortex.com/forumdisplay.php?5325-Golf-GTI-VII",
		"http://forums.vwvortex.com/forumdisplay.php?5376-eGolf-VII",
		"http://forums.vwvortex.com/forumdisplay.php?5378-Golf-SportWagen-VII",
		"http://forums.vwvortex.com/forumdisplay.php?5357-Golf-VII-R",
		"http://forums.vwvortex.com/forumdisplay.php?5311-Jetta-SportWagen",
		"http://forums.vwvortex.com/forumdisplay.php?5310-Jetta-GLI-VI",
		"http://forums.vwvortex.com/forumdisplay.php?67-Lupo",
		"http://forums.vwvortex.com/forumdisplay.php?5-New-Beetle-amp-New-Beetle-Convertible",
		"http://forums.vwvortex.com/forumdisplay.php?5309-The-Beetle",
		"http://forums.vwvortex.com/forumdisplay.php?971-New-Scirocco",
		"http://forums.vwvortex.com/forumdisplay.php?7-Passat-(B3-amp-B4)",
		"http://forums.vwvortex.com/forumdisplay.php?6-Passat-(B5)",
		"http://forums.vwvortex.com/forumdisplay.php?728-Passat-(B6)",
		"http://forums.vwvortex.com/forumdisplay.php?5301-Passat-(B7)",
		"http://forums.vwvortex.com/forumdisplay.php?112-Phaeton",
		"http://forums.vwvortex.com/forumdisplay.php?69-Polo",
		"http://forums.vwvortex.com/forumdisplay.php?1061-Routan",
		"http://forums.vwvortex.com/forumdisplay.php?13-Scirocco",
		"http://forums.vwvortex.com/forumdisplay.php?970-Tiguan",
		"http://forums.vwvortex.com/forumdisplay.php?39-Touareg",
		"http://forums.vwvortex.com/forumdisplay.php?33-Vans-and-Transporters-all-years",
		"http://forums.vwvortex.com/forumdisplay.php?5061-Audi-Model-Specific",
		"http://forums.vwvortex.com/forumdisplay.php?19-The-Audi-Lounge",
		"http://forums.vwvortex.com/forumdisplay.php?874-Audi-Sport",
		"http://forums.vwvortex.com/forumdisplay.php?960-European-Delivery",
		"http://forums.vwvortex.com/forumdisplay.php?5379-Audi-Exclusive",
		"http://forums.vwvortex.com/forumdisplay.php?1076-A1-S1-A2",
		"http://forums.vwvortex.com/forumdisplay.php?10-TT-(Mk1-a4-chassis)",
		"http://forums.vwvortex.com/forumdisplay.php?870-TT-TTS-amp-TTRS-(Mk2-a5-chassis)",
		"http://forums.vwvortex.com/forumdisplay.php?5356-TT-TTS-amp-TTRS-(MK3-MQB-Chassis)",
		"http://forums.vwvortex.com/forumdisplay.php?111-A3-amp-S3-(8L)",
		"http://forums.vwvortex.com/forumdisplay.php?548-A3-S3-RS-3-(8P)",
		"http://forums.vwvortex.com/forumdisplay.php?5319-A3-S3-RS-3-(MQB-8V)",
		"http://forums.vwvortex.com/forumdisplay.php?26-A4-S4-RS4-(B5)",
		"http://forums.vwvortex.com/forumdisplay.php?549-A4-S4-RS4-(B6-and-B7)",
		"http://forums.vwvortex.com/forumdisplay.php?1051-A4-S4-A5-S5-RS4-RS5-Q5-SQ5-(B8)",
		"http://forums.vwvortex.com/forumdisplay.php?5374-A4-S4-A5-S5-RS4-RS5-Q5-SQ5-(B9)",
		"http://forums.vwvortex.com/forumdisplay.php?571-allroad",
		"http://forums.vwvortex.com/forumdisplay.php?554-A6-amp-100-(C4)",
		"http://forums.vwvortex.com/forumdisplay.php?14-A6-S6-amp-RS6-(C5)",
		"http://forums.vwvortex.com/forumdisplay.php?572-A6-amp-S6-and-RS-6-(C6)",
		"http://forums.vwvortex.com/forumdisplay.php?5287-A6-S6-RS6-A7-S7-RS7-(C7)",
		"http://forums.vwvortex.com/forumdisplay.php?5307-Q3-SQ3-and-RSQ3",
		"http://forums.vwvortex.com/forumdisplay.php?741-Q7-1st-generation-(4L)",
		"http://forums.vwvortex.com/forumdisplay.php?5394-Q7-2nd-generation-(4M)",
		"http://forums.vwvortex.com/forumdisplay.php?555-A8-amp-S8-(All-Generations)",
		"http://forums.vwvortex.com/forumdisplay.php?772-R8-(All-Generations)",
		"http://forums.vwvortex.com/forumdisplay.php?1131-R8-Parts-Classifieds",
		"http://forums.vwvortex.com/forumdisplay.php?1132-R8-Cars-Classifieds",
		"http://forums.vwvortex.com/forumdisplay.php?557-5000-100-200-(C3)-amp-V8-(D1)",
		"http://forums.vwvortex.com/forumdisplay.php?559-4000-80-90-RS2-B2-B3-B4-Coupe-quattro-amp-Cabriolet-(B3-amp-B4-Small-Chassis-Vintage-Audi)",
		"http://forums.vwvortex.com/forumdisplay.php?560-Ur-S4-Ur-S6",
		"http://forums.vwvortex.com/forumdisplay.php?561-Ur-quattro-amp-Sport-quattro",
		"http://forums.vwvortex.com/forumdisplay.php?562-Vintage-Audi-Auto-Union-amp-NSU",
		"http://forums.vwvortex.com/forumdisplay.php?5003-Technical-(VW-Audi)",
		"http://forums.vwvortex.com/forumdisplay.php?32-Wheel-and-Tire-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?15-Suspension-Tuning",
		"http://forums.vwvortex.com/forumdisplay.php?1055-Air-Suspension",
		"http://forums.vwvortex.com/forumdisplay.php?115-Brakes",
		"http://forums.vwvortex.com/forumdisplay.php?148-Body-Work-Body-Styling-and-Body-Kits",
		"http://forums.vwvortex.com/forumdisplay.php?720-Interior",
		"http://forums.vwvortex.com/forumdisplay.php?1079-Oil-and-Lubrication",
		"http://forums.vwvortex.com/forumdisplay.php?510-VAG-COM-Diagnostic-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?12-Car-Audio-and-Electronics",
		"http://forums.vwvortex.com/forumdisplay.php?750-Portable-MP3-and-Satellite-Radio-OEM-Integration",
		"http://forums.vwvortex.com/forumdisplay.php?150-Preservation-and-Restoration",
		"http://forums.vwvortex.com/forumdisplay.php?22-TDI-and-Diesel-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?517-Carbs-ITBs-and-SEM-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?5410-1-4-TSI-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?27-1-8T-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?5293-1-8T-Vendor-Marketplace",
		"http://forums.vwvortex.com/forumdisplay.php?5360-1-8-TSI-(EA888-Gen-3)-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?5361-1-8-TSI-(EA888)-Vendor-Marketplace",
		"http://forums.vwvortex.com/forumdisplay.php?739-2-0T-FSI-TSI-and-TFSI-(EA113)-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?5290-2-0T-FSI-Vendor-Marketplace",
		"http://forums.vwvortex.com/forumdisplay.php?1081-2-0-TSI-and-TFSI-(EA888-Gen-1-and-Gen-2)-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?5291-2-0-TSI-and-TFSI-Vendor-Marketplace",
		"http://forums.vwvortex.com/forumdisplay.php?5358-2-0-TSI-and-TFSI-(EA888-Gen-3)-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?5359-2-0-TSI-(EA888)-Vendor-Marketplace",
		"http://forums.vwvortex.com/forumdisplay.php?740-2-5l-Inline-5-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?28-2-0-Liter-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?29-2-8l-12v-VR6-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?42-2-8l-24v-VR6-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?405-3-2l-24v-VR6-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?775-3-6l-24v-VR6-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?566-2-7T-V6-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?34-2-8l-V6-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?565-3-0l-V6-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?1129-3-0-TFSI-V6",
		"http://forums.vwvortex.com/forumdisplay.php?5321-4-0-TFSI-V8",
		"http://forums.vwvortex.com/forumdisplay.php?567-4-2l-V8-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?73-W8-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?35-16v-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?43-8v-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?36-G60-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?568-Inline-5-10v-amp-20v-Engine-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?574-Automatic-Transmission-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?988-DSG-and-S-tronic-Transmission-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?147-Manual-Transmission-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?742-Syncro-4motion-Quattro-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?38-Hybrid-Swap-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?113-Forced-Induction",
		"http://forums.vwvortex.com/forumdisplay.php?1148-Naturally-Aspirated",
		"http://forums.vwvortex.com/forumdisplay.php?114-Lighting",
		"http://forums.vwvortex.com/forumdisplay.php?715-Fabrication",
		"http://forums.vwvortex.com/forumdisplay.php?854-Tools-and-Machining",
		"http://forums.vwvortex.com/forumdisplay.php?968-Dyno-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?986-CIS-Injection",
		"http://forums.vwvortex.com/forumdisplay.php?1052-Motronic-Systems",
		"http://forums.vwvortex.com/forumdisplay.php?1138-Water-Alcohol-Methanol-Injection",		
		"http://forums.vwvortex.com/forumdisplay.php?5283-Deals-Group-Buys-and-New-Products",
		"http://forums.vwvortex.com/forumdisplay.php?5284-Deals-and-Specials-(Parts)",
		"http://forums.vwvortex.com/forumdisplay.php?5286-New-Products",		
		"http://forums.vwvortex.com/forumdisplay.php?5228-New-England-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5230-New-England-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5231-TriState-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5233-TriState-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5235-Mid-Atlantic-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5236-Mid-Atlantic-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5239-Capital-Area-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5240-Capital-Area-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5243-South-East-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5244-South-East-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5247-South-West-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5248-South-West-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5251-Midwest-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5252-Midwest-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5255-South-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5256-South-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5259-Nevada-and-Utah-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5260-Nevada-and-Utah-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5263-Rocky-Mountain-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5264-Rocky-Mountain-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5267-Pacific-Northwest-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5268-Pacific-Northwest-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5271-NorCal-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5272-NorCal-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5275-SoCal-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5276-SoCal-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5278-Hawaii-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5279-Hawaii-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?802-Golf-I-Jetta-I-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?807-Golf-I-Jetta-I-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?808-Golf-II-Jetta-II-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?809-Golf-II-Jetta-II-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?810-Golf-III-Jetta-III-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?811-Golf-III-Jetta-III-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?812-Golf-IV-Jetta-IV-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?813-Golf-IV-Jetta-IV-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?814-Golf-IV-R32-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?815-Golf-IV-R32-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?816-Golf-V-Jetta-V-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?817-Golf-V-Jetta-V-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5292-Golf-V-amp-Jetta-V-Vendor-Marketplace",		
		"http://forums.vwvortex.com/forumdisplay.php?1056-Golf-V-R32-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?1057-Golf-V-R32-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?1188-Golf-GTI-VI-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?1189-Golf-GTI-VI-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5288-Golf-VI-amp-Jetta-VI-Vendor-Marketplace",		
		"http://forums.vwvortex.com/forumdisplay.php?5323-Golf-R-(VI)-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5324-Golf-R-(VI)-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?5366-Golf-GTI-VII-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5367-Golf-GTI-VII-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5369-Golf-R-(VII)-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5370-Golf-R-(VII)-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5344-Jetta-SportWagen-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5345-Jetta-SportWagen-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?5313-Jetta-VI-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5314-Jetta-VI-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?984-Eos-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?985-Eos-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?818-Passat-B3-amp-B4-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?819-Passat-B3-amp-B4-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?820-Passat-B5-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?821-Passat-B5-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?822-Passat-B6-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?823-Passat-B6-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5317-Passat-B7-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5318-Passat-B7-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?1179-CC-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?1180-CC-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?1153-Dasher-and-Quantum-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?1152-Dasher-and-Quantum-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?824-New-Beetle-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?825-New-Beetle-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5333-Beetle-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5334-Beetle-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?1133-Phaeton-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?1135-Phaeton-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?826-Corrado-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?827-Corrado-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?828-Touareg-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?829-Touaregs",
		"http://forums.vwvortex.com/forumdisplay.php?1150-Tiguan-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?1151-Tiguans",
		"http://forums.vwvortex.com/forumdisplay.php?830-Vans-and-Transporters-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?831-Vans-and-Transporters-(Vehicles)",
		"http://forums.vwvortex.com/forumdisplay.php?1181-Routan-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?1182-Routan-Vans",
		"http://forums.vwvortex.com/forumdisplay.php?832-Scirocco-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?833-Scirocco-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?834-Fox-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?835-Fox-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?836-Cabriolet-and-Cabrio-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?837-Cabriolet-and-Cabrio-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?838-Aircooled-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?839-Aircooled-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?860-Diesel-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?861-Diesel-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?840-Miscellaneous-VW-Stuff",
		"http://forums.vwvortex.com/forumdisplay.php?879-Non-VW-Cars-For-Sale",
		"http://forums.vwvortex.com/forumdisplay.php?895-Cars-Parting-Out",
		"http://forums.vwvortex.com/forumdisplay.php?531-TT-Mk1-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?899-TT-Mk1-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?1049-TT-Mk2-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?1050-TT-Mk2-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5381-TT-Mk3-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5382-TT-Mk3-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?900-A3-and-S3-(8L)-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?901-A3-and-S3-(8L)-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?532-A3-S3-amp-RS3-(8P)-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?902-A3-S3-amp-RS3-(8P)-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?5363-A3-S3-RS3-(MQB-8V)-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5364-A3-S3-RS3-(MQB-8V)-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?529-A4-S4-and-RS4-(B5)-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?903-A4-S4-and-RS4-(B5)-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?530-A4-S4-amp-RS4-(B6-B7)-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?904-A4-S4-amp-RS4-(B6-B7)-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?1071-A4-S4-RS4-A5-S5-RS5-Q5-SQ5-(B8)-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?1072-A4-S4-RS4-A5-S5-RS5-Q5-SQ5-(B8)-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?908-100-A6-UrS4-amp-UrS6-(C4)-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?909-100-A6-UrS4-amp-UrS6-(C4)-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?533-A6-S6-and-RS6-(C5)-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?911-A6-S6-and-RS6-(C5)-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?912-A6-S6-amp-RS6-(C6)-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?913-A6-S6-amp-RS6-(C6)-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?5384-A6-S6-RS6-A7-S7-RS7-(C7)-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5385-A6-S6-RS6-A7-S7-RS7-(C7)-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?5372-Q3-SQ3-and-RSQ3-Parts",		
		"http://forums.vwvortex.com/forumdisplay.php?914-Q7-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?915-Q7-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?916-A8-and-S8-(All-Generations)-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?917-A8-and-S8-(All-Generations)-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5201-R8-Classifieds-(All-Generations)",
		"http://forums.vwvortex.com/forumdisplay.php?770-UrQuattro-and-Sport-Quattro-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?919-UrQuattro-and-Sport-Quattro-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?920-Small-Chassis-Audi-(B1-B2-B3-B4)-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?921-Small-Chassis-Audi-(B1-B2-B3-B4)-Cars",		
		"http://forums.vwvortex.com/forumdisplay.php?537-Vintage-Audi-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?924-Vintage-Audi-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5386-Wheel-amp-Tire-Classifieds",
		"http://forums.vwvortex.com/forumdisplay.php?5330-Spacers-Adapters-and-Wheel-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5002-Community-and-Lifestyle",
		"http://forums.vwvortex.com/forumdisplay.php?5224-Off-Topic",
		"http://forums.vwvortex.com/forumdisplay.php?514-Art-and-Design",
		"http://forums.vwvortex.com/forumdisplay.php?714-Aviation-and-Space",
		"http://forums.vwvortex.com/forumdisplay.php?725-Boat-and-Personal-Watercraft",
		"http://forums.vwvortex.com/forumdisplay.php?368-Books-and-Literature",
		"http://forums.vwvortex.com/forumdisplay.php?81-Camping-Hiking-and-Travel",
		"http://forums.vwvortex.com/forumdisplay.php?79-Computers",
		"http://forums.vwvortex.com/forumdisplay.php?78-Cycling",
		"http://forums.vwvortex.com/forumdisplay.php?140-Diecast-and-Model-Car",
		"http://forums.vwvortex.com/forumdisplay.php?119-Electronics-and-Gadgets",
		"http://forums.vwvortex.com/forumdisplay.php?371-Employment",
		"http://forums.vwvortex.com/forumdisplay.php?955-Fashion-and-Apparel",
		"http://forums.vwvortex.com/forumdisplay.php?719-Firearms-and-Hunting",
		"http://forums.vwvortex.com/forumdisplay.php?117-Food-and-Beverage",
		"http://forums.vwvortex.com/forumdisplay.php?743-Health-and-Fitness",
		"http://forums.vwvortex.com/forumdisplay.php?156-Home-Improvement",
		"http://forums.vwvortex.com/forumdisplay.php?729-Home-Theater",
		"http://forums.vwvortex.com/forumdisplay.php?713-Money-and-Investing",
		"http://forums.vwvortex.com/forumdisplay.php?105-Motorcycle-and-ATV",
		"http://forums.vwvortex.com/forumdisplay.php?75-Movies-and-Television",
		"http://forums.vwvortex.com/forumdisplay.php?102-Music",
		"http://forums.vwvortex.com/forumdisplay.php?864-Musical-Instruments-and-Pro-Audio-Gear",
		"http://forums.vwvortex.com/forumdisplay.php?989-Parenting-and-Family",
		"http://forums.vwvortex.com/forumdisplay.php?157-Pets",
		"http://forums.vwvortex.com/forumdisplay.php?82-Photography",
		"http://forums.vwvortex.com/forumdisplay.php?573-Radio-Control-Model-Car-(RC-Car)",
		"http://forums.vwvortex.com/forumdisplay.php?766-Ski-and-Snowboard",
		"http://forums.vwvortex.com/forumdisplay.php?77-Sports",
		"http://forums.vwvortex.com/forumdisplay.php?767-Surf-and-Skate",
		"http://forums.vwvortex.com/forumdisplay.php?983-Toys-and-Collectibles",
		"http://forums.vwvortex.com/forumdisplay.php?76-Video-Games",
		"http://forums.vwvortex.com/forumdisplay.php?962-Videography",
		"http://forums.vwvortex.com/forumdisplay.php?1130-Watches",
		"http://forums.vwvortex.com/forumdisplay.php?5080-The-Car-Lounge",
		"http://forums.vwvortex.com/forumdisplay.php?1-The-Car-Lounge",
		"http://forums.vwvortex.com/forumdisplay.php?959-4x4-and-Offroading",
		"http://forums.vwvortex.com/forumdisplay.php?126-Car-Purchasing-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?24-Detailing-Forum",		
		"http://forums.vwvortex.com/forumdisplay.php?106-The-Bentley-Lounge",
		"http://forums.vwvortex.com/forumdisplay.php?107-The-Bugatti-Lounge",
		"http://forums.vwvortex.com/forumdisplay.php?108-The-Lamborghini-Lounge",
		"http://forums.vwvortex.com/forumdisplay.php?5329-Aventador",
		"http://forums.vwvortex.com/forumdisplay.php?583-Countach",
		"http://forums.vwvortex.com/forumdisplay.php?582-Diablo",
		"http://forums.vwvortex.com/forumdisplay.php?544-Gallardo-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?584-Miura",
		"http://forums.vwvortex.com/forumdisplay.php?545-Murcielago-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?5191-SEAT-and-Skoda",
		"http://forums.vwvortex.com/forumdisplay.php?109-The-SEAT-Lounge",
		"http://forums.vwvortex.com/forumdisplay.php?546-Ibiza-amp-Cordoba-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?547-Toledo-Leon-amp-Altea-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?110-The-Skoda-Lounge",		
		"http://forums.vwvortex.com/forumdisplay.php?5113-United-States",
		"http://forums.vwvortex.com/forumdisplay.php?84-New-England",
		"http://forums.vwvortex.com/forumdisplay.php?5228-New-England-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5230-New-England-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?352-TriState",
		"http://forums.vwvortex.com/forumdisplay.php?5231-TriState-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5233-TriState-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?85-Mid-Atlantic",
		"http://forums.vwvortex.com/forumdisplay.php?5235-Mid-Atlantic-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5236-Mid-Atlantic-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?351-Capital-Area",
		"http://forums.vwvortex.com/forumdisplay.php?5239-Capital-Area-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5240-Capital-Area-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?86-South-East",
		"http://forums.vwvortex.com/forumdisplay.php?5243-South-East-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5244-South-East-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?93-South-West",
		"http://forums.vwvortex.com/forumdisplay.php?5247-South-West-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5248-South-West-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?87-Midwest",
		"http://forums.vwvortex.com/forumdisplay.php?5251-Midwest-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5252-Midwest-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?88-South",
		"http://forums.vwvortex.com/forumdisplay.php?5255-South-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5256-South-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?862-Nevada-and-Utah",
		"http://forums.vwvortex.com/forumdisplay.php?5259-Nevada-and-Utah-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5260-Nevada-and-Utah-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?89-Rocky-Mountain",
		"http://forums.vwvortex.com/forumdisplay.php?5263-Rocky-Mountain-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5264-Rocky-Mountain-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?90-Pacific-Northwest",
		"http://forums.vwvortex.com/forumdisplay.php?5267-Pacific-Northwest-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5268-Pacific-Northwest-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?91-NorCal",
		"http://forums.vwvortex.com/forumdisplay.php?5271-NorCal-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5272-NorCal-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?92-SoCal",
		"http://forums.vwvortex.com/forumdisplay.php?5275-SoCal-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5276-SoCal-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?120-Hawaii",
		"http://forums.vwvortex.com/forumdisplay.php?5278-Hawaii-Parts",
		"http://forums.vwvortex.com/forumdisplay.php?5279-Hawaii-Cars",
		"http://forums.vwvortex.com/forumdisplay.php?5114-Canada",
		"http://forums.vwvortex.com/forumdisplay.php?858-Western-Canada",
		"http://forums.vwvortex.com/forumdisplay.php?94-Ontario",
		"http://forums.vwvortex.com/forumdisplay.php?859-Eastern-Canada",
		"http://forums.vwvortex.com/forumdisplay.php?5115-Europe",
		"http://forums.vwvortex.com/forumdisplay.php?131-Germany",
		"http://forums.vwvortex.com/forumdisplay.php?130-United-Kingdom",
		"http://forums.vwvortex.com/forumdisplay.php?134-Europe-General",
		"http://forums.vwvortex.com/forumdisplay.php?5116-Australia",
		"http://forums.vwvortex.com/forumdisplay.php?137-Australia",
		"http://forums.vwvortex.com/forumdisplay.php?5117-South-Africa",
		"http://forums.vwvortex.com/forumdisplay.php?132-South-Africa",
		"http://forums.vwvortex.com/forumdisplay.php?5118-South-America-Central-America-and-Mexico",
		"http://forums.vwvortex.com/forumdisplay.php?135-South-America-Central-America-amp-Mexico",
		"http://forums.vwvortex.com/forumdisplay.php?5145-Asia",
		"http://forums.vwvortex.com/forumdisplay.php?954-Asia",
		"http://forums.vwvortex.com/forumdisplay.php?5112-Events",
		"http://forums.vwvortex.com/forumdisplay.php?5388-Carlisle-2015",
		"http://forums.vwvortex.com/forumdisplay.php?5377-EuroSlam-15",
		"http://forums.vwvortex.com/forumdisplay.php?5355-Euro-Tripper",
		"http://forums.vwvortex.com/forumdisplay.php?5402-Wookies-in-the-Woods-2016",
		"http://forums.vwvortex.com/forumdisplay.php?974-Spring-VW-amp-Audi-Show-and-Go-Englishtown-s-Raceway-Park",
		"http://forums.vwvortex.com/forumdisplay.php?967-2015-New-England-Dustoff-presented-by-Ocean-State-Dubs",
		"http://forums.vwvortex.com/forumdisplay.php?5352-W%F6rthersee",
		"http://forums.vwvortex.com/forumdisplay.php?1159-SOWO-presents-The-European-Experience",
		"http://forums.vwvortex.com/forumdisplay.php?5308-Wuste-European-Car-Festival-2015",
		"http://forums.vwvortex.com/forumdisplay.php?5389-Vacationland-VAG-Fair-2015",
		"http://forums.vwvortex.com/forumdisplay.php?5349-Eurokracy",
		"http://forums.vwvortex.com/forumdisplay.php?5328-Euro-Hangar",
		"http://forums.vwvortex.com/forumdisplay.php?5409-Walkerfest-1",
		"http://forums.vwvortex.com/forumdisplay.php?570-Waterfest%AE-22",
		"http://forums.vwvortex.com/forumdisplay.php?5348-Wolfsgart",
		"http://forums.vwvortex.com/forumdisplay.php?1191-VW-Cult-Classic-10",
		"http://forums.vwvortex.com/forumdisplay.php?981-V-A-G-Fair-2015",
		"http://forums.vwvortex.com/forumdisplay.php?1046-VAGKRAFT",
		"http://forums.vwvortex.com/forumdisplay.php?5335-BERLIN-KLASSIK-2016-Island-Tour",
		"http://forums.vwvortex.com/forumdisplay.php?5336-NOPI-NATIONALS-Supershow-Atlanta-Sept-22-23-2012-Atlanta-Dragway",
		"http://forums.vwvortex.com/forumdisplay.php?1147-Fall-VW-amp-Audi-Show-and-Go-Englishtown-s-Raceway-Park",
		"http://forums.vwvortex.com/forumdisplay.php?5387-H20-International-2016",
		"http://forums.vwvortex.com/forumdisplay.php?5351-Das-Laufwerk-The-Drive",
		"http://forums.vwvortex.com/forumdisplay.php?5338-5th-Annual-Oktoberfest-at-Black-Forest-Industries",
		"http://forums.vwvortex.com/forumdisplay.php?5390-NOLA-Speed-and-Style",
		"http://forums.vwvortex.com/forumdisplay.php?5337-%93DubRun%94-to-the-Poconos-2014",
		"http://forums.vwvortex.com/forumdisplay.php?1045-FixxFest-12",
		"http://forums.vwvortex.com/forumdisplay.php?5208-Motorsport-Forums",
		"http://forums.vwvortex.com/forumdisplay.php?5031-Professional-Racing",
		"http://forums.vwvortex.com/forumdisplay.php?359-Open-Wheel-Racing",
		"http://forums.vwvortex.com/forumdisplay.php?360-Rally-Racing",
		"http://forums.vwvortex.com/forumdisplay.php?361-Sportscar-GT-Racing",
		"http://forums.vwvortex.com/forumdisplay.php?362-Touring-Car",
		"http://forums.vwvortex.com/forumdisplay.php?305-Misc-Professional-Racing",
		"http://forums.vwvortex.com/forumdisplay.php?322-Racing-Technology-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?5032-Amateur-Racing",
		"http://forums.vwvortex.com/forumdisplay.php?309-Autocross",
		"http://forums.vwvortex.com/forumdisplay.php?124-Drag-Racing",
		"http://forums.vwvortex.com/forumdisplay.php?123-Misc-Amateur-Racing",
		"http://forums.vwvortex.com/forumdisplay.php?307-Open-Wheel",
		"http://forums.vwvortex.com/forumdisplay.php?306-Rally",
		"http://forums.vwvortex.com/forumdisplay.php?308-Road-Racing",
		"http://forums.vwvortex.com/forumdisplay.php?125-Technical",
		"http://forums.vwvortex.com/forumdisplay.php?5004-Forum-Help-and-Suggestions",
		"http://forums.vwvortex.com/forumdisplay.php?98-Forum-Help",
		"http://forums.vwvortex.com/forumdisplay.php?40-Testing-Forum",
		"http://forums.vwvortex.com/forumdisplay.php?23-Suggestion-Box"
        ]
	COUNTRY = "USA"
	THREAD_XPATH = "//a[re:test(@id,'thread_title_*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "(//div[@id='pagination_top']//span[@class='first_last'])[last()]/a/@href"
	PREV_XPATH = "//div[@id='pagination_top']//span[@class='selected']/preceding::a[1]/@href"
	POST_XPATH = "//ol[@id='posts']//li[re:test(@id,'post_*')]/div[@class='postdetails']"
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
			"concat":True,
			"xpath": ".//div[@class='username_container']//a[re:test(@class,'username*')]//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='content']//text()"
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
			"xpath":"//div[@class='breadcrumb']//li[@class='navbit lastnavbit']//text()"
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
