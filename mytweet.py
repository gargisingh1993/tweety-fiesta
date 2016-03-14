# A Simple Function to 
# Fetch relevant tweet for a single REST Api request provided a keyword as a param
# Imported relevant libs - json , requests, request_oauthlib 
# imported json since twitter api returns the output as a json object ( when we hit the end point )
# important information which is needed for running this code is mentioned as comments below
# argparse used to pass a argument in command line.

# To run this file in command prompt (windows) or Command line other OS , type python <filename> <keyword>(you want to search for)

import json
import requests
from requests_oauthlib import OAuth1
import random
import time
import argparse

def main():
    #if we dont need the arguments in command prompt use the input fucntion to take a word to search relevant tweet in cmd or cli
    #if we want for a keyword with multiple words (remove the parser object and use the input method)
    
    #keyword = input('Enter the keyword word:')
    try:
        parser = argparse.ArgumentParser(description='Keyword for search')
        parser.add_argument('b')
        args = parser.parse_args()
        keyword = args.b
        myfunction(keyword)
    except (SystemExit,KeyError):
        print("Correct Argument needed to process request, try again with an argument")
    
    
def myfunction(keyword):
    CONSUMER_KEY = "Icn8VwBk5kjqv5XQlyf9LpqV3" # enter your app's consumer key
    CONSUMER_SECRET = "sT50aK0JANqzbGuTRrCs8BOCs0WwnYvLmCnRK6yPB1oYeedbvQ" # enter app's consumer secret 
    ACCESS_KEY ="4729598838-wD5JKXxDakjDE2dysq2mW83mvjWYr1zTcde0sfY" # enter access token 
    ACCESS_SECRET = "ZgDpPfwFVp8RggOcBd4wr9jCfxqzvD5gn9tUZ8780o6Le" #access token secret 
    auth = OAuth1(CONSUMER_KEY,CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
    url='https://api.twitter.com/1.1/search/tweets.json?q='+keyword
    res = requests.get(url,auth = auth)
    data = res.json()
    mylist  = []
    try:
        for statuses in data['statuses']:
            d = {
            'screen_name':statuses['user']['screen_name'],
            'text':statuses['text'],
            'url':statuses['user']['url'],
            }
            mylist.append(d)
    except KeyError:
        print ("entered string is invalid: please type a proper text to match")
    myfuncprint(mylist)
def myfuncprint(mylist):
    #for x in mylist:
    #print(x)
    try:
        x = random.choice(mylist)
        try:
            print ("@username:",x['screen_name']," ",x['text'])
        except UnicodeEncodeError:
            pass
            #print("IDLE does not support encoding: json in ansible") #can throw this exception if required to show the encoding problem with IDLE
        if x['url'] is None:
            print("Media : is empty")
        else:
            print("Media : ",x['url'])
        print("\n")
    except IndexError:
        print ("No tweet present")
        time.sleep(1)
if __name__ == "__main__": main()




#def convert(data):
 #   if isinstance(data, basestring):
  #      return str(data)
   # elif isinstance(data, collections.Mapping):
    #    return dict(map(convert, data.iteritems()))
    #elif isinstance(data, collections.Iterable):
     #   return type(data)(map(convert, data))
    #else:
        #return data
# we can use this function to convert the IDLE UnicodeEncodeError , but will need to import the ansible library to use the basestring 
# to use this function we need to import the collections library 
#since it was mentioned not to use anyother libraries other than the one's listed , i have commented this part of the code required to deal with the UnicodeEncodeError
