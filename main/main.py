from scraper.scraper import search_new_tweet, search_keyword, getImage
#from image_classifier.classifier import detectionObject
from datetime import datetime
from twilio.rest import Client
import time as t
import sys
import os

account_sid = 'TWILIO_ACCOUNT_SID' # REPLACE WITH TWILLIO CREDENTIALS
auth_token = 'TWILIO_AUTH_TOKEN' # REPLACE WITH TWILLIO CREDENTIALS
twillioPhoneNum = "xxxxxxxxxxx" # REPLACE WITH TWILLIO PHONE NUMBER
client = Client(account_sid, auth_token)

def setup():
    global username
    global phoneNum
    username = str(input("Enter the username of the Twitter account: "))
    phoneNum = str(input("Enter the phone number to recieve notifications: ")) # you must specify your country code (e.g. if it's a U.S. number, add "+1" to the beginning)

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
            if w: # if at least one keyword matches
                notifier(', '.join(w), returnVar, sinceTime)
            elif "t.co" in returnVar: #detects an image
                getImage(returnVar)
                #(not finished)
        t.sleep(1) # check every 1 second

def notifier(about, tweet, sinceTime):
    global twillioPhoneNumber
    body = "<" + username + "> just tweeted about: " + about + "\nhttps://twitter.com/" + username

    message = client.messages \
                .create(
                     body = body,
                     from_= twillioPhoneNum,
                     to = phoneNum
                 )
    print("SMS Message Successfully Sent!")

if __name__ == '__main__':
    setup()
    main()
