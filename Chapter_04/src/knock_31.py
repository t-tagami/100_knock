# 31. 動詞
# 動詞の表層形をすべて抽出せよ．

from knock_30 import parse
from itertools import chain, islice

verb_surfaces = {word['surface'] for word in chain.from_iterable(parse())
                 if word['pos'] == "動詞"}
for i in islice(verb_surfaces, 10): print(i)