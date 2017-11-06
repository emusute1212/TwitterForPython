from requests_oauthlib import OAuth1Session
import json

class Search:
    SEARCH_TYPE=["screen_name","user_id"]
    SEARCH_USER_URL = "https://api.twitter.com/1.1/users/lookup.json"
    SEARCH_TWEET_URL = "https://api.twitter.com/1.1/statuses/show.json"

    def __init__(self,twitter):
        self.twitter=twitter

    def findUser(self,serachTarget,searchType):
        params = {self.SEARCH_TYPE[searchType]: serachTarget}
        req = self.twitter.get(self.SEARCH_USER_URL, params = params)
        if req.status_code == 200:
            print(json.dumps(req.json(),ensure_ascii=False,indent=4))
            if searchType == 0:
                return req.json()[0]['name'] + ":" +  req.json()[0]['id_str']
            if searchType == 1:
                return req.json()[0]['name'] + ":" +  req.json()[0]['screen_name']
            else:
                return "Error"
        else:
            return "Error: %d" % req.status_code

    def findTweet(self,serachTarget):
        params={"id":serachTarget}
        req = self.twitter.get(self.SEARCH_TWEET_URL, params = params)
        if req.status_code == 200:
            print(json.dumps(req.json(),ensure_ascii=False,indent=4))
        else:
            return "Error: %d" % req.status_code