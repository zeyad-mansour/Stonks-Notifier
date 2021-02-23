import twint
import os, sys
from datetime import datetime

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
        
def search_new_tweet(presentTime, username):
    c = twint.Config()
    c.Username = username
    c.Since = presentTime
    c.Limit = 1
    with HiddenPrints():
        x = str(twint.run.Search(c))
        if x[0] != 'N':
            
    print("Nothing!")


def search_keyword(keyword, presentTime):
    
    c.Username = username
    c.Search = keyword
    with HiddenPrints():
        if str(twint.run.Search(c))[0] != 'N':
            print(keyword)


