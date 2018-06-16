# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

from collections import Counter

with open('../data/hightemp.txt') as f19:
    list_line = [line.split('\t')[0] for line in f19]
    for pref, count_pref in Counter(list_line).most_common(): print(count_pref, pref)

# UNIXコマンド
# cut -f 1 data/hightemp.txt | sort | uniq -c | sort -r