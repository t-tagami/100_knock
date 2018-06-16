# 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

from knock_30 import parse
from itertools import chain, islice
from collections import Counter
import re

def count():
    word_count = Counter(word['base'] for word in chain.from_iterable(parse())
                         if not re.match(r'[!-〿]|\s', word['base']))
    return word_count

def main():
    for i in count().most_common(10): print(i)

if __name__ == '__main__':
    main()