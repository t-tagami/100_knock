# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

with open('../data/hightemp.txt') as f:
    for _ in range(int(input())): print(f.readline().rstrip())

 # head -n 10 ../data/hightemp.txt