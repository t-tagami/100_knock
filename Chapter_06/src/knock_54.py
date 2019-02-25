# 54. 品詞タグ付け
# Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．

import sys
from lxml import etree

tree = etree.parse(sys.argv[1])
for token in tree.xpath('//token'):
    print('{}\t{}\t{}'.format(token.find('word').text, token.find('lemma').text, token.find('POS').text))