#!/usr/bin/env python
#
from matplotlib import pyplot
import math
import numpy as np
import pandas as pd
#shelter
num_res = 141580000 #20% increase since 2000
sing_fam = num_res * .84
ownership_rate = num_res * .64
people_with_multiple_homes = ~10000000
num_com = 5900000 #56% increase since 1979
sq_ft = 97000000000 #89% increase since 1979
tires = 280000000 #annually 9 per second
plastic_bottles = 481600000000
water_bottles = 35000000000
restc = 2430000 #num_real_estate_businesses
commb = 5900000 #num_commercial_buildings
bootb = 240000 #num_military_buildings
commf = 97000000000 #num_comm_building_sqft
commo = 82.8/100 #comm_prop_occupied
commv = 17.2/100 #comm_prop_vacant
commw = 2400000000000 #comm_property_worth in USD
resb = 141950000 #num_residential_buildings
reso = 100/(88.4*resb) #res_prop_occupied
resv = 100/(11.6*resb) #res_prop_vacant [currently 16+ million]
tmp = 64  #average temp
sol = 13  #average hours sun per day
rpd = .13  #average rainfall per day
gnd = [0,1,2,3,4]  #soil type
pig = 1500000000 #num_pigs
beef = 34000000 #num_cows
hens = 48000000000 #num_chickens
goats = 444000000 #num_goats
sheep = 500000000 #num_sheep [excludes humans]
ls =  pig + beef + goats + sheep #num_livestock
fed2ls = 41/100 #edible_food_fed_to_livestock
water2ls = 70/100 #potable_water_used_for_ag
num_ac_am = 1274000000 #num_acres_frootable_land_am
num_ac_eu = 418000000 #num_acres_frootable_land_eu
num_ac_af = 2765109218 #num_acres_frootable_land_af
num_ac_as = 4200791485#num_acres_frootable_land_as
num_ac_sa = 14105600000 #num_acres_frootable_land_sa
num_ac_au = 1055139978 #num_acres_frootable_land_au
num_cal_req = 3200 #num_calories(to exist healthily, not just survive)
#growth_humans
daily = num_births - num_deaths
num_humneg5000 = 5000000
num_humneg500  = 100000000
num_hum600 =  200000000
num_hum1600 = 500000000
num_hum1804 = 1000000000
num_hum1850 = 1200000000
num_hum1900 = 1600000000
num_hum1927 = 2000000000
num_hum1960 = 3015470894
num_hum1980 = 4447606236
num_hum2000 = 6100000000
num_hum2020 = 7800000000
#growth_other_species
eukbac = # https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi
flora = # https://plants.usda.gov/
fauna = # https://www.catalogueoflife.org/data/taxon/N
#waste
plastic_byCountry = {'us':'92.5 Million Lbs.',
}
plastic_byIndustry = {'packaging':'101412640.6 Million Lbs.',
}
plastic_personDaily = {'us':'.7 Lbs.',
}
sewage_byCountryDaily = {'us':'34 Billion Gal',
}
#water
num_gal = 3 #num_gal water per day per person(to exist healthily[including washing, not just survive)
wastewater_untreated = 80/100 #returns to the ground this way
using_safeService = 70/100, 5300000000 #located on premises, available when needed, and free from contamination
using_basicService = 90/100, 6800000000 #basic service is an improved drinking-water source within a round trip of 30 minutes to collect water.
sans_basicService = 785000000
surface_dependent = 144000000
bottles = [
	#cost bulk
	{
	'1oz':.035, '8oz':.53, '12oz':.49, '16.9oz':.21,  '20oz':.30, '32oz':0, '64oz':0,'1G':0, '5G':0},
	#cost single
	{
	'1oz':0, '8oz':.79, '12oz':.99, '16.9oz':1.19,  '20oz':1.29, '32oz':2.29, '64oz':2.79,'1G':2.99, '5G':8.99},	
	#per_capita
	{	
	'2009':27.2, '2010':27.8, '2011':28.7, '2012': 30.4, '2013':31.6, '2014':33.6, '2015':35.9, '2016':38.5, '2017':40.6, '2018':42.4, '2019':43.7},	
	#per_state
	{	
	'al':27.2, 'ak':27.8, 'az':28.7, 'ar': 30.4, 'ca':31.6, 'co':33.6, 'ct':35.9, 'de':38.5, 'fl':40.6, 'ga':42.4, 'hi':43.7, 'id':27.2, 'il':27.8, 'in':28.7, 'ia':30.4, 'ks':31.6, 'ky':33.6, 'la':35.9, 'me':38.5, 'md':40.6, 'ma':42.4, 'mi':43.7, 'mn':27.2, 'ms':27.8, 'mo':28.7, 'mt':30.4, 'ne':31.6, 'nv':33.6, 'nh':35.9, 'nj':38.5, 'nm':40.6, 'ny':42.4, 'nc':43.7, 'nd':27.2, 'oh':27.8, 'ok':28.7, 'or':30.4, 'pa':31.6, 'ri':33.6, 'sc':35.9, 'sd':38.5, 'tn':40.6, 'tx':42.4, 'ut':43.7, 'vt':27.2, 'va':27.8, 'wa':28.7, 'wv':30.4, 'wi':31.6, 'wy':33.6}
	]
brands = ["3 springs", "3300 artesian water", "365 spring water", "a. l. lee corporation natural spring water", "aafiya water", "aarp west virginia", "abita springs", "absopure distilled water", "absopure drinking water", "absopure natural spring water", "admiral dewey distilled water", "admiral dewey drinking water", "admiral dewey purified water", "adobe springs", "aguazul natural spring water", "alaska chill", "alaska glacier", "alaska glacier cap", "alaska glacierblend", "alaska natural spring water", "albion water", "alcatraz", "alhambra", "alps water", "amelia springs water", "angel fire", "apani", "appalachian springs water", "aquamantra", "aquafina", "aquoforce", "arbutus", "arctic mist", "arrowhead", "artesia", "av-02", "avita", "baccara", "bashas' artesian spring water", "belmont springs", "big bear mountain", "big indian", "bikers' coolant","black mountain spring water", "bonaqa", "brick house farm water", "calistoga mineral water", "calistoga mountain spring water", "calistoga spring water","carolina mountain spring water", "caroline mountain water", "carrabassett", "castle rock", "castle springs", "catskill mountains", "cerebellum h2o", "cherokee bottled water", "claire baie bottled water", "clear mountain", "clearly arctic", "climax ky", "cobb mountain natural spring water", "cole brothers", "colfax", "colorado crystal", "cool luc", "cool springs pure springwater", "country creek", "crystal geyser natural alpine spring water", "crystal geyser natural spring water", "crystal geyser water", "crystal springs", "dannon", "dasani","deep rock", "deep rock crystal drop", "deep rock fontenelle", "deer park maryland", "deer park pennsylvania", "diamond natural spring water", "distillata", "dog water", "drinka", "earth2o", "edins x.o.", "eldorado natural spring water", "english mountain", "evo premium water", "famous crazy natural mineral water", "famous natural deep well mineral water", "famous premium drinking water", "flo first liquid obsession", "food lion drinking water", "fountain natural spring water", "fountainhead", "franklin heritage", "georgia mountain water", "giant filtered drinking water", "giant springs", "glaceau smart water", "glaceau vitamin water", "glenwood inglewood", "grand springs", "great bear", "h2only", "halstead", "harris teeter natural spring water", "hawaii water", "hd2o", "hidden spring", "hillcrest spring water. inc.", "hinckley springs", "hinkley & schmidt", "ice mountain", "idaho ice", "indian hills spring water", "keeper springs", "kentwood springs", "kroger drinking water", "kroger spring water", "laure spring water", "lauré pristine spring water", "le-natures water", "leisure time", "lesage natural wells", "life o2", "loon county", "manitou mineral water", "marin county all natural", "mckenzie mist", "model on a bottle (tm)", "mount olympus", "mountain forest spring water", "mountaineer pure", "mt. mckinley clear", "naturalle mountain spring water", "noah's california spring water", "oasis", "odwalla", "original fountain of youth mineral water", "ozardar", "ozarka", "pagosa springs", "palomar mountain spring water", "panther creek", "paradise bottled water", "parley's canyon", "penta", "pine barrens", "pocono springs pure mountain spring water", "poland spring", "pristine peaks", "pure montana", "pure pride", "purely sedona", "purple parrot", "quibell", "rain", "rocky grove", "saegertown beverage eureka springs", "seven creeks spring water", "shenandoah spring water", "shivar springs", "sierra springs", "silver creek",  "snow valley mountain spring water", "snowbird", "snowline natural water", "sparkletts", "stoneclear springs", "sweet springs natural mountain water", "tennessee mountain pure spring water", "trinity springs", "triton purified drinking water", "utopia", "valentine's pure spring water", "valley of the moon", "vermont pure", "water boy", "west virginia's pride of the mountains", "whispering springs water", "whole foods market 365 distilled water", "whole foods market 365 italian sparkling mineral water", "whole foods market 365 spring water", "wissahickon mountain spring water", "yellowstone headwaters", "zephyrhills"]
worldwide_sales = [{"wholesale":19400000000, "retail":34600000000}]
nestle_revenue2023 = 103984000000
water_bottles = 35000000000
#ag
'''
Farming animals is a problem that can and SHOULD be avoided. If their suffering doesn't sway your pampered, entitled cheeks, then the exponential use and waste of food and water should:
'''
am_rpy = [{	
'al':56.27, 'ak':37.33, 'az':14.71, 'ar': 65.59, 'ca':29.1, 'co':18.86, 'ct':54.24, 'de':41.58, 'fl':52.02, 'ga':47.89, 'hi':70.0,'id':23.34, 'il':49.87, 'in':49.52, 'ia':41.63, 'ks':36.08, 'ky':61.28, 'la':61.9, 'me':49.94, 'md':42.63, 'ma':52.7, 'mi':41.79, 'mn':35.49, 'ms':68.06, 'mo':53.85, 'mt':21.41, 'ne':31.41, 'nv':13.77, 'nh':50.2, 'nj':51.89, 'nm':13.35, 'ny':48.18, 'nc':50.98, 'nd':24.34, 'oh':46.86, 'ok':44.94, 'or':30.01, 'pa':50.75, 'ri':57.13, 'sc':45.71, 'sd':31.42, 'tn':66.87, 'tx':26.87, 'ut':16.94, 'vt':51.41, 'va':46.0, 'wa':33.08, 'wv':48.24, 'wi':44.55, 'wy':18.29}]
intl_rpy = [{
'ac':2.43, 'ad':31.98, 'ae':2.1, 'af': 17.01, 'ag':39.1, 'ai':34.86, 'al':54.24, 'am':9.8, 'ao':39.76, 'aq':2.01,'ar':23.26, 'as':113.38, 'at':43.7, 'au':21.02, 'aw':17.78, 'az':17.59}]	
amk = am_rpy.values()
amt = sum(amk)
intlk = am_rpy.values()
intlt = sum(intlk)	
'''def vym():
	with open('/lumber.vym', 'r') as lvym:
		pass
	with open('/hazchem.vym', 'r') as hcvym:
		pass
	with open('/water.vym', 'r') as wvym:
		pass
	with open('/ag.vym', 'r') as avym:
		pass
	with open('/waste.vym', 'r') as wastevym:
		pass
vym()
def lumber():

	with open('lumber.xlsx', 'r') as l:
		countries = []
		acresdes = []
		resourcew = []
		woodw = []
		
		done = False
		while not done:
			country = l.readline()
			if country == "":
				done = True
			else:
				line = l.readline()
				countries.append(country)
				parts = line.split()
				
				acsdes = int(parts[0])
				reswaste = int(parts[1])
				woodwaste = int(parts[2])
				
				acresdes.append(acsdes)
				resourcew.append(reswaste)
				woodw.append(woodwaste)
		
		pyplot.scatter(acresdes, resourcew, woodw, range(0, len(countries)))
		
		for x in range(len(countries)):
			pyplot.text(resourcew[x], woodw[x], countries[x], color = 'blue')
		
		pyplot.grid('on')
		pyplot.xlabel('wood wasted')
		pyplot.ylabel('resources wasted(excluding wood)')
		pyplot.title('destruction is not production')
		
		pyplot.show()

lumber()'''
