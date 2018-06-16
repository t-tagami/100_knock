# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

from knock_36 import count
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot') #おすすめ
font = {'family':'TakaoGothic'}
mpl.rc('font', **font)
plt.rcParams["font.size"] = 25

df = pd.DataFrame(count().most_common(10), columns=['単語', '頻度'])

plt.figure(figsize=(14,8)) #サイズの変更
plt.bar(range(len(df.index)), df.頻度, color='c', alpha=0.4, tick_label=df.単語)
plt.xlabel("単語")
plt.ylabel("頻度")
plt.savefig('../work/37.png')