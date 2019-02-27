# 74. 予測
# 73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，
# その予測確率を計算するプログラムを実装せよ．

from knock_72 import stemming
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.externals import joblib


def main(sent):
	vectorizer = joblib.load('work/vectorizer.pkl')
	clf = joblib.load('work/clf.pkl')

	X = vectorizer.transform(sent)
	return sent, clf.predict(X), clf.predict_proba(X)


if __name__ == '__main__':
	print(main(['I have a pen.']))