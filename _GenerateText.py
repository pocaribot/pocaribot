from _mecab_list import mlist
from _nmojihosei import nmojihosei
import random

def pickup():
    f = open("data.txt",encoding="utf-8")
    text = f.read()
    f.close
    #print(text)
    #text="ぽ"
    text=text.split('fghalglea')
    random.shuffle(text)
    #print(text)
    return text

def GenerateText():
    text=pickup()
    #text=["ぽ\nぽ\nぽ\n走る"]
    ending="走り回る女子高生のCM(POCARI SWEAT)"
    i=0
    generated_text=""
    while i<len(text):
        string=text[i]
        list=mlist(string)
        #print(list)
        j=len(list)-1
        while j>=0:
            katsuyou = list[j][1][4].split("・")[0]
            if list[j][1][0]=='動詞' and (katsuyou!='一段' or list[j][1][6]!='てる'):
                if katsuyou=='五段':
                    po=list[j][1][4]
                    if po[3]=='ア':
                        list[j][0] = nmojihosei(list[j][1][6],1) + "い"
                    if po[3]=='カ':
                        list[j][0] = nmojihosei(list[j][1][6],1) + "き"
                    if po[3]=='サ':
                        list[j][0] = nmojihosei(list[j][1][6],1) + "し"
                    if po[3]=='タ':
                        list[j][0] = nmojihosei(list[j][1][6],1) + "ち"
                    if po[3]=='ナ':
                        list[j][0] = nmojihosei(list[j][1][6],1) + "に"
                    if po[3]=='ハ':
                        list[j][0] = nmojihosei(list[j][1][6],1) + "ひ"
                    if po[3]=='マ':
                        list[j][0] = nmojihosei(list[j][1][6],1) + "み"
                    if po[3]=='ヤ':
                        list[j][0] = nmojihosei(list[j][1][6],1) + "い"
                    if po[3]=='ラ':
                        list[j][0] = nmojihosei(list[j][1][6],1) + "り"
                    if po[3]=='ワ':
                        list[j][0] = nmojihosei(list[j][1][6],1) + "い"
                if katsuyou=='カ変':
                    if list[j][1][6][len(list[j][1][6])-2]=='く':
                        list[j][0]=nmojihosei(list[j][1][6],2)+"き"
                    if list[j][1][6][len(list[j][1][6])-2]=='来':
                        list[j][0]=nmojihosei(list[j][1][6],1)
                if katsuyou=='サ変':
                    list[j][0]=nmojihosei(list[j][1][6],2)+"し"
                if katsuyou=='一段':
                    list[j][0]=nmojihosei(list[j][1][6],1)
                for k in range(j+1):
                    generated_text+=list[k][0]
                generated_text += "ながら"+ending
                return generated_text
            if list[j][1][0]=='形容詞':
                list[j][0]=nmojihosei(list[j][1][6],1) + "く"
                for k in range(j+1):
                    generated_text+=list[k][0]
                generated_text=generated_text+ending
                return generated_text
            if list[j][1][1]=='形容動詞語幹':
                list[j][0]=list[j][1][6] + "に"
                for k in range(j+1):
                    generated_text+=list[k][0]
                generated_text=generated_text+ending
                return generated_text
            else:
                j=j-1
        i=i+1
    return "CMの制作に失敗しました"

print(GenerateText())