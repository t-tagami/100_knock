# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

with open('../work/merge.txt', 'w') as f13, \
        open('../work/col1.txt') as f13_1, \
        open('../work/col2.txt') as f13_2:
    for row_1, row_2 in zip(f13_1, f13_2):
        f13.write(row_1.replace('\n', '\t') + row_2.rstrip())

#UNIXコマンド
# paste -d "\t" ../work/col1.txt ../work/col2.txt