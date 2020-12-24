# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
import os
import TextTweet
import GetTweet

# APIのトークン
CK=os.environ[CK]
CS=os.environ[CS]
AT=os.environ[AT]
AS=os.environ[AS]

twische = BlockingScheduler()

# 10分に一度ツイート（minutesで時間を指定できるよ）
@twische.scheduled_job('interval',minutes=30)
def timed_job():
    TextTweet.puttweet()

# 10分に一度ツイートを取得、チェーンを作ってdbに保存するよ
@twische.scheduled_job('interval',minutes=15)
def timed_job():
    #ツイートを取得
    GetTweet.gettweet(CK,CS,AT,AS)

    #data.txtに保存
    f = open("Data.txt",encoding="utf-8")
    text = f.read()
    f.close()

    '''
    #チェーンを作成、dbに保存
    chain = PrepareChain(text)
    triplet_freqs = chain.make_triplet_freqs()
    chain.save(triplet_freqs, True)
    '''

if __name__ == "__main__":
    twische.start()