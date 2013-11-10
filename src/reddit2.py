import pickle
import unicodedata
import foursquare

client = foursquare.Foursquare(client_id='142EITET01LNXNP0N13MCUTJSOKWNZNETP5TEHKP3LNJTHPV', client_secret='L1TJOPPWZZKWQ5JGTZBIJL52DLBTCURGTXIMB1A2YOPULQV0', version='20111215')

with open("/home/tj/Dropbox/pg/py/whereis.it/src/location1.pickle") as f:
    tot_location_dict, fullname_location_dict, new_image_dict = pickle.load(f)
    
in_dict = tot_location_dict

for id, dump in in_dict.iteritems():
	nearby_places = client.venues.explore(params={'ll':str(round(dump['lat'],1))+','+str(round(dump['lng'],1))})
	k = 0
	temp_l = []
	while (k < 10 and k < len(nearby_places['groups'][0]['items'])):
		venue_name = unicodedata.normalize('NFKD', nearby_places['groups'][0]['items'][k]['venue']['name']).encode('ascii','ignore')
		venue_id = nearby_places['groups'][0]['items'][k]['venue']['id']
		venue_url = client.venues(venue_id)['venue']['shortUrl']
		print venue_name,':::',venue_id,':::',venue_url
		print '------------------------------------------------------'
		temp_l.append({'venue_name':venue_name, 'venue_id':venue_id, 'venue_url':venue_url})
		k = k+1
	dump['nearby_places'] = temp_l

with open("/home/tj/Dropbox/pg/py/whereis.it/src/location9.pickle", 'w') as f:
    pickle.dump([tot_location_dict, fullname_location_dict, new_image_dict, in_dict], f)
