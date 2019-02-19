# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

num_split = int(input())
num_line = sum(1 for _ in open('../data/hightemp.txt'))
with open('../data/hightemp.txt') as f16:
    for num in [(num_line + i) // num_split for i in range(num_split)]:
        for _ in range(num): print(f16.readline().rstrip())
        print()