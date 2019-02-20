# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ

with open('../data/hightemp.txt') as f:
    print({row.split('\t')[0] for row in f}) #set内包表記

# UNIXコマンド
# cut -f1 ../data/hightemp.txt | sort -u
