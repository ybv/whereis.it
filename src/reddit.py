'''
Created on Nov 9, 2013

@author: kaushal
'''
import commands
import json
import random
import re
import nltk

subreddit_name="earthporn"
top_json=commands.getstatusoutput('curl -s http://www.reddit.com/r/'+subreddit_name+'/.json?count=100')
#loading the json as the dict of dict of list of dicts
top_json_dict=json.loads(top_json[1])
new_image_dict=[]

for image_json_index in range(len(top_json_dict['data']['children'])):
    temp_dict_item={}
    if(top_json_dict['data']['children'][image_json_index]['data']['selftext_html'] is None):
        #generation of 10 digit random number
        temp_dict_item['key']=random.randint(1111111111,9999999999)
        temp_dict_item['domain']=top_json_dict['data']['children'][image_json_index]['data']['domain'].strip()
        temp_dict_item['subreddit']=top_json_dict['data']['children'][image_json_index]['data']['subreddit'].strip()
        temp_dict_item['author']=top_json_dict['data']['children'][image_json_index]['data']['author'].strip()
        temp_dict_item['permalink']=top_json_dict['data']['children'][image_json_index]['data']['permalink'].strip()
        temp_dict_item['url']=top_json_dict['data']['children'][image_json_index]['data']['url'].strip()
        #removing unwanted characters from the title and striping every thing after the square bracket for proper region extraction
        temp_dict_item['title']=re.sub(r'\[.*','',top_json_dict['data']['children'][image_json_index]['data']['title'].strip())
        new_image_dict.append(temp_dict_item)

for image_dict_index in range(len(new_image_dict)):
    

print new_image_dict

