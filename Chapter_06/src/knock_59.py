# 59. S式の解析
# Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．

import sys, re
from lxml import etree
from nltk.tree import Tree

tree = etree.parse(sys.argv[1])
for parse in tree.xpath('//parse'):
    for subtree in Tree.fromstring(parse.text).subtrees():
            if subtree.label() == 'NP': print(' '.join(subtree.leaves()))