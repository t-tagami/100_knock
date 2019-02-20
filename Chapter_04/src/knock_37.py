# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

from knock_36 import count
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('ggplot')
font = {'family':'TakaoGothic'}
mpl.rc('font', **font)
plt.rcParams["font.size"] = 15
import pandas as pd

df = pd.DataFrame(count().most_common(10), columns=['単語', '頻度'])
df.plot(kind='bar', cmap='autumn', y='頻度')
plt.xticks(range(10), df['単語'])
plt.xlabel("単語")
plt.ylabel("頻度")
plt.savefig('../work/37.png')