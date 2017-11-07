# coding: UTF-8

from requests_oauthlib import OAuth1Session

"""
OAuth認証を行うときに使うクラス
"""
class OAuth:
    config = {}
    """
    コンストラクタ
    """
    def __init__(self,path):
        exec(open(path).read(),self.config)

    """
    指定されたキーを使用してOAuth認証を行う
    """
    def oauth(self):
        return OAuth1Session(self.config["consumer_key"], self.config["consumer_secret"], self.config["access_key"], self.config["access_secret"])
