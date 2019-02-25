# 41. 係り受け解析結果の読み込み（文節・係り受け）
# 40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス
# 番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を
# 読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで
# 作ったプログラムを活用せよ．

from knock_40 import Morph
from copy import copy
from cytoolz import nth


class Chunk():
	def __init__(self, morphs, idx, dst):
		self.morphs = morphs
		self.dst = dst
		self.srcs = []
		self.idx = idx

	def __str__(self):
		return ''.join(morph.surface for morph in self.morphs if morph.surface != '記号' and morph.pos != '記号')

	@classmethod
	def set_srcs(cls, chunk_list):
		"""
		Given : List of chunk object
		Do : Set self.srcs for each chunk
		"""
		for chunk in chunk_list:
			if chunk.dst != -1:
				chunk_list[chunk.dst].srcs.append(chunk.idx)

	@classmethod
	def sent_to_chunk_object_list(cls, sent):
		result, morphs = [], []
		for line in sent:
			if line.startswith('* '):
				if morphs:
					result.append(Chunk(copy(morphs), int(idx), int(dst.rstrip('D'))))
					morphs.clear()
				_, idx, dst, *_ = line.strip().split(' ')
			else:
				morphs.append(Morph.line_to_morph(line))
		result.append(Chunk(copy(morphs), int(idx), int(dst.rstrip('D'))))
		Chunk.set_srcs(result)
		return result

	@classmethod
	def make_chunk_object_list(cls):
		for sent in Morph.read_cabocha():
			yield Chunk.sent_to_chunk_object_list(sent)

	def check_contain_pos(self, pos):
		return any(morph.pos == pos for morph in self.morphs)

	def check_contain_pos1(self, pos1):
		return any(morph.pos1 == pos1 for morph in self.morphs)

	def check_contain_sahen_wo(self):
		for i in range(len(self.morphs) - 1):
			if self.morphs[i].pos1 == 'サ変接続' and self.morphs[i + 1].surface == 'を':
				return True
		return False

	def check_contain_word(self, surface, pos):
		return any(morph.pos == pos and morph.surface == surface for morph in self.morphs)

	def get_surface_pos(self, pos):
		for morph in self.morphs:
			if morph.pos == pos: return morph.surface

	def get_left_base(self, pos):
		for morph in self.morphs:
			if morph.pos == pos:
				return morph.base

	def get_morph_surface(self):
		return ''.join(morph.surface for morph in self.morphs if morph.pos != '記号' and morph.pos != '空白')

	@classmethod
	def get_idx(cls, sent, pos):
		return [chunk.idx for chunk in sent if chunk.check_contain_pos(pos)]

	def replace_surface(self, char):
		surfaces = ''
		for morph in self.morphs:
			if morph.pos == '名詞':
				surfaces += char
			elif morph.pos != '記号':
				surfaces += morph.surface.lstrip('\u3000X')
		return surfaces

def main():
	for sent in nth(7, Chunk.make_chunk_object_list()):
		print('係り先 {:2d}\t係り元 {}\t{}'.format(sent.dst, sent.srcs, sent))


if __name__ == '__main__':
	main()