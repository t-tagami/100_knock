# 42. 係り元と係り先の文節の表示
# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

from knock_40 import Morph
from knock_41 import Chunk

for sent in Chunk.make_chunk_object_list():
    for chunk in sent:
        if chunk.dst != -1:
            print('{:10}\t{}'.format(str(chunk), sent[chunk.dst]))