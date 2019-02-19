# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

with open('../data/hightemp.txt') as f18:
    list_line = [line.split('\t') for line in f18]
    list_line.sort(key = lambda x: x[2], reverse = True)
    for i1 in list_line: print ('\t'.join(i1).rstrip())

# UNIXコマンド
# sort -k 3 -r -n ../data/hightemp.txt