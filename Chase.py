# coding: UTF-8

from OAuth import OAuth
from Search import Search
import json

"""
ツイッターのユーザーを検索するプログラム
User_IDとAPI_IDのどちらかで検索可能
"""
if __name__ == "__main__":
    # TwitterAPIを制御するためのインスタンス生成
    certification = OAuth("Config.py")
    twitter=certification.oauth()
    search = Search(twitter)

    # 検索方法の選択
    print("Which want search?\nuserID:0,API_ID:1")
    while True:
        tempInput = input('>> ')
        if tempInput.isdigit():
            searchType=int(tempInput)
            if searchType <= 1:
                break
        print("Input 0 or 1.")

    # 検索対象の入力
    print("Input target.")
    target = input('>> ')
    user=search.findUser(target,searchType)
    
    # 結果をjsonで出力
    print(json.dumps(user,ensure_ascii=False,indent=4))

    # API_IDかUser_IDの出力．
    # User_IDで検索した際はAPI_IDを
    # API_IDで検索した際はUser_IDを出力する．
    if searchType == 0:
        print(user[0]['name'] + ":" + user[0]['id_str'])
    elif searchType == 1:
        print(user[0]['name'] + ":" + user[0]['screen_name'])
    else:
        print("Error")
