# 39.Zipfの法則
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

 import count
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot') #おすすめ
font = {'family':'TakaoGothic'}
mpl.rc('font', **font)
plt.rcParams["font.size"] = 25

df = pd.DataFrame(count().most_common(), columns=['単語', '頻度'])

plt.figure(figsize=(14,8))
df.頻度.plot(logx=True, logy=True)
plt.xlabel('出現頻度順位')
plt.ylabel('出現頻度')
plt.savefig('../work/39.png')