from requests_oauthlib import OAuth1Session

class OAuth:
    config = {}
    def __init__(self,path):
        exec(open(path).read(),self.config)

    def oauth(self):
        return OAuth1Session(self.config["consumer_key"], self.config["consumer_secret"], self.config["access_key"], self.config["access_secret"])
