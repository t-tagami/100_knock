# 53. Tokenization
# Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．

#java -cp "/Users/tagami/Documents/stanford-corenlp-full-2018-10-05/*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file data/nlp.txt work

import sys
from lxml import etree

tree = etree.parse(sys.argv[1])
for word in tree.xpath('//word'):
    print(word.text)