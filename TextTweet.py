# -*- coding: utf-8 -*-
import os
import json
from requests_oauthlib import OAuth1Session
from _GenerateText import GenerateText
import random

def puttweet():
    # APIのトークン
    CK=os.environ[CK]
    CS=os.environ[CS]
    AT=os.environ[AT]
    AS=os.environ[AS]

    # APIに接続
    twitter = OAuth1Session(CK,CS,AT,AS)

    #generator = GenerateText(random.randint(1,3))

    #ツイート
    #markovstring = generator.generate()
    #print(markovstring)
    text=GenerateText()
    print(text)
    
    #ツイート内容
    params = {'status': text}
    #print(params)
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
    print('TT')

if __name__=="__main__":
    puttweet()