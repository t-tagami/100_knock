# 51. 単語の切り出し
# 空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．

import re, sys

pattern = re.compile("[!-/:-@[-`{-~]")

with open(sys.argv[1]) as f:
    for line in f:
        for word in line.split(' '):
            print(re.sub(pattern, '', word))