# coding: UTF-8

import datetime
import pytz

"""
タイムゾーンを変更するときに使うクラス
"""
class TimeZoneConversion:
    """
    コンストラクタ
    インスタンスを生成する際に引数を指定することで．タイムゾーンを指定する
    """
    def __init__(self,timeZone):
        self.timeZone=pytz.timezone(timeZone)

    """
    引数で受け取った時刻を，指定したタイムゾーンの時刻に変更する．
    返却値はdatetime.datetime型となるので注意！
    """
    def convertDate(self,date):
        self.date = datetime.datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y")
        return self.timeZone.fromutc(self.date)
