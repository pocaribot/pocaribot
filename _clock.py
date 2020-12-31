# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
import os
import TextTweet
import GetTweet

# APIのトークン
CK=os.environ["CK"]
CS=os.environ["CS"]
AT=os.environ["AT"]
AS=os.environ["AS"]

twische = BlockingScheduler(timezone='UTC')

def GT():
    GetTweet.gettweet(CK,CS,AT,AS)

    #data.txtに保存
    f = open("Data.txt",encoding="utf-8")
    text = f.read()
    f.close()

def TT():
    TextTweet.puttweet()

twische.add_job(GT,'cron',hour="0-17,22-23",minute="0,15,30,45")
twische.add_job(TT,'cron',hour="0-17,22-23",minute="0,30")

GT()

if __name__ == "__main__":
    twische.start()