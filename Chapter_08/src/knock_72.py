# 72. 素性抽出
# 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，
# 各単語をステミング処理したものが最低限のベースラインとなるであろう．

from knock_71 import is_stopword
from nltk.stem.porter import PorterStemmer as PS
import pickle, re
from tqdm import tqdm


def rm_symbol(sent):
	return re.sub(symbol, '', sent)


def stemming(sent):
	return ' '.join(ps.stem(word) for word in rm_symbol(sent).split() if not is_stopword(word))


def main():
	X_words, Y_labels = [], []
	with open('work/sentiment.txt', encoding='latin-1') as f:
		for line in tqdm(f):
			label, sent = line.split(' ', 1)
			X_words.append(stemming(sent))
			Y_labels.append(label)
	with open('work/X_words.pickle', mode='wb') as f, open('work/Y_labels.pickle', mode='wb') as g:
		pickle.dump(X_words, f)
		pickle.dump(Y_labels, g)


if __name__ == '__main__':
	symbol = re.compile(r"[#$%&'()*+-/:;<=>@[\]^_`{|}~”!?\"＃＄％＆’（）＝～｜‘｛＋＊｝＜＞＿－＾￥＠「；：」、。・！？]")
	ps = PS()
	main()