import MeCab
import ipadic

#string = "走る　走るagkobeorおれ～た～ち～boaignier走る　転ぶ　血が出る～"

def mlist(string):
    CHASEN_ARGS = r' -F "%m\t%f[7]\t%f[6]\t%F-[0,1,2,3]\t%f[4]\t%f[5]\n"'
    CHASEN_ARGS += r' -U "%m\t%m\t%m\t%F-[0,1,2,3]\t\t\n"'
    tagger = MeCab.Tagger(ipadic.MECAB_ARGS + CHASEN_ARGS)
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

