# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def main():
	print(n_gram(2, 0, 'I am an NLPer'))
	print(n_gram(2, 1, 'I am an NLPer'))

def n_gram(num_gram, word_or_char, word):
	if word_or_char == 0:
		word = word.split()
	return [word[i1:i1+num_gram] for i1 in range(len(word)-num_gram+1)]

if __name__ == '__main__':
	main()
