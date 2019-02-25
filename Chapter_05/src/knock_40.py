# 40. 係り受け解析結果の読み込み（形態素）
# 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）を
# メンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリスト
# として表現し，3文目の形態素列を表示せよ．

from itertools import groupby
from cytoolz import nth


class Morph():
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1

	def __str__(self):
		return '{}\t{}\t{}\t{}'.format(self.surface, self.base, self.pos, self.pos1)

	@classmethod
	def read_cabocha(cls):
		"""
		Read .cabocha file and yield sentence
		"""
		with open('work/neko.txt.cabocha') as f:
			for is_EOS, grouped in groupby(f, key=lambda x: x.rstrip() == 'EOS'):
				if not is_EOS:
					yield grouped

	@classmethod
	def line_to_morph(cls, line):
		"""
		Return morph by reading one line
		"""
		surface, pos, pos1, _, _, _, _, base, *_ = line.strip().replace('\t', ',').split(',')
		return Morph(surface, base, pos, pos1)

	@classmethod
	def make_sent_morph_list(cls):
		"""
		Yield a list of Morph objects for each sentence
		"""
		for sent in Morph.read_cabocha():
			result = []
			for line in sent:
				if not line.startswith('* '):
					result.append(Morph.line_to_morph(line))
			if result:
				yield result


def main():
	for sent in nth(3, Morph.make_sent_morph_list()):
		print(sent)


if __name__ == '__main__':
	main()
