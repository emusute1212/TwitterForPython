# coding: UTF-8

from OAuth import OAuth
from Search import Search
from TimeZoneConversion import TimeZoneConversion
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
    # 検索結果の格納
    tweet=search.findTweet(target)

    # タイムゾーンを変更して表示するかの入力待ち
    print("Change to the timezone of Japan?\nyes:1 no:0")
    changeTimeZone=input(">> ")
    if int(changeTimeZone) == 1:
        # タイムゾーンを制御するためのインスタンス(今回は東京にタイムゾーンを合わせてある)
        zone=TimeZoneConversion("Asia/Tokyo")
        tweet["created_at"]=str(zone.convertDate(tweet["created_at"]))

    # 検索結果をjsonで出力
    print(json.dumps(tweet,ensure_ascii=False,indent=4))
