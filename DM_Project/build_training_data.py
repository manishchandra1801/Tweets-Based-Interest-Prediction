# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 19:56:10 2016

@author: manish chandra
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:56:22 2016

@author: 
"""

import json
import pickle
#import simplejson
import os
from pattern.en import sentiment, positive

def main():
    
    tweets_filename = 'sports.txt'
    tweets_file = open(tweets_filename, "r")
    
    #file1 = 'test.txt'
    #file2 = open(file1, 'w')
    #f = open('test1.txt', 'w')
    count = 0
    tweets = []
    B =[1,1,"xyz"]
    print "***********************************************************************"
    for line in tweets_file:
        try:        
            # Read in one line of the file, convert it into a json object 
            tweet = json.loads(line.strip())
            tweet_text = tweet['text']
            tweet_assment = sentiment(tweet_text)
            #B[0] = count
            #B[2] = tweet['text']
            
            if positive(tweet_assment, threshold=0.1):
                fil = open('sports_train.txt', 'a')
                
                count += 1        
                B[0] = count
                B[1]=1
                B[2] = tweet['text']                
                fil.write(json.dumps(B) + '\n')
                fil.close()
                
            else:
                fil = open('sports_train.txt', 'a')
                count += 1                
                B[0] = count
                B[1]=0
                B[2] = tweet['text']
                fil.write(json.dumps(B) + '\n')
                fil.close()
                
            #f.write(json.dumps(B) + '\r\n')
            #tweets.insert(count,B)
                                
            

   
                
        except:
            # read in a line is not in JSON format
            continue
    print "***********************************************************************"
    print count
    fil.close()        
    #print tweets
if __name__ == '__main__':
    main()