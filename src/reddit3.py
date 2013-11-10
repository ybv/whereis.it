import pickle


with open("/home/tj/Dropbox/pg/py/whereis.it/src/location9.pickle") as f:
    tot_location_dict, fullname_location_dict, new_image_dict, in_dict = pickle.load(f)
    
#
final_dict = {}
for k,value in fullname_location_dict.iteritems():
	final_dict['id'] = k
	final_dict['location'] = value['place']
	final_dict['source'] = new_image_dict[k]['domain']
	final_dict['source_link'] = new_image_dict[k]['permalink']
	final_dict['image_link'] = new_image_dict[k]['url']
	final_dict['lat_long'] = [str(value['lat']),str(value['lng'])]
	final_dict['weather_link'] = None
	final_dict['weather_current_type'] = None
	final_dict['weather_current_now'] = None
	final_dict['weather_today_high'] = None
	final_dict['weather_today_low'] = None
	if len(in_dict[k]['nearby_places']) == 0:
		final_dict['nearby_place1_name'] = None
		final_dict['nearby_place1_url'] = None
		final_dict['nearby_place2_name'] = None
		final_dict['nearby_place2_url'] = None
		final_dict['nearby_place3_name'] = None
		final_dict['nearby_place3_url'] = None
		final_dict['nearby_place4_name'] = None
		final_dict['nearby_place4_url'] = None
	elif len(in_dict[k]['nearby_places']) == 1:
		final_dict['nearby_place1_name'] = in_dict[k]['nearby_places'][0]['venue_name']
		final_dict['nearby_place1_url'] = in_dict[k]['nearby_places'][0]['venue_url']
		final_dict['nearby_place2_name'] = None
		final_dict['nearby_place2_url'] = None
		final_dict['nearby_place3_name'] = None
		final_dict['nearby_place3_url'] = None
		final_dict['nearby_place4_name'] = None
		final_dict['nearby_place4_url'] = None
	elif len(in_dict[k]['nearby_places']) == 2:
		final_dict['nearby_place1_name'] = in_dict[k]['nearby_places'][0]['venue_name']
		final_dict['nearby_place1_url'] = in_dict[k]['nearby_places'][0]['venue_url']
		final_dict['nearby_place2_name'] = in_dict[k]['nearby_places'][1]['venue_name']
		final_dict['nearby_place2_url'] = in_dict[k]['nearby_places'][1]['venue_url']
		final_dict['nearby_place3_name'] = None
		final_dict['nearby_place3_url'] = None
		final_dict['nearby_place4_name'] = None
		final_dict['nearby_place4_url'] = None
	elif len(in_dict[k]['nearby_places']) == 3:
		final_dict['nearby_place1_name'] = in_dict[k]['nearby_places'][0]['venue_name']
		final_dict['nearby_place1_url'] = in_dict[k]['nearby_places'][0]['venue_url']
		final_dict['nearby_place2_name'] = in_dict[k]['nearby_places'][1]['venue_name']
		final_dict['nearby_place2_url'] = in_dict[k]['nearby_places'][1]['venue_url']
		final_dict['nearby_place3_name'] = in_dict[k]['nearby_places'][2]['venue_name']
		final_dict['nearby_place3_url'] = in_dict[k]['nearby_places'][2]['venue_url']
		final_dict['nearby_place4_name'] = None
		final_dict['nearby_place4_url'] = None
	elif len(in_dict[k]['nearby_places']) == 4:
		final_dict['nearby_place1_name'] = in_dict[k]['nearby_places'][0]['venue_name']
		final_dict['nearby_place1_url'] = in_dict[k]['nearby_places'][0]['venue_url']
		final_dict['nearby_place2_name'] = in_dict[k]['nearby_places'][1]['venue_name']
		final_dict['nearby_place2_url'] = in_dict[k]['nearby_places'][1]['venue_url']
		final_dict['nearby_place3_name'] = in_dict[k]['nearby_places'][2]['venue_name']
		final_dict['nearby_place3_url'] = in_dict[k]['nearby_places'][2]['venue_url']
		final_dict['nearby_place4_name'] = in_dict[k]['nearby_places'][3]['venue_name']
		final_dict['nearby_place4_url'] = in_dict[k]['nearby_places'][3]['venue_url']
	final_dict['wikipedia_url'] = None
	final_dict['wikipedia_text'] = None
	

