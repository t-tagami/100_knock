# coding: UTF-8
# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

with open('../data/hightemp.txt') as f12, \
        open('../work/col1.txt', 'w') as f12_1, \
            open('../work/col2.txt', 'w') as f12_2:
        for line in f12:
            list_line = line.split()
            f12_1.write(list_line[0].rstrip() + '\n')
            f12_2.write(list_line[1].rstrip() + '\n')

# UNIXコマンド
# cut -f 1 ../data/hightemp.txt
# cut -f 2 ../data/hightemp.txt