# -*- coding: utf-8 -*-
import json
from requests_oauthlib import OAuth1Session
from _GenerateText import GenerateText
import random

def puttweet():
    # APIのトークン
    CK="uMP7ZYRj9WwglabvKpMnkWPGT"
    CS="qQBywkpM7lCU9KVCeXCwUUnkzPiVEgpqb6uP4siTjvZJhUd3Jg"
    AT="1325434551217266689-H4lAyWfjLUBjpjAKMe9H6iEAOqPV8H"
    AS="4iI5frDikdWSQRmRbjGNJnc3ILzIumhVdYnIDVceiodNK"

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