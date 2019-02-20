# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
from collections import deque

deq = deque(maxlen = int(input()))
with open('../data/hightemp.txt') as f:
    for line in f: deq.append(line.rstrip())
for line in deq: print(line)

# UNIXコマンド
# tail -n 5 ../data/hightemp.txt