# coding: UTF-8

from requests_oauthlib import OAuth1Session

"""
検索するときに使うクラス
"""
class Search:
    """
    検索方法
    """
    SEARCH_TYPE=["screen_name","user_id"]
    """
    Userを検索するときのリクエストURL
    """
    SEARCH_USER_URL = "https://api.twitter.com/1.1/users/lookup.json"
    """
    Tweetを検索するときのリクエストURL
    """
    SEARCH_TWEET_URL = "https://api.twitter.com/1.1/statuses/show.json"

    """
    コンストラクタ
    """
    def __init__(self,twitter):
        self.twitter=twitter

    """
    ユーザーを検索するメソッド

    引数
    serachTarget：検索対象
    searchType：0か1．0の場合はUser_IDでの検索，1の場合はAPI_IDで検索する
    """
    def findUser(self,serachTarget,searchType):
        params = {self.SEARCH_TYPE[searchType]: serachTarget}
        req = self.twitter.get(self.SEARCH_USER_URL, params = params)
        if req.status_code == 200:
            return req.json()
        else:
            return "Error: %d" % req.status_code

    """
    ツイートを検索するメソッド
    
    引数
    serachTarget：検索対象
    """
    def findTweet(self,serachTarget):
        params={"id":serachTarget}
        req = self.twitter.get(self.SEARCH_TWEET_URL, params = params)
        if req.status_code == 200:
            return req.json()
        else:
            return "Error: %d" % req.status_code