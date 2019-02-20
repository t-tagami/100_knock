# 34. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．

from knock_30 import parse
from itertools import chain, islice

noun_phrases = set()
for sent in parse():
    for idx in range(len(sent) - 2):
        if sent[idx]['pos'] == '名詞' and sent[idx+2]['pos'] == '名詞' and sent[idx+1]['surface'] == 'の':
            noun_phrases.add(f"{sent[idx]['surface']}{'の'}{sent[idx+2]['surface']}")

for i in islice(noun_phrases, 10): print(i)