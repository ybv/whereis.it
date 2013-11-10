'''
Created on Nov 9, 2013

@author: kaushal
'''
import commands
import json
import random
import re
import nltk
from bs4 import BeautifulSoup
from geopy import geocoders
import pickle
import  pywapi
import string

subreddit_list=["earthporn","winterporn","autumnporn","cityporn","villageporn","abandonedporn","ruralporn"]

tot_location_dict={}
for subreddit_name in subreddit_list:
    top_json=commands.getstatusoutput('curl -s http://www.reddit.com/r/'+subreddit_name+'/.json?limit=100')
    #loading the json as the dict of dict of list of dicts
    top_json_dict=json.loads(top_json[1])
    new_image_dict={}
    
    for image_json_index in range(len(top_json_dict['data']['children'])):
        temp_dict_item={}
        if(top_json_dict['data']['children'][image_json_index]['data']['selftext_html'] is None):
            #generation of 10 digit random number
            temp_dict_item['key']=random.randint(1111111111,9999999999)
            temp_dict_item['domain']=top_json_dict['data']['children'][image_json_index]['data']['domain'].strip()
            temp_dict_item['subreddit']=top_json_dict['data']['children'][image_json_index]['data']['subreddit'].strip()
            temp_dict_item['author']=top_json_dict['data']['children'][image_json_index]['data']['author'].strip()
            temp_dict_item['permalink']=top_json_dict['data']['children'][image_json_index]['data']['permalink'].strip()
            if(top_json_dict['data']['children'][image_json_index]['data']['domain'].strip()=='flickr.com'):
                temp_url_splits=top_json_dict['data']['children'][image_json_index]['data']['url'].strip().split("/")
                temp_url=temp_url_splits[0]+"/"+temp_url_splits[1]+"/"+temp_url_splits[2]+"/"+temp_url_splits[3]+"/"+temp_url_splits[4]+"/"+temp_url_splits[5]+"/"+ "sizes/l/in/photostream/"
                flickr_html=commands.getstatusoutput('curl -s '+temp_url)[1]
                flickr_soup = BeautifulSoup(flickr_html)
                if flickr_html=="" :
                    temp_url=temp_url_splits[0]+"/"+temp_url_splits[1]+"/"+temp_url_splits[2]+"/"+temp_url_splits[3]+"/"+temp_url_splits[4]+"/"+temp_url_splits[5]+"/"+ "sizes/z/in/photostream/"
                    flickr_html=commands.getstatusoutput('curl -s '+temp_url)[1]
                    flickr_soup = BeautifulSoup(flickr_html)
                temp_dict_item['url']=flickr_soup.find(id="allsizes-photo").img['src']         
            elif(top_json_dict['data']['children'][image_json_index]['data']['domain'].strip()=='500px.com'):
                temp_url=top_json_dict['data']['children'][image_json_index]['data']['url'].strip()
                fivepx_html=commands.getstatusoutput('curl -s '+temp_url)[1]
                fivepx_soup = BeautifulSoup(fivepx_html)
                img_list=fivepx_soup.find_all('img')
                for img_tag in img_list:
                    if(img_tag.has_attr("data-protect")):
                        temp_dict_item['url']=img_tag['src']
            else:
                temp_dict_item['url']=top_json_dict['data']['children'][image_json_index]['data']['url'].strip()
            #removing unwanted characters from the title and striping every thing after the square bracket for proper region extraction
            temp=re.sub(r'\[.*','',top_json_dict['data']['children'][image_json_index]['data']['title'].strip())
            temp_dict_item['title']=re.sub(r'\..*','',re.sub(r'[0-9]*','',temp))
            new_image_dict[temp_dict_item['key']]=temp_dict_item
    
    #print new_image_dict
    
    location_dict={}
    for image_dict_index in new_image_dict.iterkeys():
        temp_tokens=nltk.word_tokenize(new_image_dict[image_dict_index]['title'])
        tags=nltk.pos_tag(temp_tokens)
        tempstring=""
        for tag_item in tags:
            if tag_item[1]=='NNP' or tag_item[1]==',':
                tempstring=tempstring+tag_item[0]+" "
            else:
                tempstring=""
        tempstring.rstrip(" ")
        #print re.sub(r'.,.',',',tempstring)
        #location_dict[new_image_dict[image_dict_index]['key']]=re.sub(r'.,.',',',tempstring)
        g = geocoders.GoogleV3()
        #g = geocoders.MediaWiki("http://wiki.case.edu/%s") 
        #g = geocoders.SemanticMediaWiki("http://wiki.case.edu/%s",attributes=['Coordinates'],relations=['Located in'])
        try:
            place, (lat, lng) = g.geocode(re.sub(r'.,.',',',tempstring))    
            print "%s: %.5f, %.5f" % (place, lat, lng) 
            location_dict[new_image_dict[image_dict_index]['key']]={'place':place.split(',')[0], 'lat':lat, 'lng':lng}
            tot_location_dict[new_image_dict[image_dict_index]['key']]={'place':place.split(',')[0], 'lat':lat, 'lng':lng}
        except:
            pass
            '''
            saved_loc=open('/home/kaushal/Downloads/location.wit')
            tot__location_dict=pickle.load(saved_loc)
            for dict_element in tot__location_dict:
                print tot__location_dict
            '''
        else:
            location_json=commands.getstatusoutput('curl -s http://api.wunderground.com/api/8e3075e464747f3c/geolookup/q/'+str(lat)+','+str(lng)+'.json')
            location_json_dict=json.loads(location_json[1])
            
            weather_json=commands.getstatusoutput('curl -s http://api.openweathermap.org/data/2.5/weather?q='+location_json_dict['location']['city'])
            weather_json_dict=json.loads(location_json[1])
            print "status : "+weather_json_dict["weather"][0]['main']
            print "temp : "+((weather_json_dict["main"]['temp']-32)*(5/9))
            print "temp min : "+((weather_json_dict["main"]['temp_min']-32)*(5/9))
            print "temp max: "+((weather_json_dict["main"]['temp_max']-32)*(5/9))
            
            
    print len(location_dict)
    print location_dict
    
#loc_file=open("/home/kaushal/Downloads/location.wit",'w')
#pickle.dump(tot_location_dict,loc_file)

