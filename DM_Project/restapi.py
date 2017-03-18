# -*- coding: utf-8 -*-
"""
Created on Mon May 09 19:06:29 2016

@author: manish chandra
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 20:09:14 2016

@author: manish chandra
"""

# -*- coding: utf-8 -*-
"""
@author: Huixian
"""
import sys, twitter, operator
from dateutil.parser import parse
import json
import os
#out_folder = r'C:\Users\manish chandra\Documents\DM_Project\Train_project'
out_folder = r'C:\Users\manish chandra\Documents\DM_Project\test'
#list_users = ['@katyperry ','@justinbieber','@taylorswift13 ','@rihanna ','@ladygaga ','@britneyspears','@selenagomez ','@ArianaGrande','@shakira','@ddlovato','@Drake','@MileyCyrus','@onedirection']
list_users = ['@katyperry']
api = twitter.Api(consumer_key='sfYOUZ7CUZe5qxP4tE2qvAP3K', consumer_secret='OfEMUOPQKc2Dm0trNnjXL64Wdicdk4ROWOZBerwDtzOSfuaKfm', access_token_key='701115970493005824-bTkR5svLoOUOqUQLylytTKkvxsBIgCn', access_token_secret='w933MGOP40bPV25g6Pbpm6TVnJOhGZ5bUxSzzt9PczA3U')   

"""
fetch all tweets of a single user
"""

def print_info(tweet):
    print '***************************'
    print 'Tweet ID: ', tweet[id]
    print 'Post Time: ', tweet['created_at']
    print 'User Name: ', tweet['user']['screen_name']
    try:
	    print 'Tweet Text: ', tweet['text']
    except:
		pass

def fetch_historical(user):
    data = {}  
    max_id = None
    total = 0
    while True:
        statuses = api.GetUserTimeline(screen_name=user, count=200, max_id=max_id) 
        #print statuses
        newCount = ignCount = 0 
        for s in statuses:
            if s.id in data:
                ignCount += 1
            else:
                data[s.id] = s
                newCount += 1
        total += newCount
        print >>sys.stderr, "Fetched %d/%d/%d new/old/total." % (newCount, ignCount, total)
        if total > 500:
            break       
        max_id = min([s.id for s in statuses])-1
    return data.values()

"""
fetch tweets whose id is bigger than specific id
"""
def fetch_today(user):
    data = {}  
    max_id = None
    total = 0
    last_id = get_last_id(user)
    while True:       
        statuses = api.GetUserTimeline(screen_name=user, count=200, max_id=max_id, since_id=last_id)    
        newCount = ignCount = 0 
        for s in statuses:
            if s.id in data:
                ignCount += 1
            else:
                data[s.id] = s
                newCount += 1
        total += newCount
        print >>sys.stderr, "Fetched %d/%d/%d new/old/total." % (
            newCount, ignCount, total)
        if newCount == 0:
            break       
        max_id = min([s.id for s in statuses])-1
    return data.values()
    
def get_last_id(user):
    fname = '%s.txt'%user 
    fname = os.path.join(out_folder,fname)
    f = open(fname,'r')
    last_line = f.readlines()[-80]
    tweet = json.loads(last_line)
    f.close()
    return tweet['id']

def txtPrint1(user,tweets,out_folder):
    for t in tweets:
        t.pdate = parse(t.created_at)
    key = operator.attrgetter('pdate')
    tweets = sorted(tweets, key=key)
    keytweets = [json.loads(str(rawtweet)) for rawtweet in tweets]
    fname = 'R.txt'
    fname = os.path.join(out_folder,fname)
    f = open(fname,'a+')
    for tweet in keytweets:
        f.write(json.dumps(tweet) + '\n')
    f.close()

    
def txtPrint(user,tweets,out_folder):
    for t in tweets:
        t.pdate = parse(t.created_at)
    key = operator.attrgetter('pdate')
    tweets = sorted(tweets, key=key)
    keytweets = [json.loads(str(rawtweet)) for rawtweet in tweets]
    #fname = '%s.txt'%user
    fname='perry.txt'
    fname = os.path.join(out_folder,fname)
    f = open(fname,'a+')
    for tweet in keytweets:
        f.write(json.dumps(tweet) + '\n')
    f.close()

def crawl_users_historical_tweets(list_users, out_folder):  
    for user in list_users:
        data = fetch_historical(user)
        txtPrint(user,data,out_folder)

#def crawl_most_recent_tweets(list_users, out_folder):
 #   for user in list_users:
  #      data = fetch_today(user)
   #     txtPrint1(user,data,out_folder)
        

def main(): 
    #tweet=[]    
    crawl_users_historical_tweets(list_users,out_folder)
   
    #crawl_most_recent_tweets(list_users, out_folder)
    
        
        
    
if __name__ == '__main__':
    
    main()