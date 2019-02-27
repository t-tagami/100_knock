# 71. ストップワード
# 英語のストップワードのリスト（ストップリスト）を適当に作成せよ．さらに，引数に与えられた単語（文字列）がストップリストに
# 含まれている場合は真，それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．

import nltk, unittest

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(True, is_stopword('a'))

def is_stopword(word):
	stop_words = nltk.corpus.stopwords.words('english')
	return word in stop_words

def main():
	unittest.main(argv=['ignored'], exit=False)

if __name__ == '__main__':
	main()