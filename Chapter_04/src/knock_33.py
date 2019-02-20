# 33. サ変名詞
# サ変接続の名詞をすべて抽出せよ．

from knock_30 import parse
from itertools import chain, islice

sa_irregular_nouns = {word['base'] for word in chain.from_iterable(parse())
                      if word['pos1'] == "サ変接続"}
for i in islice(sa_irregular_nouns, 10): print(i)