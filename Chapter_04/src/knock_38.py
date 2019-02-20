# 38. ヒストグラム
# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

from knock_36 import count
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('ggplot')
font = {'family':'TakaoGothic'}
mpl.rc('font', **font)
plt.rcParams["font.size"] = 15
import pandas as pd
import seaborn as sns

df = pd.DataFrame(count().most_common(), columns=['単語', '頻度'])
ax = df['頻度'].hist()
ax.set_yscale('log')
plt.ylabel('出現頻度をとる単語の種類数')
plt.savefig('../work/38.png')