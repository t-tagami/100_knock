# 11. タブをスペースに置換__
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ

with open('../data/hightemp.txt') as f:
    for line in f: print(line.replace('\t', ' ').rstrip())

# UNIXコマンド
# cat ../data/hightemp.txt | tr '\t' ' '