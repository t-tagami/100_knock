# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

with open('../work/merge.txt', 'w') as f, \
        open('../work/col1.txt') as g, \
        open('../work/col2.txt') as h:
    for row_1, row_2 in zip(g, h):
        f.write(row_1.replace('\n', '\t') + row_2.rstrip())

#UNIXコマンド
# paste -d "\t" ../work/col1.txt ../work/col2.txt