# 50. 文区切り
# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．

import re, sys

with open(sys.argv[1]) as f:
    for line in f:
        for sent in re.split(r'(?<=[.;:?!])\s(?=[A-Z])', line.strip()):
            print(sent)