from scraper.scraper import search_new_tweet, search_keyword
from datetime import datetime
from twilio.rest import Client
import time as t
import sys
import os

account_sid = 'ACcdf64dd3f2944ddb49e7247198426a7c' #these can be replaced with other twillio credentials
auth_token = '6e959bbbea93f12b3010d5b9983bdb9a' #these can be replaced with other twillio credentials
client = Client(account_sid, auth_token)

def setup():
    global username
    global phoneNum
    username = str(input("Enter the username of the Twitter account: "))
    phoneNum = str(input("Enter the phone number to recieve notifications: ")) #you must specify your country code (e.g. if it's a U.S. number, add "+1" to the beginning)

def main():
    keywords = open("keywords.txt", "r").read().split(", ")
    sinceTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Checking for new tweets...")
    while True:
        w = list()
        returnVar = search_new_tweet(sinceTime, username)
        if isinstance(returnVar, str):
            sinceTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for keyword in keywords:
                w.append(search_keyword(keyword, returnVar))
                w = [i for i in w if i]
            if w:
                notifier(', '.join(w), returnVar, sinceTime)
        t.sleep(1) # check every 1 second

def notifier(about, tweet, sinceTime):
    
    body = "<" + username + "> just tweeted about: " + about + "\nhttps://twitter.com/" + username
    
    message = client.messages \
                .create(
                     body = body,
                     from_='12673101877', #this can be replaced with another twillio number
                     to = phoneNum
                 )

    print("SMS Message Successfully Sent!")



if __name__ == '__main__':
    setup()
    main()
