# 38. ヒストグラム
# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

from knock_36 import count
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.style.use('ggplot') #おすすめ
font = {'family':'TakaoGothic'}
mpl.rc('font', **font)
plt.rcParams["font.size"] = 25

df = pd.DataFrame(count().most_common(), columns=['単語', '頻度'])

plt.figure(figsize=(14,8))
sns.distplot(df.頻度, bins=10, hist_kws={'log':True}, kde=False)
plt.ylabel('出現頻度をとる単語の種類数')
plt.savefig('../work/38.png')