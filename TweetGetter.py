# coding: UTF-8

from OAuth import OAuth
from Search import Search
import json

"""
ツイートIDから情報を取得するプログラム
"""
if __name__ == "__main__":
    # TwitterAPIを制御するためのインスタンス生成
    certification = OAuth("Config.py")
    twitter=certification.oauth()
    search = Search(twitter)

    # 検索対象の入力待ち
    print("Input target id.\nTarget id is \"https://twitter.com/(User_ID)/status/(Target_ID)\"")
    target = input('>> ')
    tweet=search.findTweet(target)

    # 検索結果をjsonで出力
    print(json.dumps(tweet,ensure_ascii=False,indent=4))
