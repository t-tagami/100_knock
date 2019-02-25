# 58. タプルの抽出
# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．
# ただし，主語，述語，目的語の定義は以下を参考にせよ．

# 述語: nsubj関係とdobj関係の子（dependant）を持つ単語
# 主語: 述語からnsubj関係にある子（dependent）
# 目的語: 述語からdobj関係にある子（dependent）

import sys
from lxml import etree

tree = etree.parse(sys.argv[1])
for dependency in tree.xpath('//dependencies[@type="collapsed-dependencies"]'):
    nsubjs = dependency.xpath("dep[@type='nsubj']")
    for nsubj in nsubjs:
        governor_idx = nsubj.find('governor').attrib['idx']
        governor_text = nsubj.find('governor').text #述語
        dependent_text = nsubj.find('dependent').text #主語
        for dobj in dependency.xpath('dep[@type="dobj"][governor[@idx="{}"]]'.format(governor_idx)):
            print('{}\t{}\t{}'.format(dependent_text, governor_text, dobj.find('dependent').text))