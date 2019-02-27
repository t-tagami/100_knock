# 70. データの入手・整形
# 文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

# rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
# rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
# 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
# sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．

import random
random.seed(10)

results = []
with open('data/rt-polarity.pos', encoding='latin-1') as fp, open('data/rt-polarity.neg', encoding='latin-1') as fg:
    for pos, neg in zip(fp, fg):
        results.append('+1 ' + pos)
        results.append('-1 ' + neg)
random.shuffle(results)
for i in results: print(i.strip())

#--- unixコマンド ---
# sed 's/^/+1 /g' data/rt-polarity.pos > work/rt-polarity_added.pos
# sed 's/^/-1 /g' data/rt-polarity.neg > work/rt-polarity_added.neg
# cat work/rt-polarity_added.neg work/rt-polarity_added.pos | gshuf > work/sentiment.txt