# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

with open('../data/hightemp.txt') as f10:
    print('行数:{}'.format(sum([1 for _ in f10])))

# UNIXコマンド
# cat ../data/hightemp.txt | wc -l