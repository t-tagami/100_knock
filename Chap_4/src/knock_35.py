# 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

from knock_30 import parse
from itertools import chain, islice

connected_nouns = []
temp = []
for sent in parse():
    for word in sent:
        if word['pos'] == '名詞': temp.append(word['surface'])
        else:
            if(len(temp) > 1): connected_nouns.append(' '.join(temp))
            temp.clear()

print(connected_nouns[:10])