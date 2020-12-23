def nmojihosei(str,n):
    hostr=""
    for i in range(len(str)-n):
        hostr=hostr+str[i]
    return hostr

#str="私は\n素敵な\n鳩です。"
#print(nmojihosei(str,4))