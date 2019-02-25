# 57. 係り受け解析
# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に
# 変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．

import sys
from lxml import etree
from pygraphviz import AGraph

SENT_NUM = 0
G = AGraph(directed=True)
G.node_attr['shape'] = 'box'
G.node_attr['color'] = 'lightskyblue'
G.node_attr['style'] = 'filled'

tree = etree.parse(sys.argv[1])
depedencies = tree.xpath('//dependencies[@type="collapsed-dependencies"]')
for idx, dependency in enumerate(depedencies):
    if idx == SENT_NUM:
        dep_list = [[dep.find('governor').text, dep.find('dependent').text]
                        for dep in dependency.xpath('.//dep')]
        for dep in dep_list:
            G.add_edge(dep[0], dep[1], color='plum', style='filled')
        G.layout(prog='dot')
        G.draw('work/57.png')