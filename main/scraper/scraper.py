import twint
import requests, bs4
import os, sys
import urllib
from lxml import html
from io import StringIO
from datetime import datetime

class Capturing(list): # didn't realize twint had a format function :p 
    def __enter__(self):    
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout
        
def search_new_tweet(sinceTime, username):
    c = twint.Config()
    c.Username = username
    c.Since = sinceTime
    c.Limit = 1
    c.Output = "output.csv"
    with Capturing() as output:
        twint.run.Search(c)
    if len(output) == 0:
        return 0
    elif output[0] != "[!] No more data! Scraping will stop now.":
        newTweet = output[0][output[0].find(">") + 2: None]
        print("[",sinceTime,"]", newTweet)
        return newTweet
    
def search_keyword(keyword, tweet):
    if keyword.lower() in tweet.lower():
        return keyword

def getImage(URL_String):
    rel_path = "./classifier/temp"
        
    page=requests.get(URL_String)
    print(page.status_code)
    tree=html.fromstring(page.content)
 
    print(tree)
    tweet_imgs=tree.xpath('//div[@class="AdaptiveMedia-singlePhoto"]//img[@src]')
 
    del page, tree
    print("Array of tweet images fetched")
    print(tweet_imgs)
    img_num = 1
    for tweet_img in tweet_imgs:
        print("Image " + tweet_img.attrib['src'] + " processed")
        image_address=requests.get(tweet_img.attrib['src'])
        resource=image_address.content
        output=open(FOLDER_URL + "/" + "Image" + str(img_num) + ".jpg", "wb")
        output.write(resource)
        output.close()
        img_num=img_num+1

