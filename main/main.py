from scraper.scraper import search_new_tweet
from datetime import datetime
import time as t

def main():
    keywords = open("keywords.txt", "r").read().split(", ")
    username = input("Enter the username of the Twitter account: ")
    presentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    while True:
        if isinstance(search_new_tweet(presentTime, username), str):
            print(search_new_tweet(presentTime, username))
            t.sleep(1) #checks every 1 second

        '''
        for keyword in keywords:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            search_keyword(keyword, time, username)
        '''

if __name__ == '__main__':
    main()
