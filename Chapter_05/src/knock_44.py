# 44. 係り受け木の可視化
# 与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
# また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．

from knock_40 import Morph
from knock_41 import Chunk
from itertools import islice
import pygraphviz as pgv


def visualize_dependency(sent):
	G = pgv.AGraph(directed=True)
	G.node_attr['shape'] = 'box'
	G.node_attr['style'] = 'filled'
	for chunk in sent:
		G.add_node(chunk.idx, label=chunk, color='lightskyblue')
		if chunk.dst != -1:
			G.add_edge(chunk.idx, chunk.dst, color='plum', style='filled')
	dot = G.string()
	G.layout(prog='dot')
	G.draw('work/44.png')


def main():
	for sent in islice(Chunk.make_chunk_object_list(), 7, 8):
		visualize_dependency(sent)


if __name__ == '__main__':
	main()