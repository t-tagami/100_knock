# 32. 動詞の原形
# 動詞の原形をすべて抽出せよ．

from knock_30 import parse
from itertools import chain, islice

verb_bases = {word['base'] for word in chain.from_iterable(parse()) if word['pos'] == "動詞"}

for i in islice(verb_bases, 10): print(i)