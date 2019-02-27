# 73. 学習
# 72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．

import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.externals import joblib


def main():
	with open('work/X_words.pickle', 'rb') as f, open('work/Y_labels.pickle', 'rb') as g:
		X_words = pickle.load(f)
		Y_labels = pickle.load(g)

	vectorizer = CountVectorizer()

	X = vectorizer.fit_transform(X_words)
	y = [1 if label == '+1' else -1 for label in Y_labels]
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

	clf = LogisticRegression()
	clf.fit(X_train, y_train)
	joblib.dump(clf, 'work/clf.pkl')
	joblib.dump(vectorizer, 'work/vectorizer.pkl')
	print(clf.score(X_test, y_test))


if __name__ == '__main__':
	main()