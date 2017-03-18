# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 20:05:08 2016

@author: manish chandra
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:56:22 2016

@auth
"""

import json
import pickle
#import simplejson

def main():
    
    tweets_filename = 'perry_test.txt'
    tweets_file = open(tweets_filename, "r")
    #file1 = 'test.txt'
    #file2 = open(file1, 'w')
    f = open('testing
    .txt', 'w')
    count = 0
    tweets = []
    B =[1,"xyz"]
    print "***********************************************************************"
    for line in tweets_file:
        try:        
            # Read in one line of the file, convert it into a json object 
            tweet = json.loads(line.strip())
            B[0] = count
            #B[1]=1
            B[1] = tweet['text']
            #tweets.append(B)
            #file2.write('\n'.join(B))
            #file2.write("%s", % count)
            #with open('test.txt', 'w') as out_file:
                #out_file.write('\n'.join(B)) 
            #pickle.dump(B, file2)
            #json.dump(B, f)
            f.write(json.dumps(B) + '\r\n')
            #json.dump(\n,f)            
            #tweets.insert(count,B)
            #tweets[count] = B
            #if count <5:
                #print "AAAAA"
            print B
                #print "BBBB"
                #print tweets
                #print "CCCC"
            count += 1
            
            #print "ID of the %d tweet = %d" %(count,tweet['id'])
            #print tweet.keys()
            #print tweet['text']
            #print tweet['created_at']

   
                
        except:
            # read in a line is not in JSON format
            continue
    print "***********************************************************************"
    print count
    f.close()        
    #print tweets
if __name__ == '__main__':
    main()