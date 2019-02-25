# 55. 固有表現抽出
# 入力文中の人名をすべて抜き出せ．

import sys
from lxml import etree

tree = etree.parse(sys.argv[1])
name = []
for token in tree.xpath('//token'):
    if token.find('NER').text == 'PERSON':
        name.append(token.find('word').text)
    elif name:
        print(' '.join(name))
        name.clear()
if name:
    print(' '.join(name))