# 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
# 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

from knock_40 import Morph
from knock_41 import Chunk

for sent in Chunk.make_chunk_object_list():
    for chunk in sent:
        if chunk.dst != -1:
            if any(morph.pos == '名詞' for morph in chunk.morphs) and any(morph.pos == '動詞' for morph in sent[chunk.dst].morphs) :
                print('{:10}\t{}'.format(str(chunk), sent[chunk.dst]))