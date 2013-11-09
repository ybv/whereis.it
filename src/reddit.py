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

subreddit_list=["earthporn"]
                #,"winterporn","autumnporn","cityporn","villageporn","abandonedporn","ruralporn"]

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
                temp_dict_item['url']=flickr_soup.find(id="allsizes-photo").img['src']         
            elif(top_json_dict['data']['children'][image_json_index]['data']['domain'].strip()=='500px.com'):
                temp_url=top_json_dict['data']['children'][image_json_index]['data']['url'].strip()
                fivepx_html=commands.getstatusoutput('curl -s '+temp_url)[1]
                fivepx_soup = BeautifulSoup(fivepx_html)
                print flickr_soup.find_all('div')
            else:
                temp_dict_item['url']=top_json_dict['data']['children'][image_json_index]['data']['url'].strip()
            #removing unwanted characters from the title and striping every thing after the square bracket for proper region extraction
            temp=re.sub(r'\[.*','',top_json_dict['data']['children'][image_json_index]['data']['title'].strip())
            temp_dict_item['title']=re.sub(r'\..*','',re.sub(r'[0-9]*','',temp))
            new_image_dict[temp_dict_item['key']]=temp_dict_item
    
    
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
        location_dict[new_image_dict[image_dict_index]['key']]=re.sub(r'.,.',',',tempstring)
    
    #print len(location_dict)
    #print location_dict
