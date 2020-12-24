import MeCab
import ipadic

#string = "起きろ"

def mlist(string):
    tagger = MeCab.Tagger("-Ochasen")
    tagger.parse('')
    node = tagger.parseToNode(string)

    word_class=[]
    while node:
        word=node.surface
        wclass=node.feature.split(',')
        word_class.append([word,wclass])
        node=node.next
    return word_class

#print(mlist(string))

